import time
import requests


def call_api(url, timeout=3, retries=1):
    for attempt in range(retries + 1):
        start = time.time()
        try:
            response = requests.get(url, timeout=timeout)
            latency = int((time.time() - start) * 1000)
            return response, latency
        except requests.RequestException:
            if attempt == retries:
                latency = int((time.time() - start) * 1000)
                return None, latency
            time.sleep(0.5)
