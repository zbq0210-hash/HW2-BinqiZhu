"""
Homework 2: Customer Support Response Drafting

A simple command-line GenAI workflow that:
1. reads customer support cases
2. sends them to an LLM
3. prints structured output
4. saves results to a JSON file

Before running:
    pip install openai

Set your API key first:
    export OPENAI_API_KEY="your_api_key_here"

Run:
    python3 app.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from openai import OpenAI

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

MODEL_NAME = "gpt-4.1-mini"

EVAL_CASES = [
    {
        "id": 1,
        "label": "normal_case_delivery_delay",
        "customer_message": "I ordered a product two weeks ago and it still hasn't arrived. Can you check the status?"
    },
    {
        "id": 2,
        "label": "normal_case_refund_request",
        "customer_message": "I want to return my item and get a refund. What should I do?"
    },
    {
        "id": 3,
        "label": "edge_case_vague_input",
        "customer_message": "This is bad."
    },
    {
        "id": 4,
        "label": "edge_case_angry_customer",
        "customer_message": "This is the worst service ever. You guys are completely useless."
    },
    {
        "id": 5,
        "label": "failure_risk_unknown_account_suspension",
        "customer_message": "Why was my account suspended? I didn't do anything wrong."
    },
]

OUTPUT_FILE = Path("outputs.json")


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Please export your API key before running."
        )
    return OpenAI(api_key=api_key)


def generate_response(client: OpenAI, customer_message: str) -> str:
    user_prompt = f"""
Customer message:
{customer_message}

Write a customer support response.
""".strip()

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.output_text.strip()


def simple_review(response_text: str) -> dict[str, bool]:
    text = response_text.lower()
    return {
        "polite": any(word in text for word in ["thank you", "sorry", "apologize", "appreciate"]),
        "clear": len(response_text.split()) >= 30,
        "avoids_overclaiming": not any(
            phrase in text for phrase in [
                "your account was suspended because",
                "we confirmed that",
                "we have already fixed",
            ]
        ),
    }


def run_case(client: OpenAI, case: dict[str, Any]) -> dict[str, Any]:
    generated = generate_response(client, case["customer_message"])
    review = simple_review(generated)

    result = {
        "id": case["id"],
        "label": case["label"],
        "customer_message": case["customer_message"],
        "generated_response": generated,
        "review": review,
    }

    print("=" * 70)
    print(f"Case ID: {case['id']}")
    print(f"Label: {case['label']}")
    print("Customer Message:")
    print(case["customer_message"])
    print("\nGenerated Response:")
    print(generated)
    print("\nReview:")
    for key, value in review.items():
        print(f"- {key}: {value}")

    return result


def save_results(results: list[dict[str, Any]]) -> None:
    OUTPUT_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nSaved results to {OUTPUT_FILE}")


def main() -> None:
    client = get_client()
    print("Running customer support response drafting workflow...\n")

    results = []
    for case in EVAL_CASES:
        results.append(run_case(client, case))

    save_results(results)


if __name__ == "__main__":
    main()
