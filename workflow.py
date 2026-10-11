import re
from config import COURSE_FEES, QUESTIONS

def workflow(question):
    codes = re.findall(r"[A-Z]{2}\d{3}", question.upper())
    fees = [COURSE_FEES[c] for c in codes if c in COURSE_FEES]

    if not fees:
        return "Sorry, I can only answer questions about course fees."

    text = question.lower()

    if "total" in text:
        total = sum(fees)

        if "10%" in text:
            total = total * 0.9

        return f"Total fee: Rs. {int(total)}"

    if len(fees) == 1:
        return f"Fee for {codes[0]}: Rs. {fees[0]}"

    return "No rule available"


if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for q in QUESTIONS:
        print("Q:", q)
        print("A:", workflow(q))
        print("-" * 50)