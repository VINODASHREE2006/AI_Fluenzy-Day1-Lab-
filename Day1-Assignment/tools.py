import ast
import operator

# PRIVATE EVENT DATA
EVENT_FEES = {
    "TECHFEST2026": 2000,
    "AIWORKSHOP2026": 1500,
    "HACKATHON2026": 2500
}

# ----------------------------
# TOOL 1: Get Event Fee
# ----------------------------
def get_event_fee(event_name: str) -> str:
    fee = EVENT_FEES.get(event_name.upper())
    if fee:
        return str(fee)
    return "Event not found"


# ----------------------------
# TOOL 2: Calculator
# ----------------------------
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        return OPS[type(node.op)](evaluate(node.left), evaluate(node.right))
    raise ValueError("Invalid expression")

def calculate(expression: str) -> str:
    try:
        return str(evaluate(ast.parse(expression, mode="eval").body))
    except:
        return "Calculation error"


# ----------------------------
# TOOL DEFINITIONS (IMPORTANT)
# ----------------------------
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_event_fee",
            "description": "Get fee of an event",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_name": {"type": "string"}
                },
                "required": ["event_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform math calculation",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }
    }
]