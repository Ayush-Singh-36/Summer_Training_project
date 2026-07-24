#!/bin/bash

# ==============================================================================
# GENERALIZED MULTI-TIER ECOSYSTEM DEPLOYMENT WRAPPER
# ==============================================================================
set -e

# Target Module Names
BACKEND_TARGET="app.py"
FRONTEND_TARGET="frontend.py"
OPTIONS_FILE="categorical_options.json"
ENV_VENV_FOLDER=".venv"

echo "===================================================================="
echo "⚡ Initiating Dual-Process Application Pipeline Infrastructure ⚡"
echo "===================================================================="

# 1. Auto-locate environment runtimes inside local subfolders
if [ -d "$ENV_VENV_FOLDER" ]; then
    source "$ENV_VENV_FOLDER/bin/activate"
elif [ -d "venv" ]; then
    source "venv/bin/activate"
fi

# 2. Defensive Check: Ensure options JSON exists before launching services
if [ ! -f "$OPTIONS_FILE" ]; then
    echo "⚠️ Warning: '$OPTIONS_FILE' not found in current directory!"
    echo "   Running generator script if available..."
    if [ -f "generate_options.py" ]; then
        python generate_options.py
    else
        echo "   ❌ Could not find 'generate_options.py'. Proceeding anyway (validation may fail)..."
    fi
fi

# 3. Trap structural break commands (Ctrl+C) to prevent background leakage
terminate_stack_workers() {
    echo -e "\n🛑 Intercept shutdown hook signal. Dropping execution runtime layers..."
    kill "$BACKEND_EXEC_PID" "$FRONTEND_EXEC_PID" 2>/dev/null || true
    exit 0
}
trap terminate_stack_workers SIGINT SIGTERM

# 4. Start FastAPI Backend
echo "📡 Mounting FastAPI Model Ingestion Engine on Local Port 8000..."
fastapi dev "$BACKEND_TARGET" --port 8000 &
BACKEND_EXEC_PID=$!

echo "⏳ Waiting for service sockets to bind properly..."
sleep 3

# 5. Start Streamlit Frontend
echo "🖥️ Mounting Streamlit Workspace Dashboard UI on Local Port 8501..."
streamlit run "$FRONTEND_TARGET" --server.port 8501 &
FRONTEND_EXEC_PID=$!

echo "===================================================================="
echo "🎯 Complete Integrated Pipeline Environment Successfully Provisioned!"
echo "📡 Open API Contracts Specs (FastAPI): http://127.0.0.1:8000/docs"
echo "🖥️ User Interaction Panel Workspace (Streamlit): http://127.0.0.1:8501"
echo "💡 To drop both process networks instantly, enter [Ctrl + C] in this terminal."
echo "===================================================================="

# Lock shell environment execution path tracking background tasks continuously
wait "$BACKEND_EXEC_PID" "$FRONTEND_EXEC_PID"