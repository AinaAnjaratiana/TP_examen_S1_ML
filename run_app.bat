@echo off
REM ----- Fichier pour lancer ton application Flask -----

REM Se placer dans le dossier du script
cd /d %~dp0

REM Définir les variables d'environnement Flask
set FLASK_APP=app.py
set FLASK_ENV=development

REM Lancer Flask DANS CETTE FENÊTRE
python -m flask run

REM Ouvrir automatiquement le navigateur après 2 secondes
REM (optionnel : tu peux l’ouvrir toi-même si tu veux)
REM timeout /t 2 >nul
REM start "" http://127.0.0.1:5000/

echo Serveur arrêté. Appuyez sur une touche pour fermer...
pause