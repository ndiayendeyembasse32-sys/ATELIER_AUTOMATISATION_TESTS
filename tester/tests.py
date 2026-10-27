from tester.client import call_api


def run_all_tests():
    results = []
    base_url = "https://api.agify.io?name=michael"

    resp, lat = call_api(base_url)

    # Test 1: Statut HTTP 200
    status = "PASS" if resp and resp.status_code == 200 else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Status 200",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 2: Réponse reçue
    status = "PASS" if resp is not None else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Server Responded",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Extraction des données JSON
    data = {}
    if resp and resp.status_code == 200:
        try:
            data = resp.json()
        except Exception:
            pass

    # Test 3: Clé 'name' présente
    status = "PASS" if "name" in data else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Has 'name'",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 4: Clé 'age' présente
    status = "PASS" if "age" in data else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Has 'age'",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 5: Clé 'count' présente
    status = "PASS" if "count" in data else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Has 'count'",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 6: Valeur du nom correcte
    status = "PASS" if data.get("name") == "michael" else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Valid value",
            "status": status,
            "latency_ms": lat,
        }
    )

    return results
