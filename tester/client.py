import time
import requests


def call_api(url, timeout=5, retries=1):
    for attempt in range(retries + 1):
        start = time.time()
        try:
            # On ajoute un User-Agent pour éviter d'être bloqué comme un bot
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, timeout=timeout, headers=headers)
            latency = int((time.time() - start) * 1000)
            return response, latency
        except requests.RequestException:
            if attempt == retries:
                latency = int((time.time() - start) * 1000)
                return None, latency
            time.sleep(0.5)
