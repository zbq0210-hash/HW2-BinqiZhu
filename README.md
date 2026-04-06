# GenAI Workflow Assignment: Customer Support Response Drafting

This is a simple Python project for a beginner-friendly GenAI workflow assignment.

The workflow focuses on drafting customer support responses based on a customer's message. The project does not call a real AI model. Instead, it simulates a clear workflow that is easy to understand:

1. Read the customer issue
2. Identify the issue type and tone
3. Draft a support response
4. Review the response for quality

## Files

- `app.py` - simple Python script that runs the workflow
- `prompts.md` - example prompts for the drafting task
- `eval_set.md` - small evaluation set with sample customer messages
- `report.md` - short report describing the workflow

## How to Run

Make sure you have Python 3 installed.

```bash
python3 app.py
```

## What the Script Does

The script includes a few sample customer support tickets, such as:

- delayed delivery
- refund request
- damaged product
- password reset

For each ticket, the script:

- detects the issue type
- checks whether the customer sounds calm, upset, or frustrated
- drafts a polite support reply
- prints a short quality check

## Why This Is Useful

In a real GenAI system, a language model would generate the response. In this beginner version, we use simple Python logic so the workflow is easy to follow and explain in class.
