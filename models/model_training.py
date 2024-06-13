import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib


start_time = time.time()


data = pd.read_csv('data/sample_dataset.csv', low_memory=False)


features = ['movie_id', 'user_id', 'genres', 'original_language', 'popularity', 
            'production_countries', 'release_date', 'runtime', 'spoken_languages', 
            'vote_average', 'vote_count', 'year_released', 'budget', 'revenue', 
            'status', 'keywords']
target = 'rating_val'



#list of numerical and categorical features for normalisation
numerical_features = ['popularity', 'runtime', 'vote_average', 'vote_count', 
                      'year_released', 'budget', 'revenue']
categorical_features = ['movie_id', 'user_id', 'genres', 'original_language', 
                        'production_countries', 'spoken_languages', 'status', 'keywords']


#normalise data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])


categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])


preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])


model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=10, n_jobs=-1, random_state=42))
])

#split data into training and testing sets
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the model
print("Training the model...")
model.fit(X_train, y_train)
print("Model training complete.")

#evaluate the model
print("Evaluating the model...")
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}') #calculate mean squared error
print(f'Mean Absolute Error: {mae}')


joblib.dump(model, 'models/movie_rating_model.joblib') #save the model
print("Model saved to models/movie_rating_model.joblib")


end_time = time.time() #calculate the time taken to train the model
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time} seconds")


def predict(new_data):
    return model.predict(new_data)
