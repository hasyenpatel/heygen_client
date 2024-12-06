Heygen Client Library

Overview
This repository simulates Heygen's video translation backend and provides a client library for polling the status of a video translation job efficiently.

Features
- Server Simulation: Returns `"pending"` until a configurable delay elapses, then either `"completed"` or `"error"`.

- Client Library (`heygen_client.py`):
  - Uses exponential backoff to reduce excessive polling.
  - Configurable via parameters and environment variables.
  - Provides logging and optional callbacks for status updates.
  - Raises `TimeoutError` if it cannot reach a terminal status within the configured retries.

Things we need to get start :

Prerequisites
- Python 3.8+
- `pip` for installing dependencies

Installation
```bash
git clone https://github.com/hasyenpatel/heygen_client.git
cd heygen_client
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install --upgrade pip
pip install -r requirements.txt

python test_integration.py # Run the test

# Expected Output

Callback: Current Status - pending
INFO:__main__:Attempt 1: Status - pending
Callback: Current Status - pending
INFO:__main__:Attempt 2: Status - pending
Callback: Current Status - pending
INFO:__main__:Attempt 3: Status - pending
Callback: Current Status - completed
INFO:__main__:Attempt 4: Status - completed
Final Status: completed


python server.py # Run the server
