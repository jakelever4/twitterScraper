**Twitter Scraper** 

- The input for the script is query_list.csv. You can edit/swap out this document for your own queries
- The query_list.csv must be in the following format: each line is an individual search. Each line must have these 3 entries in this order, separated by commas:
- query: a line of text up to 512 characters long
    - If the query has commas, then it MUST be in double quotes "".
    - If the query has special characters ?,! etc, these will be removed
- Start Date: the earliest date you want to receive results for, in the format YYYY-MM-DD e.g. 2016-09-01
- End Date: the latest date you want to receive results for, in the format YYYY-MM-DD e.g. 2016-09-10
    - Neither start nor end date can be in the future

- The query, start date and end date must be on the same line, separated by commas
- see the example csv for reference.
- run main.py to run search queries on the data


SETUP
- Before you start you need to do the following:
    - Twitter API token: Tokens are a type of authorization for an App to gain specific access to data. They let Twitter know who you are.
    - Go to https://developer.twitter.com/en/docs/developer-portal/overview and register for an account
    - Once you have been accepted for an account, go to the developer portal (https://developer.twitter.com/en/portal/dashboard). Create/go to your project -> App Settings -> Keys and Tokens -> Bearer Token and click the button that says regenerate. This will copy your bearer token.
    - Once you have copied your bearer token, open the file twitter.py and replace the variable on line 6 called BEARER_TOKEN = your copied value.
    - For smaller analysis (<= 1,000,000 Tweets), I can supply bearer tokens.
    