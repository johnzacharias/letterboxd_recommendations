import pandas as pd
import joblib

def get_movie_recommendations(user_ratings, offset=0):
    # load the existing movie data
    movie_data = pd.read_csv('data/model_data.csv')
    # drop rows with popularity less than 1
    movie_data = movie_data[movie_data['popularity'] > 1]

    # convert user_ratings to a dataframe
    user_ratings_df = pd.DataFrame(user_ratings)

    # ensure user_ratings has the necessary columns
    if 'title' not in user_ratings_df.columns or 'rating' not in user_ratings_df.columns:
        raise ValueError("User ratings must contain 'title' and 'rating' columns")

    # merge user ratings with movie data on movie title
    merged_data = movie_data.merge(user_ratings_df, how='left', left_on='title', right_on='title')

    # fill NaN values for ratings with 0 (indicating the user has not rated the movie yet)
    merged_data['rating'] = merged_data['rating'].fillna(0)

    # load the pretrained model
    model = joblib.load('models/movie_rating_model.joblib')

    # predict ratings using the model
    merged_data['predicted_rating'] = model.predict(merged_data.drop(columns=['title', 'rating']))

    # filter out movies that the user has already seen
    unseen_movies = merged_data[merged_data['rating'] == 0]
    unseen_movies['year_released'] = unseen_movies['year_released'].astype(int)

    # sort movies by predicted ratings
    sorted_movies = unseen_movies[['movie_id', 'title', 'year_released', 'overview_metadata', 'predicted_rating']].sort_values(by='predicted_rating', ascending=False)

    # return top 15 movies
    top_movies = sorted_movies.iloc[offset:offset+15].to_dict(orient='records') #offset is used to get the next 15 movies (via load more button)

    return top_movies
