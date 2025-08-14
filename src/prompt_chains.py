# src/prompt_chains.py

from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
import json

class FactCheckChain:
    def __init__(self):
        self.model = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model="llama3-8b-8192",
            temperature=0,
            max_tokens=512
        )

    def verify_claim(self, claim: str, evidence: list) -> dict:
        """
        Analyze any claim vs evidence globally.
        Returns a structured JSON:
        - status: True/False
        - corrected_fact: corrected statement if False
        - reason: why the claim is false
        """
        evidence_text = "\n".join(str(e) for e in evidence) if evidence else "No evidence found."

        prompt = f"""
        You are a fact-checking assistant.
        Claim: "{claim}"
        Evidence: "{evidence_text}"

        Instructions:
        - Respond strictly in JSON format:
        {{
            "status": true/false,
            "corrected_fact": "If false, provide the corrected fact; if true, leave empty",
            "reason": "If false, explain why; if true, leave empty"
        }}
        - Always provide TRUE or FALSE in status
        - Do not add extra text outside JSON
        - Example if false:
        {{
            "status": false,
            "corrected_fact": "Italy's capital is Rome",
            "reason": "The claim said Italy's capital is France, which is incorrect"
        }}
        """

        response = self.model.invoke(prompt).content.strip()

        try:
            result = json.loads(response)
            result["status"] = bool(result.get("status", False))
            result["corrected_fact"] = result.get("corrected_fact", "")
            result["reason"] = result.get("reason", "")
            return result
        except json.JSONDecodeError:
            # fallback for any parsing failure
            return {
                "status": False,
                "corrected_fact": "Unable to verify claim",
                "reason": "Parsing error or no evidence"
            }
