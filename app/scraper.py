import requests
from bs4 import BeautifulSoup

def get_letterboxd_ratings(username):
    base_url = f'https://letterboxd.com/{username}/films/ratings/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    page = 1
    ratings = []

    # loop through all pages of ratings
    while True:
        url = f'{base_url}page/{page}/' # construct the URL for the current page
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve page {page} for user {username}.")
            break

        soup = BeautifulSoup(response.content, 'html.parser') # parse the HTML content of the page
        films = soup.find_all('li', class_='poster-container') # find all films on the page

        if not films:
            break

        for film in films:
            title = film.find('img')['alt'] # extract the title of the film
            rating = film.find('span', class_='rating').text.strip() if film.find('span', class_='rating') else 'No rating' # extract the rating of the film
            ratings.append({'title': title, 'rating': rating}) # add the film to the list of ratings

        page += 1 # move to the next page

    return ratings
