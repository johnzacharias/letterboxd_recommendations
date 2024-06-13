import pandas as pd
import joblib
from sklearn.model_selection import train_test_split


model = joblib.load('models/movie_rating_model.joblib')


data = pd.read_csv('data/sample_dataset.csv', low_memory=False)


features = ['movie_id', 'user_id', 'genres', 'original_language', 'popularity', 
            'production_countries', 'release_date', 'runtime', 'spoken_languages', 
            'vote_average', 'vote_count', 'year_released', 'budget', 'revenue', 
            'status', 'keywords']
target = 'rating_val'


X = data[features]
y = data[target]
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


y_pred = model.predict(X_test)


for actual, predicted in zip(y_test[:20], y_pred[:20]):
    print(f'Actual: {actual}, Predicted: {predicted}')
