# Éditeur Intelligent Malagasy

##  Description
Ce projet consiste à concevoir un éditeur de texte intelligent pour la langue malagasy, une langue à faibles ressources (Low Resource Language).  
L'objectif est d'assister les utilisateurs dans la rédaction en intégrant plusieurs fonctionnalités d'intelligence artificielle adaptées au contexte malagasy.

Le projet utilise une approche hybride combinant :
- des règles linguistiques
- des méthodes algorithmiques
- des données (corpus)


##  Membres du groupe et rôles

- ANDRIANJOHANY Liantsoa Nomban'Ny Avo  IGGLIA5 N07 : Développeur Backend  
  → Implémentation du serveur Flask et des API

- ANDRIANANDRASANA Finiaina IGGLIA5 N43 : Développeur Frontend  
  → Conception de l’interface utilisateur (HTML, CSS, UX)

- RAHARINAIVO Faramampionona IGGLIA5 N52 : Ingénieur IA / NLP  
  → Développement des fonctionnalités IA (correction, sentiment, N-gram)

- RAKOTOMALALA Aina Anjaratiana IGGLIA5 N30: Data Engineer  
  → Collecte et préparation des données (corpus, dictionnaire, traduction)



##  Documentation technique

###  Architecture du système
- Backend : Python avec Flask (API REST)
- Frontend : HTML, CSS, JavaScript
- Communication : JSON via requêtes HTTP

###  Bibliothèques utilisées
- Flask → framework web
- rapidfuzz → calcul de similarité (distance de Levenshtein)
- gTTS → synthèse vocale (Text-to-Speech)
- collections → modèle N-gram

###  Structure du projet

TP_ML_S1_exam/
│
├── app.py # Backend Flask
├── data/ # Données (corpus, dictionnaire, traduction)
├── templates/ # HTML
├── static/ # CSS et fichiers audio


##  Fonctionnalités IA

###  Correcteur orthographique
Correction des mots basée sur la distance de Levenshtein avec le dictionnaire malagasy.

###  Vérification par règles linguistiques
Détection d’erreurs selon des règles spécifiques (ex : combinaisons interdites : nb, mk, dt...).

###  Lemmatisation
Extraction de la racine des mots en supprimant les préfixes et suffixes courants.

###  Autocomplétion (N-gram)
Prédiction du mot suivant à partir d’un modèle simple basé sur un corpus malagasy.

###  Traduction mot-à-mot
Traduction simple via un dictionnaire local (JSON).

###  Analyse de sentiment
Classification du texte en positif ou négatif à partir d’un ensemble de mots-clés.

###  Synthèse vocale (TTS)
Lecture du texte saisi par l’utilisateur à l’aide de gTTS.


##  Bibliographie

###  Documentation technique
- Flask : https://flask.palletsprojects.com/
- RapidFuzz : https://github.com/maxbachmann/RapidFuzz
- gTTS : https://pypi.org/project/gTTS/

###  Articles et concepts
- NLP pour langues à faibles ressources
- Modèles N-gram
- Distance de Levenshtein


##  Évolution du projet

Dans les prochaines versions, nous prévoyons :

-  Amélioration de l’interface utilisateur (éditeur riche type Google Docs)
-  Ajout d’un chatbot assistant pour aider l’utilisateur
-  Intégration d’un système de reconnaissance d’entités (NER)
-  Traduction automatique avancée
-  Augmentation du corpus malagasy
-  Autocomplétion plus intelligente (modèles plus avancés)