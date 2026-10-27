from flask import Flask, jsonify, render_template
from storage import init_db, list_runs, save_run
from tester.runner import execute_run

app = Flask(__name__)

# Initialise la base SQLite au démarrage
init_db()  #[cite: 11, 13]


@app.route("/run")  #
def trigger_run():
    """Exécute la série de tests et sauvegarde le résultat[cite: 11, 13]."""
    data = execute_run()
    save_run(data)
    return jsonify({"message": "Run exécuté avec succès !", "data": data})


@app.route("/dashboard")  #[cite: 13]
def dashboard():
    """Affiche le tableau de bord avec le dernier run et l'historique[cite: 11, 13, 15]."""
    runs = list_runs()
    last_run = runs[0] if runs else None
    return render_template("dashboard.html", last_run=last_run, runs=runs)


@app.route("/health")  #[cite: 13, 15]
def health():
    """Endpoint de santé pour vérifier le bon fonctionnement (Bonus)[cite: 13, 15]."""
    return jsonify({"status": "OK", "database": "connected"})
