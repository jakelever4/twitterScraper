**Twitter Scraper** 

OVERVIEW
- The input for the script is query_list.csv. You can edit/swap out this document for your own queries 
    - It must still be called query_list.csv.
    - You must keep the first line (headers).
- The query_list.csv must be in the following format: each line is an individual search. Each line must have these 4 entries, separated by commas, in this order:
- Index: query index. Should just be row/query number.
- query: a line of text up to 512 characters long
    - Queries should be in double quotes "". They MUST be if the query contains commas.
    - If the query has special characters ?,! etc, these will be removed
- Start Date: the earliest date you want to receive results for, in the format YYYY-MM-DD e.g. 2016-09-01
- End Date: the latest date you want to receive results for, in the format YYYY-MM-DD e.g. 2016-09-10
    - Neither start nor end date can be in the future

- The index, query, start date and end date must be on the same line, separated by commas.
- see the example csv for reference.
- run main.py to run search queries on the data


SETUP
- Before you start you need to do the following:
    - Get a Twitter API token: Tokens are a type of authorization for an App to gain specific access to data. They let Twitter know who you are.
      - Go to https://developer.twitter.com/en/docs/developer-portal/overview and register for an account
      - Once you have been accepted for an account, go to the developer portal (https://developer.twitter.com/en/portal/dashboard). Create/go to your project -> App Settings -> Keys and Tokens -> Bearer Token and click the button that says regenerate. This will copy your bearer token.
      - Once you have copied your bearer token, open the file twitter.py and replace the variable on line 7 called BEARER_TOKEN = your copied value.
      - For smaller analysis (<= 1,000,000 Tweets), I can supply bearer tokens.
    - Download this project: This can be done by cloning the Git repository or clicking the green 'Code' button in the top right.
    - Prepare your queries: make sure the CSV query_list is in the correct format with your own queries in.
    
    