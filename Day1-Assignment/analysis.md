# Agentic AI Comparison

## Scenario
This project uses a college fee system with private data.

## Chatbot
The chatbot uses only an LLM. It does not have access to private data, so it produces incorrect answers for fee-related queries. However, it works well for general tasks.

## Workflow
The rule-based workflow uses predefined rules and accesses private data directly. It produces accurate results but lacks flexibility.

## AI Agent
The AI agent combines LLM + Tools + Loop. It selects tools, performs calculations, and returns accurate results.

## Comparison

| Basis | Chatbot | Workflow | Agent |
|------|--------|---------|-------|
| Flexibility | Low | Low | High |
| Decision-making | None | Fixed | Dynamic |
| Tool usage | No | Limited | Yes |
| Private-data access | No | Yes | Yes |
| Multi-step tasks | No | Limited | Yes |
| Automation | No | Partial | Full |
| Reliability | Medium | High | High |

## Conclusion
Chatbot is useful for general queries. Workflow is reliable for fixed logic. AI agent is best for complex, multi-step tasks.