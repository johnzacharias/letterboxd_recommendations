import logging
from flask import Flask, render_template, request, jsonify
from scraper import get_letterboxd_ratings
from model import get_movie_recommendations

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations(): 
    data = request.get_json()
    username = data.get('username') 

    if not username: # if username is not provided return an error
        return jsonify({'error': 'Username is required'}), 400

    logger.info(f"Scraping data for user {username}")
    user_ratings = get_letterboxd_ratings(username) # get the ratings for the user
    logger.info(f"Scraped {len(user_ratings)} ratings for user {username}")

    logger.info(f"Generating movie recommendations for user {username}")
    recommendations = get_movie_recommendations(user_ratings) # get the movie recommendations for the user
    logger.info(f"Generated {len(recommendations)} recommendations for user {username}")

    return render_template('recommendations.html', recommendations=recommendations, username=username)


@app.route('/get_more_recommendations', methods=['POST'])
def get_more_recommendations():
    data = request.get_json()
    username = data.get('username')
    offset = data.get('offset', 0)

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    logger.info(f"Scraping data for user {username}")
    user_ratings = get_letterboxd_ratings(username)
    logger.info(f"Scraped {len(user_ratings)} ratings for user {username}")

    logger.info(f"Generating more movie recommendations for user {username} with offset {offset}")
    recommendations = get_movie_recommendations(user_ratings, offset)
    logger.info(f"Generated {len(recommendations)} more recommendations for user {username}")

    return jsonify({'recommendations': recommendations, 'username': username})



if __name__ == '__main__':
    app.run(debug=True)
