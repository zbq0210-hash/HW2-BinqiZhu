# Evaluation Set

## Case 1: Normal Case (Delayed Delivery)

**Input:**
"I ordered a product two weeks ago and it still hasn't arrived. Can you check the status?"

**Good Output Should:**

* Apologize for the delay
* Acknowledge the issue clearly
* Offer to check order status
* Maintain a polite and professional tone

---

## Case 2: Normal Case (Refund Request)

**Input:**
"I want to return my item and get a refund. What should I do?"

**Good Output Should:**

* Clearly explain the refund/return process
* Provide next steps
* Be concise and helpful
* Maintain a friendly tone

---

## Case 3: Edge Case (Very Short / Vague Input)

**Input:**
"This is bad."

**Good Output Should:**

* Politely ask for more details
* Avoid making assumptions
* Encourage the customer to clarify the issue
* Maintain a professional tone

---

## Case 4: Edge Case (Angry Customer)

**Input:**
"This is the worst service ever. You guys are completely useless."

**Good Output Should:**

* Remain calm and professional
* Show empathy
* Avoid defensive language
* Offer help or next steps

---

## Case 5: Likely Failure Case (Missing / Unknown Information)

**Input:**
"Why was my account suspended? I didn't do anything wrong."

**Good Output Should:**

* Avoid hallucinating a specific reason
* Acknowledge the concern
* Explain that further investigation is needed
* Suggest contacting support or checking account policies
* Maintain a reassuring tone
