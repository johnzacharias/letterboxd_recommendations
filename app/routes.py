from flask import app, render_template, request, jsonify
from app.scraper import get_letterboxd_ratings
from app.model import get_movie_recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ratings', methods=['POST'])
def get_ratings():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    ratings = get_letterboxd_ratings(username)
    recommendations = get_movie_recommendations(ratings)  
    return jsonify(recommendations)
