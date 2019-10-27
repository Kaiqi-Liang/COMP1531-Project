#!/bin/sh
echo "var BACKEND_PORT = $1;" > frontend/public/config.js
cd frontend
python3 static.py $2
