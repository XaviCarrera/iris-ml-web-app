#!/bin/bash

# Starting Flask in the background
python3 app/app.py &

# Wait for Flask to start
while ! nc -z localhost 5000; do
  sleep 1
done

# Initialize Streamlit
streamlit run app/frontend/app.py --server.port=$PORT --server.address=0.0.0.0