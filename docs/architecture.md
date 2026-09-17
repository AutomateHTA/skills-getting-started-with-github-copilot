# Architecture

```mermaid
flowchart LR
    U[Browser user]

    HTML[static/index.html]
    JS[static/app.js]
    CSS[static/styles.css]

    API[FastAPI backend in src/app.py]
    GET[GET /activities]
    POST[POST signup endpoint]
    DELETE[DELETE unregister endpoint]
    DATA[in-memory activities data]
    TESTS[pytest tests]

    U --> HTML
    HTML --> JS
    HTML --> CSS

    JS -->|fetches activities| GET
    JS -->|submits signup| POST
    JS -->|removes participant| DELETE

    GET --> API
    POST --> API
    DELETE --> API

    API --> DATA
    DATA -->|returns activity data| GET
    DATA -->|stores signup| POST
    DATA -->|removes participant| DELETE

    TESTS -->|verifies API behavior| API
    TESTS -->|checks data updates| DATA
```

This diagram reflects the project structure and runtime flow in the repository:

- The browser loads the static HTML, CSS, and JavaScript.
- The frontend JavaScript calls the FastAPI backend routes.
- The backend reads and updates the in-memory `activities` dataset in `src/app.py`.
- The pytest suite validates the API endpoints and their behavior.
