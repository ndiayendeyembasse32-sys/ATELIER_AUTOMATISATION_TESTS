from tester.client import call_api


def run_all_tests():
    results = []
    base_url = "https://api.agify.io?name=michael"

    # Test 1: Statut HTTP 200
    resp, lat = call_api(base_url)
    status = "PASS" if resp and resp.status_code == 200 else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Status 200",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 2: Content-Type JSON
    status = (
        "PASS"
        if resp and "application/json" in resp.headers.get("Content-Type", "")
        else "FAIL"
    )
    results.append(
        {
            "name": "GET /?name=michael - Content-Type JSON",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 3: Champ 'name' présent
    data = resp.json() if resp and resp.status_code == 200 else {}
    status = "PASS" if "name" in data else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Has 'name'",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 4: Champ 'age' est un entier
    status = "PASS" if isinstance(data.get("age"), int) else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - 'age' is int",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 5: Champ 'count' est un entier
    status = "PASS" if isinstance(data.get("count"), int) else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - 'count' is int",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 6: Validation avec nom valide
    status = "PASS" if data.get("name") == "michael" else "FAIL"
    results.append(
        {
            "name": "GET /?name=michael - Valid value",
            "status": status,
            "latency_ms": lat,
        }
    )

    return results
