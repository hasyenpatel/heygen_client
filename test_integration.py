# test_integration.py
import threading
import time
from heygen_client import HeygenClient

def start_server():
    import server
    server.run_server()

def main():
    
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    
    time.sleep(2)

    
    client = HeygenClient(
        base_url="http://127.0.0.1:5000",
        max_retries=10,
        initial_delay=1,
        max_delay=8
    )

    
    def status_callback(status):
        print(f"Callback: Current Status - {status}")

    try:
        
        final_status = client.get_status(on_update=status_callback)
        print(f"Final Status: {final_status}")
    except TimeoutError as e:
        print(f"TimeoutError: {e}")

if __name__ == "__main__":
    main()