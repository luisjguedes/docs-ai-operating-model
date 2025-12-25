# Risk register (starter)

| Risk | Example | Mitigation | Owner |
|---|---|---|---|
| Hallucination | AI invents a parameter or behavior | RAG + citations, “unknown” behavior, review lane | Docs lead |
| Data leakage | Confidential input is sent externally | Data classification, redaction, tool approval | Security |
| Drift | Prompt changes degrade output quality | Prompt versioning + evaluation dataset + CI gate | Docs lead |
| Over-trust | Users treat output as authoritative | Disclaimers, citations, UI patterns | Product |

