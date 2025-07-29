#  Movie Recommender System

A content-based movie recommendation system that suggests the top 5 similar movies based on an input movie title. It uses metadata such as genres, cast, crew, keywords, and overview to compute movie similarity. Posters are fetched using the TMDb API, and the user interface is built using Streamlit.

>  **Note:** TMDb API is currently restricted in India. You may need to use a **VPN** to fetch posters successfully.

---

##  Demo Preview

![App Screenshot](https://github.com/nileshdeb/Movie-Recommender/blob/main/Movie_recommender_screenshot.png) 

---

##  Features

- Suggests top 5 similar movies based on content
- Uses cosine similarity on combined metadata features
- Fetches movie posters dynamically via TMDb API
- Clean and simple user interface using Streamlit

---

##  Dataset

This project uses the **[TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** from Kaggle. It contains metadata for 5000+ movies from The Movie Database (TMDb).

### Files Used:

1. **`tmdb_5000_movies.csv`**
   - Columns: `id`, `title`, `genres`, `keywords`, `overview`, etc.

2. **`tmdb_5000_credits.csv`**
   - Columns: `movie_id`, `cast`, `crew`

### Preprocessing Steps:
- Merged both files on `movie_id`
- Extracted:
  - Top 3 cast members
  - Director from crew
  - Genre and keyword names
- Combined everything into a single `tags` column
- Applied stemming and cleaned text
- Vectorized tags using `CountVectorizer`
- Calculated similarity using cosine similarity

---

##  How It Works

1. User selects a movie title from the dropdown.
2. The system finds that movie in the data and computes similarity with all other movies.
3. It retrieves the top 5 most similar movies based on cosine similarity scores.
4. Posters for recommended movies are fetched from TMDb API and displayed.

---

##  Tech Stack

- **Language:** Python
- **Libraries:**  
  `pandas`, `numpy`, `scikit-learn`, `nltk`, `pickle`, `requests`, `ast`, `streamlit`
- **API:** TMDb API for fetching poster images

---



