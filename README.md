#  Movie Recommender System

A content-based movie recommendation system that suggests the top 5 similar movies based on metadata like overview, genres, keywords, cast, and crew. The app is built with **Python**, **scikit-learn**, and **Streamlit**, and it fetches posters using the **TMDb API**.

>  **Note:** TMDb API is currently restricted in India. Use a **VPN** to load posters properly.

---

##  Demo Preview

![App Screenshot](./screenshot.png) <!-- Add your actual screenshot path -->

---

##  How It Works

1. **Data Loading & Cleaning**  
   Loads `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`, merges them, and selects relevant columns.

2. **Feature Engineering**  
   - Extracts top 3 cast members  
   - Extracts director from crew  
   - Flattens `genres` and `keywords` into text  
   - Cleans spaces and combines everything into a `tags` column

3. **Text Preprocessing**  
   - Applies stemming using `PorterStemmer`  
   - Vectorizes the `tags` using `CountVectorizer` (max 5000 features)  
   - Computes cosine similarity between movies

4. **Recommendation Logic**  
   - Given a selected movie, finds its index  
   - Sorts other movies by similarity score  
   - Returns top 5 similar movies and fetches their posters via TMDb API

5. **Web App Interface**  
   - Built with **Streamlit**  
   - Dropdown for movie selection  
   - Displays recommended titles with poster images

---

##  Tech Stack

- Python
- pandas, numpy
- scikit-learn
- nltk
- pickle
- Streamlit
- requests
- TMDb API

---

