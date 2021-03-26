# Written by Jake Lever 24/03/2021
import twitter
import csv


with open('query_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    i = 1
    for row in reader:
        print(row)
        if len(row) == 3:
            query, start_date, end_date = row[0], row[1], row[2]
            tweets = twitter.get_tweets(start_date, end_date, query)
        else:
            print('Error reading CSV row {}: Contains incorrect number of columns ({})'.format(i, len(row)))
        i += 1




query = 'Johnson & Johnson'
tweets = twitter.get_tweets('2019-09-10', '2019-11-25', query)

if tweets is not None:
    print('{} tweets found for query '.format(len(tweets)))
    for tweet in tweets:
        print(tweet)

# print(twitter.full_archive_search(query, '2019-09-10', '2019-09-25', None))
