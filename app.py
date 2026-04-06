
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None  # type: ignore


MODEL_NAME = "gpt-4.1-mini"

SYSTEM_PROMPT = """
You are a helpful customer support writing assistant.

Write a professional customer support response that:
- acknowledges the customer's issue
- uses a polite and empathetic tone
- avoids making up facts not provided in the input
- suggests appropriate next steps
- stays concise and clear

If key information is missing, do not invent it.
Instead, politely ask for clarification or explain that the issue needs review.
""".strip()

OUTPUT_FILE = Path("outputs.json")


EVAL_CASES: list[dict[str, Any]] = [
    {
        "id": 1,
        "label": "normal_case_delivery_delay",
        "customer_message": (
            "I ordered a product two weeks ago and it still hasn't arrived. "
            "Can you check the status?"
        ),
    },
    {
        "id": 2,
        "label": "normal_case_refund_request",
        "customer_message": (
            "I want to return my item and get a refund. What should I do?"
        ),
    },
    {
        "id": 3,
        "label": "edge_case_vague_input",
        "customer_message": "This is bad.",
    },
    {
        "id": 4,
        "label": "edge_case_angry_customer",
        "customer_message": (
            "This is the worst service ever. You guys are completely useless."
        ),
    },
    {
        "id": 5,
        "label": "failure_risk_unknown_account_suspension",
        "customer_message": (
            "Why was my account suspended? I didn't do anything wrong."
        ),
    },
]


def get_client() -> OpenAI | None:
    """
    Return an OpenAI client if the package and API key are available.
    Otherwise return None so the script can use the fallback mode.
    """
    if OpenAI is None:
        return None

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    return OpenAI(api_key=api_key)



def fallback_response(customer_message: str) -> str:
    """
    Return a simple template response when the LLM is unavailable.
    """
    return (
        "Hello,\n\n"
        "Thank you for reaching out. I understand your concern.\n\n"
        f"You mentioned: \"{customer_message}\"\n\n"
        "Our team will review the issue and follow up with the appropriate next steps "
        "as soon as possible.\n\n"
        "Best regards,\n"
        "Customer Support Team"
    )



def generate_response(client: OpenAI | None, customer_message: str) -> tuple[str, str]:
    """
    Generate a response using the LLM if possible.
    Returns:
        (response_text, mode)
    where mode is either:
        - 'llm'
        - 'fallback'
    """
    if client is None:
        return fallback_response(customer_message), "fallback"

    user_prompt = f"""
Customer message:
{customer_message}

Write a customer support response.
""".strip()

    try:
        response = client.responses.create(
            model=MODEL_NAME,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.output_text.strip(), "llm"

    except Exception as error:
        print(f"Warning: LLM call failed ({error}). Using fallback response instead.")
        return fallback_response(customer_message), "fallback"



def simple_review(response_text: str) -> dict[str, bool]:
    """
    Perform a lightweight review of the generated response.
    """
    text = response_text.lower()

    return {
        "polite": any(
            phrase in text
            for phrase in ["thank you", "sorry", "apologize", "appreciate"]
        ),
        "clear": len(response_text.split()) >= 25,
        "avoids_overclaiming": not any(
            phrase in text
            for phrase in [
                "your account was suspended because",
                "we confirmed that",
                "we have already fixed",
                "the exact reason is",
            ]
        ),
    }



def run_case(client: OpenAI | None, case: dict[str, Any]) -> dict[str, Any]:
    """
    Run the workflow for one evaluation case.
    """
    response_text, mode = generate_response(client, case["customer_message"])
    review = simple_review(response_text)

    result = {
        "id": case["id"],
        "label": case["label"],
        "customer_message": case["customer_message"],
        "generation_mode": mode,
        "generated_response": response_text,
        "review": review,
    }

    print("=" * 70)
    print(f"Case ID: {case['id']}")
    print(f"Label: {case['label']}")
    print(f"Generation Mode: {mode}")
    print("Customer Message:")
    print(case["customer_message"])
    print("\nGenerated Response:")
    print(response_text)
    print("\nReview:")
    for key, value in review.items():
        print(f"- {key}: {value}")

    return result



def save_results(results: list[dict[str, Any]]) -> None:
    """
    Save workflow outputs to a JSON file.
    """
    OUTPUT_FILE.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nSaved results to {OUTPUT_FILE}")



def main() -> None:
    """
    Main program entry point.
    """
    client = get_client()

    if client is None:
        print("Running workflow in fallback mode (no OpenAI package or API key found).")
    else:
        print("Running workflow in LLM mode.")

    results: list[dict[str, Any]] = []

    for case in EVAL_CASES:
        result = run_case(client, case)
        results.append(result)

    save_results(results)
    print("\nWorkflow completed.")


if __name__ == "__main__":
    main()
