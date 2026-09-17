---
applyTo: "tests/**/*.py"
---

# Testing rules

- Use pytest for backend tests.
- Follow the Arrange, Act, Assert pattern.
- Reset in-memory data before every test.
- Reproduce a reported defect with a failing test before modifying production code.
- Implement the smallest correction that addresses the root cause.
- Run the relevant tests after every change.
- Do not report that a defect is fixed without successful test evidence.
