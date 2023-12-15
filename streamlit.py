import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import re
from wordcloud import STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer
import itertools

# Title of the app
st.title('IMDb Reviews Analysis')

# Load the CSV file
# df = pd.read_csv('./data/reviews_labels.csv')  # Replace with the path to your file
# df = pd.read_csv('./data/updated_reviews_labels.csv')  # Replace with the path to your file
df = pd.read_csv('updated_reviews_labels_with_new_countries.csv')  # Replace with the path to your file

# Count the occurrences of each label for the pie chart
label_counts = df['label'].value_counts()

# Create a pie chart using Plotly Express
fig1 = px.pie(label_counts, values=label_counts.values, names=label_counts.index, title="Distribution des Sentiments")
st.plotly_chart(fig1)

# Preprocess text and count word frequencies
def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Split into words and remove stopwords
    words = [word for word in text.split() if word not in STOPWORDS]
    return words

# Apply preprocessing to each review and count word frequencies
all_words = sum(df['review'].apply(preprocess_text), [])
word_freq = Counter(all_words)

# Convert the word frequencies to a DataFrame
freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False).head(20)

# Create a bar chart using Plotly Express
fig2 = px.bar(freq_df, x='Word', y='Frequency', title='Top 20 Most Frequent Words in Reviews')
st.plotly_chart(fig2)

# Function to preprocess text and count word frequencies
def preprocess_and_count_words(dataframe, sentiment):
    # Filter reviews by sentiment
    filtered_reviews = dataframe[dataframe['label'] == sentiment]['review']
    # Preprocess text
    text = ' '.join(re.sub(r'[^\w\s]', '', review.lower()) for review in filtered_reviews)
    words = [word for word in text.split() if word not in STOPWORDS]
    return Counter(words)

# Calculate word frequencies for each sentiment
positive_words = preprocess_and_count_words(df, 'Positive')
negative_words = preprocess_and_count_words(df, 'Négative')
neutral_words = preprocess_and_count_words(df, 'Neutral')

# Function to create a bar chart for a sentiment
def create_bar_chart(word_freq, sentiment):
    freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False).head(10)
    fig = px.bar(freq_df, x='Word', y='Frequency', title=f'Top 10 Words in {sentiment} Reviews')
    return fig

# Display bar charts for each sentiment
st.plotly_chart(create_bar_chart(positive_words, 'Positive'))
st.plotly_chart(create_bar_chart(negative_words, 'Négative'))
st.plotly_chart(create_bar_chart(neutral_words, 'Neutral'))


# Function to extract bi-grams
def get_top_ngrams(corpus, n=None, top_k=10):
    vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:top_k]

# Extract top 10 bi-grams
top_bi_grams = get_top_ngrams(df['review'], 2, 10)

# Convert to DataFrame
bi_gram_df = pd.DataFrame(top_bi_grams, columns=['Bi-gram', 'Frequency'])

# Create a bar chart using Plotly Express
fig = px.bar(bi_gram_df, x='Bi-gram', y='Frequency', title='Top 10 Bi-grams in Reviews')
st.plotly_chart(fig)

import plotly.graph_objects as go

# ... [previous code] ...

# Count the occurrences of each country
country_counts = df['Country'].value_counts()

# Create a choropleth map
fig = go.Figure(data=go.Choropleth(
    locations = country_counts.index,
    locationmode = 'country names',
    z = country_counts.values,
    text = country_counts.index,
    colorscale = 'Portland',
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Nombre d\'avis',
))

fig.update_layout(
    title_text='Avis par Pays',
    geo=dict(
        showframe=True,
        showcoastlines=True,
        projection_type='equirectangular'
    )
)

# Display the figure in Streamlit
st.plotly_chart(fig)
