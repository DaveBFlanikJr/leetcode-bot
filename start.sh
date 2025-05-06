#!/bin/bash
echo "Killing any process using port 3000..."
lsof -ti tcp:3000 | xargs kill -9 2>/dev/null

echo "Starting Slack bot server..."

# entry point to app
uvicorn main:api --reload --port 3000

# Sleep for a second to make sure server is up
sleep 1

echo "Starting ngrok tunnel..."
# Run ngrok normally (in the foreground)
ngrok http 3000
