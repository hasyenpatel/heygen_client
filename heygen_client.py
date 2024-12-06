# heygen_client.py
import requests
import time
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HeygenClient:
    def __init__(
        self,
        base_url=None,
        max_retries=None,
        initial_delay=None,
        max_delay=None
    ):
        

        self.base_url = base_url or os.getenv("HEYGEN_BASE_URL", "http://localhost:5000")
        self.max_retries = max_retries or int(os.getenv("HEYGEN_MAX_RETRIES", 5))
        self.initial_delay = initial_delay or float(os.getenv("HEYGEN_INITIAL_DELAY", 1))
        self.max_delay = max_delay or float(os.getenv("HEYGEN_MAX_DELAY", 30))

    def get_status(self, on_update=None):
        
        retries = 0
        delay = self.initial_delay

        while retries < self.max_retries:
            try:
                response = requests.get(f"{self.base_url}/status", timeout=5)
                response.raise_for_status()
                result = response.json().get("result")
                logger.info(f"Attempt {retries + 1}: Status - {result}")

                if on_update:
                    on_update(result)

                if result == "pending":
                    time.sleep(delay)
                    delay = min(delay * 2, self.max_delay)
                    retries += 1
                elif result in ["completed", "error"]:
                    return result
                else:
                    raise ValueError(f"Unknown status: {result}")
            except (requests.RequestException, ValueError) as e:
                logger.error(f"Attempt {retries + 1}: Error - {e}")
                if on_update:
                    on_update(f"error: {e}")
                time.sleep(delay)
                delay = min(delay * 2, self.max_delay)
                retries += 1

        raise TimeoutError("Max retries exceeded without completion.")