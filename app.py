from flask import Flask, render_template, request, jsonify
from rapidfuzz import process
from collections import defaultdict
from gtts import gTTS
import json
import os
app = Flask(__name__)

# =========================
# Chargement des données
# =========================
try:
    with open("data/dictionnaire.txt", encoding="utf-8") as f:
        mots = [line.strip().lower() for line in f]
except:
    mots = ["izaho", "ianao", "tsara", "ratsy"]

try:
    with open("data/traduction.json", encoding="utf-8") as f:
        traduction = json.load(f)
except:
    traduction = {"tsara": "bon", "ratsy": "mauvais"}

# =========================
# Modèle N-gram (autocomplétion)
# =========================
model = defaultdict(list)

try:
    with open("data/corpus.txt", encoding="utf-8") as f:
        texte = f.read().lower().split()
        for i in range(len(texte) - 1):
            model[texte[i]].append(texte[i + 1])
except:
    pass

# =========================
# Vérification règles Malagasy
# =========================
def verifier_mot(mot):
    erreurs = ["nb", "mk", "dt", "bp", "sz"]
    return not any(e in mot for e in erreurs)

# =========================
# Correction orthographique
# =========================
def corriger(mot):
    suggestion = process.extractOne(mot, mots)
    return suggestion[0] if suggestion else mot

# =========================
# Lemmatisation (simple)
# =========================
def lemmatizer(mot):
    prefixes = ["mi", "ma", "man", "mam", "mpan", "mpam"]
    suffixes = ["ana", "ina", "na"]

    for p in prefixes:
        if mot.startswith(p):
            mot = mot[len(p):]

    for s in suffixes:
        if mot.endswith(s):
            mot = mot[:-len(s)]

    return mot

# =========================
# Analyse de sentiment
# =========================
positifs = ["tsara", "faly", "mahafinaritra"]
negatifs = ["ratsy", "malahelo", "tezitra"]

def sentiment(texte):
    score = 0
    for mot in texte.lower().split():
        if mot in positifs:
            score += 1
        elif mot in negatifs:
            score -= 1
    return "Positif 😊" if score >= 0 else "Négatif 😡"

# =========================
# Autocomplétion
# =========================
def autocomplete(mot):
    return model[mot][0] if mot in model else ""

# =========================
# ROUTES
# =========================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyser", methods=["POST"])
def analyser():
    texte = request.json.get("texte", "").lower()
    resultat = []

    for mot in texte.split():
        if mot not in mots or not verifier_mot(mot):
            resultat.append({
                "mot": mot,
                "suggestion": corriger(mot),
                "lemme": lemmatizer(mot)
            })

    return jsonify({
        "corrections": resultat,
        "sentiment": sentiment(texte)
    })

@app.route("/autocomplete", methods=["POST"])
def auto():
    mot = request.json.get("mot", "").lower()
    return jsonify({"suggestion": autocomplete(mot)})

@app.route("/traduire", methods=["POST"])
def traduire():
    mot = request.json.get("mot", "").lower()
    return jsonify({"traduction": traduction.get(mot, "inconnu")})

# =========================
# Text-to-Speech (TTS)
# =========================
@app.route("/tts", methods=["POST"])
def tts():
    texte = request.json.get("texte", "")
    tts = gTTS(texte, lang="fr")
    tts.save("static/audio.mp3")
    return jsonify({"audio": "/static/audio.mp3"})

# =========================
# LANCEMENT
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)