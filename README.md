LETTERBOXD RECOMMENDATIONS
    - John Zacharias, 2024

This project is a movie recommendation system that uses a trained machine learning algorithm to provide personalised film recommendations based on ratings fetched from Letterboxd. Letterboxd (letterboxd.com) is "a social network for film lovers" allowing users to log films that they have watched, rate them and write reviews. This project allows users to input their Letterboxd username and fetches their film data to provide recommendatons tailored to them.

Prediction Model
The underlying model that the project uses is a Random Forest Regressor. Datasets from Kaggle were combined to train the model. The dataset used included ratings from several users on films they watched and what the film was rated by each users, as well as data on the film itself, including genres, languages, popularity, etc. The model would predict the value of the user ratings. When users input their usernames, the program fits their data to the model and predicts their rating of the other films in the dataset, returning the films with the highest rated predictions.

Setup
- Clone repository
- Install requirements
    pip install -r requirements.txt
- Run the application
    python app.py
- Access the page on your web browser at your localhost:5000
