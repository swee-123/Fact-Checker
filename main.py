# main.py

import streamlit as st
from src.fact_checker import FactChecker

st.set_page_config(page_title="Fact Checker", page_icon="✅", layout="centered")
st.title("🔍AI Fact Checker")
st.write("Enter any claim and get True if correct, or the corrected fact and reason if false.")

fact_checker = FactChecker()

claim = st.text_area("Enter a claim to fact-check:", height=120)

if st.button("Check Facts"):
    if not claim.strip():
        st.warning("Please enter a claim.")
    else:
        with st.spinner("Analyzing claim..."):
            result = fact_checker.check_claim(claim)

        st.subheader("✅ Fact Check Result")
        st.markdown(f"**Claim:** {claim}")
        st.markdown(f"**Result:** {result['status']}")
        if not result['status']:
            st.markdown(f"**Corrected Fact:** {result['corrected_fact']}")
            st.markdown(f"**Reason:** {result['reason']}")
