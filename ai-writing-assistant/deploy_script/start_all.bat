@echo off
start cmd /k "cd frontend && npm run dev"
start cmd /k "cd backend && python main.py"
start cmd /k "cd model_service && python model_server.py"