import requests
from decouple import config

RANDOM_TRIVIA_URL = config('RANDOM_TRIVIA_URL')


def get_random_questions():
    response = requests.get(RANDOM_TRIVIA_URL)
    if response.status_code == requests.codes.ok:
        quiz_questions = response.json()
        return quiz_questions
    else:
        error_message = f'API request failed: {response.status_code}'
        return error_message


def get_questions_for_category(category):
    category_trivia_url = config(f'{category}_TRIVIA_URL')
    response = requests.get(category_trivia_url)
    if response.status_code == requests.codes.ok:
        quiz_questions = response.json()
        return quiz_questions
    else:
        error_message = f'API request failed: {response.status_code}'
        return error_message
