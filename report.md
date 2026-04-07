





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
