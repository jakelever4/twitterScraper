# Written by Jake Lever 24/03/2021
import requests
from datetime import datetime
import rfc3339
import time

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAM2zMgEAAAAAjIFbBetAWCuAzaEL%2B5jSMyofgKE%3DwCGeSfjOYu91nXq0LJiygBheEegg7mU5dhecl2jD2IJIPiwbQI'
search_url = "https://api.twitter.com/2/tweets/search/all"


class Tweet:
    def __init__(self, tweet_id, text, date, author_id):
        self.full_text = text
        self.date = date
        self.tweet_id = tweet_id
        self.author_id = author_id

    def __str__(self):
        return 'TWEET: \n Text: {} \n Date: {} \n ID: {}'.format(self.full_text, self.date, self.tweet_id)


def create_headers(token):
    headers = {"Authorization": "Bearer {}".format(token)}
    return headers


def connect_to_endpoint(url, headers, query_params):
    response = requests.request("GET", url, headers=headers, params=query_params)
    # print(response.status_code)
    status_code = response.status_code

    if status_code == 429:
        while status_code == 429:
            print('429 exception: too many requests. Waiting 10 secs')
            time.sleep(10)
            response = requests.request("GET", url, headers=headers, params=query_params)
            status_code = response.status_code
            print(status_code)

    elif status_code != 200:
        print('ERROR: Status code {}, reason {}: \n {}'.format(response.status_code, response.reason, response.text))
        # raise Exception(response.status_code, response.text)
        return None

    return response.json()


def get_rfc33339_date(date):
    return rfc3339.rfc3339(date)


def remove_special_chars(text):
    text = text.replace('&', 'and')
    text = text.replace('?', '')
    return text


def get_tweets(start_date, end_date, query):
    query = remove_special_chars(query)
    res, next_token = full_archive_search(query, start_date, end_date, next_token=None)
    all_results = [res]

    if res is None:
        print('No Tweets found for query: {}, {}: {}'.format(query, start_date, end_date))
        return None

    while next_token is not None:
        res, next_token = full_archive_search(query, start_date, end_date, next_token=next_token)
        all_results.append(res)

    tweets = []
    for result_list in all_results:
        for tweet in result_list['data']:
            try:
                date = tweet['created_at'][:10]
                # date = datetime.strptime(tweet['created_at'], "%Y-%m-%dT%H:%M:%S.%z")

                tweet_o = Tweet(tweet['id'], tweet['text'], date, tweet['author_id'])
                tweets.append(tweet_o)
            except KeyError:
                print('Cannot find fields for tweet {}.'.format(tweet['id']))

    return tweets


def full_archive_search(query, sd, ed, next_token):
    now = datetime.now()
    try:
        start_date = get_rfc33339_date(datetime.strptime(sd, '%d/%m/%Y'))
        end_date = get_rfc33339_date(datetime.strptime(ed, '%d/%m/%Y'))
        if datetime.strptime(sd, '%d/%m/%Y') > now or datetime.strptime(ed, '%d/%m/%Y') > now or \
                datetime.strptime(ed, '%d/%m/%Y') < datetime.strptime(sd, '%d/%m/%Y'):
            print('invalid date format')
            return None, None
    except:
        print('could not convert dates for archive search')
        return None, None

    headers = create_headers(BEARER_TOKEN)
    query = '(' + query + ')' + ' lang:en -is:retweet'
    query_params = {'query': query, 'start_time': start_date, 'end_time': end_date,
                    'tweet.fields': 'author_id,context_annotations,created_at,entities,geo,id,text',
                    'user.fields': 'description', 'next_token':next_token, 'max_results': 500}
    json_response = connect_to_endpoint(search_url, headers, query_params)
    if json_response is None:
        return None, None

    next_token = None
    try:
        next_token = json_response['meta']['next_token']
        print('next token found')

    except (KeyError, TypeError):
        print('no next token found')

    # print(json.dumps(json_response, indent=4, sort_keys=True))
    return json_response, next_token

