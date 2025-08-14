# src/fact_checker.py

from src.prompt_chains import FactCheckChain
from src.search_tools import search_web

class FactChecker:
    def __init__(self, api_key=None, prompts=None):
        self.chain = FactCheckChain()
        self.prompts = prompts

    def check_claim(self, claim: str) -> dict:
        """
        Verify any global claim.
        Returns structured result:
        {
            "status": True/False,
            "corrected_fact": ...,
            "reason": ...
        }
        """
        evidence = search_web(claim)
        result = self.chain.verify_claim(claim, evidence)
        return result
