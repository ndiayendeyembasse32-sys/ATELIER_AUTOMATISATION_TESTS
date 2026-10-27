from tester.client import call_api


def run_all_tests():
    results = []
    base_url = "https://api.quotable.io/random"

    # Test 1: Statut HTTP 200
    resp, lat = call_api(base_url)
    status = "PASS" if resp and resp.status_code == 200 else "FAIL"
    results.append(
        {
            "name": "GET /random - Status 200",
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
            "name": "GET /random - Content-Type JSON",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 3: Champ 'content' présent
    data = resp.json() if resp and resp.status_code == 200 else {}
    status = "PASS" if "content" in data else "FAIL"
    results.append(
        {
            "name": "GET /random - Has 'content'",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 4: Champ 'author' de type string
    status = "PASS" if isinstance(data.get("author"), str) else "FAIL"
    results.append(
        {
            "name": "GET /random - 'author' is string",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 5: Champ 'length' de type int
    status = "PASS" if isinstance(data.get("length"), int) else "FAIL"
    results.append(
        {
            "name": "GET /random - 'length' is int",
            "status": status,
            "latency_ms": lat,
        }
    )

    # Test 6: Route inexistante retourne 404
    bad_resp, bad_lat = call_api("https://api.quotable.io/invalid_endpoint")
    status = "PASS" if bad_resp and bad_resp.status_code == 404 else "FAIL"
    results.append(
        {
            "name": "GET /invalid - Status 404",
            "status": status,
            "latency_ms": bad_lat,
        }
    )

    return results
