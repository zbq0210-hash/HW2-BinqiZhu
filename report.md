## Business Use Case

The selected workflow for this project is **drafting customer support responses**. This workflow is commonly used in businesses where customer support agents need to respond to customer inquiries, complaints, or requests in a professional and efficient manner.

## User

The primary users of this system are customer support agents who are responsible for communicating with customers through written messages.

## Input

The input to the system is a customer message. This may include complaints, questions, or requests.

Example:
"I ordered a product two weeks ago and it still hasn't arrived. This is very frustrating."

## Output

The output is a professional, polite, and helpful response that addresses the customer’s issue and provides appropriate next steps.

Example:
"Thank you for reaching out. We sincerely apologize for the delay in your order. I understand how frustrating this must be. Let me check the status for you and provide an update shortly."

## Workflow Steps

1. Input: receive a customer message
2. Analysis: identify the main issue and customer intent
3. Tone handling: ensure the response is polite and empathetic
4. Response drafting: generate a clear and helpful reply
5. Review: check for clarity, professionalism, and completeness

## Why This Workflow Matters

Customer support teams handle a high volume of similar inquiries. A GenAI-assisted workflow can:

* Improve response speed
* Ensure consistent tone and quality
* Reduce workload for support agents
* Help less experienced agents produce better responses

## Limitations

* The system may generate incorrect or incomplete information
* Some cases may require human review, especially for complex or sensitive issues
* The quality of responses depends on prompt design and model behavior

## Possible Future Improvements

Future improvements could include:

* Better prompt engineering for more accurate responses
* Integration with customer databases for personalized replies
* More robust evaluation methods to measure response quality





## Model Choice

This project uses the `gpt-4.1-mini` model because it provides a good balance between cost, speed, and output quality. It is capable of generating clear and professional customer support responses while remaining efficient for a simple prototype.

Although larger models may produce more detailed responses, this model is sufficient for demonstrating a basic GenAI workflow.

---

## Baseline vs Final Design

The initial version of the system used a very simple prompt with minimal instructions. As a result, the generated responses were often generic and sometimes made unsupported assumptions.

After iterating on the prompt, the final version included clearer guidance on tone, empathy, and avoiding hallucinated information. It also instructed the model to ask for clarification when necessary instead of making assumptions.

This improvement was especially noticeable in more difficult cases. For example, in the account suspension scenario, the initial version might guess a reason for the suspension, while the final version avoids making unsupported claims and instead suggests further review.

Overall, prompt iteration improved response quality, consistency, and reliability.

---

## Limitations

The system still has several limitations. The model may generate responses that are too general or fail to fully resolve complex customer issues. It also does not have access to real customer data, which limits its ability to provide specific or personalized solutions.

Additionally, some cases require human judgment, especially when the issue involves sensitive topics or incomplete information.

---

## Deployment Recommendation

This workflow is best used as a **first-draft assistant** for customer support agents rather than a fully automated system.

Human review is recommended, especially for complex or high-risk cases. With proper oversight, the system can improve efficiency and consistency while reducing the workload for support teams.

Overall, the workflow is suitable for partial deployment with a human-in-the-loop approach.
