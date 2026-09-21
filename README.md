# 🤖 AI Agent Lab – Course Fee Assistant

This project demonstrates the difference between:

- 🧠 Plain Chatbot (LLM only)
- ⚙️ Rule-Based Workflow
- 🤖 AI Agent (LLM + Tools + Loop)

using a **course fee assistant scenario**.

---

## 📌 Scenario

A student asks questions like:

- What is the fee for AI202?
- What is the total fee after a 10% scholarship?
- Which courses fit within a budget?

The system must use **private data (course fees)** and perform calculations.

---

## 🧱 Project Structure


AI-Agent-Lab/
│
├── chatbot.py # Plain chatbot (LLM only)
├── workflow.py # Rule-based workflow
├── agent.py # AI agent (LLM + tools + loop)
├── tools.py # Functions (fee lookup, calculator)
├── config.py # Model + API setup
├── challenge.py # Budget-based question
├── check_setup.py # Environment test
│
├── Output/ # Screenshots of outputs
│ ├── chatbot.png
│ ├── workflow.png
│ ├── agent.png
│
├── .env.example # Example environment file
├── .gitignore # Ignore secrets & venv
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Setup environment variables

Create a .env file:

PROVIDER=groq
MODEL=mixtral-8x7b-32768
GROQ_API_KEY=your_api_key_here

⚠️ Important: Never commit .env to GitHub

🚀 How to Run
🔹 Check setup
python check_setup.py
🔹 Run Chatbot
python chatbot.py

👉 Uses only LLM → cannot access private data

🔹 Run Workflow
python workflow.py

👉 Uses fixed rules → works only for predefined cases

🔹 Run Agent ⭐
python agent.py

👉 Uses:

LLM (reasoning)
Tools (data + calculation)
Loop (multi-step execution)
🔹 Run Challenge
python challenge.py

👉 Finds best courses under budget

🧠 Key Concepts Demonstrated
🟢 Chatbot
No tool usage
No private data access
Can hallucinate or ask for input
🔵 Rule-Based Workflow
Deterministic logic
Accurate but rigid
Limited flexibility
🔴 AI Agent
Uses tools dynamically
Handles multi-step reasoning
Combines flexibility + accuracy
📊 Example Output
Q: What is the total fee for CS101 and AI202 after 10% scholarship?

step 1: get_course_fee(CS101) → 12000  
step 2: get_course_fee(AI202) → 18000  
step 3: calculator(...) → 27000  

Answer: ₹27,000
🔐 Security
.env is ignored using .gitignore
API keys are never pushed
.env.example provided for reference
🧠 Learning Outcome

This project clearly shows:

Approach	Capability
Chatbot	Natural language, no data access
Workflow	Accurate but rigid
Agent	Intelligent, flexible, and tool-driven
🏁 Conclusion
Use Chatbot for general Q&A
Use Workflow for simple automation
Use AI Agent for real-world complex problems
