from tester.tests import run_all_tests


def execute_run():
    tests = run_all_tests()
    passed = sum(1 for t in tests if t["status"] == "PASS")
    failed = len(tests) - passed
    latencies = [t["latency_ms"] for t in tests]

    avg_lat = sum(latencies) / len(latencies) if latencies else 0
    latencies.sort()
    p95_lat = latencies[int(len(latencies) * 0.95)] if latencies else 0

    return {
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": round(failed / len(tests), 2) if tests else 0,
            "latency_ms_avg": round(avg_lat, 2),
            "latency_ms_p95": round(p95_lat, 2),
        },
        "tests": tests,
    }
