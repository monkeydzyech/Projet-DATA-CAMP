import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
 
# Titre de l'application
st.title('IMDb Reviews Analysis')
 
# Charger le fichier CSV
df = pd.read_csv('maroc_test.csv')
 
# Télécharger les stopwords si nécessaire
nltk.download('stopwords')
 
# Fusionner tous les avis en une seule chaîne de texte
text = " ".join(review for review in df['review'])
 
# Définir les stopwords (mots à ignorer)
stop_words = set(stopwords.words('english'))  # Utiliser 'french' pour les stopwords en français
 
# Créer et générer un nuage de mots
wordcloud = WordCloud(stopwords=stop_words, background_color="white").generate(text)
 
# Afficher le nuage de mots
st.image(wordcloud.to_array(), use_container_width=True)
 
# Distribution de reviews par pays (Top 10)
country_counts = df['Country'].value_counts().head(10)  # Top 10 countries
fig_country = px.bar(country_counts, orientation='h', labels={'value':'Nombre d\'Avis', 'index':'Pays'}, title='Top 10 Pays par Nombre d\'Avis')
st.plotly_chart(fig_country)
 
# Distribution de reviews par sexe
gender_counts = df['Sexe'].value_counts()
fig_gender = px.bar(x=gender_counts.index, y=gender_counts.values, labels={'x':'Sexe', 'y':'Nombre d\'Avis'}, title='Répartition des Avis par Sexe')
st.plotly_chart(fig_gender)
 
# Distribution d'âge
fig_age = px.histogram(df, x='Age', nbins=20, title='Distribution des Âges')
st.plotly_chart(fig_age)


