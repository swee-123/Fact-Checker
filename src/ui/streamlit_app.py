import streamlit as st
from src.fact_checker import FactChecker
from src.utils import hash_text, cache_result, get_cache

# Initialize FactChecker
bot = FactChecker()

# Streamlit page configuration
st.set_page_config(page_title="AI Fact-Checker Bot", page_icon="🕵️‍♂️", layout="centered")
st.title("🕵️‍♂️ AI Fact-Checker Bot")
st.write("Enter a claim below, and the bot will verify it using AI and web search evidence.")

# Input claim
claim = st.text_input("Enter your claim here:")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

if st.button("Check Claim"):
    if not claim.strip():
        st.warning("Please enter a claim to fact-check.")
    else:
        claim_key = hash_text(claim)  # For caching

        # Check cache first
        cached_answer = get_cache(claim_key)
        if cached_answer:
            result = cached_answer
            st.info("Retrieved from cache.")
        else:
            with st.spinner("Fact-checking the claim..."):
                try:
                    result = bot.check_claim(claim)
                    cache_result(claim_key, result)  # Save to cache
                except Exception as e:
                    st.error(f"Error during fact-checking: {e}")
                    result = "Error occurred."

        # Display result
        st.subheader("Fact-Checked Answer:")
        st.write(result)

        # Save to history
        st.session_state.history.append((claim, result))

# Display previous 5 claims
if st.session_state.history:
    st.subheader("Previous Claims Checked")
    for i, (c, r) in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.markdown(f"**{i}. Claim:** {c}")
        st.markdown(f"**Answer:** {r}")
        st.markdown("---")
