from datetime import datetime
import json
import sqlite3

DB_NAME = "database.db"


def init_db():
    """Crée la table SQLite pour conserver l'historique des runs[cite: 11, 13]."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    summary TEXT,
                    tests TEXT
                )""")
    conn.commit()
    conn.close()


def save_run(run_data):
    """Enregistre un nouveau résultat de test dans SQLite[cite: 11, 13, 14]."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO runs (timestamp, summary, tests) VALUES (?, ?, ?)",
        (
            datetime.now().isoformat(),
            json.dumps(run_data["summary"]),
            json.dumps(run_data["tests"]),
        ),
    )
    conn.commit()
    conn.close()


def list_runs():
    """Récupère l'historique de tous les runs enregistrés[cite: 11, 13]."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT timestamp, summary, tests FROM runs ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    runs = []
    for r in rows:
        runs.append(
            {
                "timestamp": r[0],
                "summary": json.loads(r[1]),
                "tests": json.loads(r[2]),
            }
        )
    return runs
