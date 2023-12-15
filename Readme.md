# Analyse des Commentaires IMDb avec Streamlit

Ce projet utilise Streamlit pour analyser et visualiser les commentaires IMDb d'un film donné. L'application comprend plusieurs fonctionnalités, notamment :



1. Cloner le repository :

```bash
git clone https://github.com/monkeydzyech/Projet-DATA-CAMP.git
cd votre-projet
streamlit run streamlit.py

L'application se lance dans le navigateur par défaut et offre différentes visualisations interactives des commentaires IMDb.

Fonctionnalités
Distribution des Sentiments :

Un graphique circulaire indique la répartition des sentiments parmi les commentaires (positif, négatif, neutre).
Top Mots Fréquents :

Un diagramme à barres présente les 20 mots les plus fréquemment utilisés dans les commentaires.
Top Bi-grammes :

Un autre diagramme à barres affiche les 10 bi-grammes les plus fréquents dans les commentaires.
Carte des Avis par Pays :

Une carte choroplèthe montre la distribution géographique des avis en fonction des pays.
Prétraitement des Données
Les commentaires sont prétraités pour enlever la ponctuation, convertir en minuscules et éliminer les mots vides.

Technologies Utilisées
Streamlit
Pandas
Plotly Express
WordCloud
Scikit-learn
Contributeurs
Elias Frik, Youssef AlBagoury, Aziz BEN AYED, Ossama Louridi, Victoire Borletsis
