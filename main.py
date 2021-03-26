# Written by Jake Lever 24/03/2021
import twitter
import csv


with open('query_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        if len(row) == 4:
            index, query, start_date, end_date = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()
            tweets = twitter.get_tweets(start_date, end_date, query)
            if tweets is not None:
                for tweet in tweets:
                    print(tweet)
        else:
            print('Error reading CSV row {}: Contains incorrect number of columns ({})'.format(index, len(row)))
    print('Queries searched successfully. Tweets stored in output folder.')




# query = 'Johnson & Johnson'
# tweets = twitter.get_tweets('2019-09-10', '2019-11-25', query)
#
# if tweets is not None:
#     print('{} tweets found for query '.format(len(tweets)))
#     for tweet in tweets:
#         print(tweet)

# print(twitter.full_archive_search(query, '2019-09-10', '2019-09-25', None))
