# Taizz POS — Proposed scaffold

This branch (feature/fastapi-vue-pos) contains a minimal POS scaffold:
- backend: FastAPI + SQLite (backend/app)
- frontend: Vue 3 + Vite (frontend)

How to run (local dev):
1. Backend:
   - python -m venv .venv
   - source .venv/bin/activate
   - pip install -r backend/requirements.txt
   - cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

2. Frontend:
   - cd frontend
   - npm install
   - npm run dev

Notes:
- Frontend expects API under /api (use Vite proxy or host together).
- This is a minimal demo to start; we can extend with auth, receipts, reports, and docker-compose.
