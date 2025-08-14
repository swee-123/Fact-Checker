import pytest
from src.fact_checker import FactChecker

@pytest.fixture
def fact_checker():
    return FactChecker()

def test_initial_response(fact_checker):
    claim = "The Eiffel Tower is in Berlin."
    response = fact_checker.initial_response(claim)
    assert isinstance(response, str)
    assert len(response) > 0

def test_assumption_extraction(fact_checker):
    answer = "The Eiffel Tower is located in Berlin, which is the capital of Germany."
    assumptions = fact_checker.extract_assumptions(answer)
    assert isinstance(assumptions, list)
    assert all(isinstance(a, str) for a in assumptions)

def test_verify_assumption(fact_checker):
    assumption = "The Eiffel Tower is in Berlin."
    evidence = "The Eiffel Tower is in Paris, France."
    verification = fact_checker.verify_assumption(assumption, evidence)
    assert verification in ["true", "false", "uncertain"]

def test_synthesize_answer(fact_checker):
    initial_answer = "The Eiffel Tower is in Berlin."
    verification_results = [{"assumption": "The Eiffel Tower is in Berlin.", "status": "false"}]
    final_answer = fact_checker.synthesize_answer(initial_answer, verification_results)
    assert isinstance(final_answer, str)
