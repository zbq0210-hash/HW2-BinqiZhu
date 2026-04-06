"""
Simple GenAI workflow assignment:
Drafting customer support responses.

This script simulates a GenAI workflow without external libraries.
"""


support_tickets = [
    {
        "id": 1,
        "customer_message": "Hi, my order was supposed to arrive three days ago and I still have not received it. Can you help?",
    },
    {
        "id": 2,
        "customer_message": "I want a refund. The item arrived damaged and I am very disappointed.",
    },
    {
        "id": 3,
        "customer_message": "Hello, I forgot my password and I cannot log into my account.",
    },
    {
        "id": 4,
        "customer_message": "This is the second time I have contacted support. My package is late and I need an update now.",
    },
]


def classify_issue(message):
    """Identify the main support issue."""
    text = message.lower()

    if "refund" in text:
        return "refund request"
    if "damaged" in text or "broken" in text:
        return "damaged product"
    if "password" in text or "log into" in text or "login" in text:
        return "account access"
    if "late" in text or "arrive" in text or "received" in text or "package" in text:
        return "delivery problem"
    return "general support"


def detect_tone(message):
    """Estimate the customer's tone in a simple way."""
    text = message.lower()

    strong_words = ["disappointed", "upset", "angry", "now", "second time"]
    if any(word in text for word in strong_words):
        return "frustrated"
    if "help" in text or "hello" in text or "hi" in text:
        return "calm"
    return "neutral"


def draft_response(issue_type, tone):
    """Create a friendly support response."""
    opening = "Hello,"

    if tone == "frustrated":
        empathy = "I am sorry for the frustration this has caused."
    elif tone == "calm":
        empathy = "Thank you for reaching out."
    else:
        empathy = "I understand your concern."

    if issue_type == "delivery problem":
        body = (
            "I checked your message and understand that your order has not arrived yet. "
            "Our next step would be to review the shipping status and provide an update as soon as possible."
        )
    elif issue_type == "refund request":
        body = (
            "I understand that you would like a refund. "
            "We can help review your order and explain the refund process."
        )
    elif issue_type == "damaged product":
        body = (
            "I am sorry that your item arrived damaged. "
            "We can help with a replacement or refund after reviewing the order details."
        )
    elif issue_type == "account access":
        body = (
            "It sounds like you are having trouble accessing your account. "
            "The next step is to start the password reset process and confirm your account details."
        )
    else:
        body = (
            "Thank you for sharing the issue. "
            "Our support team can review the details and help with the next step."
        )

    closing = "Please let us know if you would like us to continue assisting you."
    return f"{opening} {empathy} {body} {closing}"


def review_response(response):
    """Perform a simple quality check."""
    checks = {
        "polite": "please" in response.lower() or "thank you" in response.lower(),
        "clear": len(response.split()) > 20,
        "professional": any(
            phrase in response.lower()
            for phrase in ["sorry", "understand", "thank you", "next step"]
        ),
    }
    return checks


def run_workflow(ticket):
    """Run the full workflow for one support ticket."""
    message = ticket["customer_message"]
    issue_type = classify_issue(message)
    tone = detect_tone(message)
    response = draft_response(issue_type, tone)
    checks = review_response(response)

    print("=" * 60)
    print(f"Ticket ID: {ticket['id']}")
    print(f"Customer Message: {message}")
    print(f"Issue Type: {issue_type}")
    print(f"Tone: {tone}")
    print("Draft Response:")
    print(response)
    print("Quality Check:")
    for name, result in checks.items():
        print(f"- {name}: {result}")


def main():
    print("Customer Support Response Drafting Workflow")
    for ticket in support_tickets:
        run_workflow(ticket)


if __name__ == "__main__":
    main()
