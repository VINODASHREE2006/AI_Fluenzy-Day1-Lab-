# 🤖 Agentic AI: Chatbot vs Workflow vs AI Agent

This project compares three approaches:
1. Plain Chatbot (LLM only)
2. Rule-Based Workflow
3. AI Agent (LLM + Tools + Loop)

---

## 📌 Scenario

A college event registration system with **private event fee data**:

| Event | Fee |
|------|------|
| TECHFEST2026 | ₹2000 |
| AIWORKSHOP2026 | ₹1500 |
| HACKATHON2026 | ₹2500 |

---

## ⚙️ Systems Implemented

### 1️⃣ Chatbot
- Uses only LLM
- No access to private data
- ❌ Hallucinates answers

---

### 2️⃣ Rule-Based Workflow
- Uses hardcoded rules
- ✅ Accurate
- ❌ Not flexible

---

### 3️⃣ AI Agent
- Uses **LLM + Tools + Loop**
- Calls tools dynamically
- Handles multi-step reasoning

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python chatbot.py
python workflow.py
python agent.py
📸 Example Outputs
🔹 Chatbot Output (Incorrect for private data)
Q: What is the registration fee for TECHFEST2026?
A: Around ₹3000 (incorrect)
🔹 Workflow Output (Correct but limited)
Q: What is the registration fee for TECHFEST2026?
A: ₹2000
🔹 Agent Output (Correct + reasoning)
Tool called: get_event_fee
Arguments: {'event_name': 'TECHFEST2026'}

Final Answer: The fee is ₹2000
🔹 Multi-step Example
Q: Total cost after 10% discount?

Tool called: get_event_fee → 2000
Tool called: get_event_fee → 1500
Tool called: calculate → (2000+1500)*0.9

Final Answer: ₹3150
📊 Comparison
Feature	Chatbot	Workflow	Agent
Flexibility	Low	Low	High
Accuracy	Low	High	High
Tool Usage	No	Limited	Yes
Multi-step	No	Limited	Yes
🧠 Key Concept

Agent = LLM + Tools + Loop

📁 Project Structure
day1_lab/
│
├── chatbot.py
├── workflow.py
├── agent.py
├── tools.py
├── config.py
├── .env (not uploaded)
├── .gitignore
├── README.md
└── Output/
🔐 Security Note

The .env file is excluded using .gitignore to keep API keys safe.

🎯 Conclusion
Chatbot → general conversation
Workflow → fixed tasks
Agent → complex intelligent systems

---

# 📸 3. Add Screenshots (IMPORTANT)

👉 Put inside `Output/` folder:
- chatbot.png
- workflow.png
- agent.png

---

# 🚀 4. Push to GitHub (STEP-BY-STEP)

### Initialize repo

```bash
git init