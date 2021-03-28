**Twitter Scraper** 

REQUIREMENTS
- Python 3

OVERVIEW
- The input for the script is query_list.csv. You edit/swap out this document for your own queries 
- It must still be called query_list.csv.
- You must keep the first line (headers).
- The query_list.csv must be in the following format: each line is an individual search. Each line must have these 4 entries, separated by commas, in this order:
    - NAME: query name/index. The output filename depends on this value. It should be unique and not contain weird characters. This should be something like a row/query number, or a unique identifier for that query, e.g. a query about Boris Johnson may be indexed boris_johnson .
    - QUERY: a line of text up to 512 characters long. This is what will be searched for by the Twitter API
        - Queries should be in double quotes "". They MUST be in double quotes if the query contains commas.
        - It is also worth noting that if the query has special characters ?,! etc, these will be removed and replaced where possible (e.g. Johnson & Johnson -> Johnson and Johnson). 
    - START_DATE: the earliest date you want to receive results for, in the format DD/MM/YYYY e.g. 01/09/2016
    - END_DATE: the latest date you want to receive results for, in the format DD/MM/YYYY e.g. 09/09/2016
        - Neither start nor end date can be in the future and the end date must be after the start date.
- The output for this script is in the folder called 'output'. 
- Each row (query) from query_list.csv will get it's own output file, named INDEX_tweets.csv , where INDEX is the index value from the row explained above.


INSTRUCTIONS
- Download this project: This can be done by clicking the green 'Code' button in the top right of this repo. Download the project as a zip and unzip once downloaded.
- Get a Twitter API token: Tokens are a type of authorization for an App to gain specific access to data. They let Twitter know who you are.
  - Go to https://developer.twitter.com/en/docs/developer-portal/overview and register for a developer account.
  - Once you have been accepted for an account, go to the developer portal (https://developer.twitter.com/en/portal/dashboard). Create/go to your project -> App Settings -> Keys and Tokens -> Bearer Token and click the button that says regenerate. This will copy your bearer token.
  - Once you have copied your bearer token, open the file twitter.py and replace the variable on the line (line 7) which says BEARER_TOKEN = "YOUR TOKEN HERE". It must be in 'quotation marks'.
  - For smaller analysis (<= 1,000,000 Tweets), I may be able to supply bearer tokens.
- Install external libraries: I tried to write this using as little libs as possible but you still need some. Open the terminal/command line and type the following commands:
    - 'pip3 install requests'
    - 'pip3 install rcf3339'
- In the project there are 3 (other) files and a folder:
    - main.py : this is the file you need to run to run the program
    - twitter.py : you need to open this file with a text editor and input your Twitter Bearer token 
    - query_list.csv : This is where you input your queries. There are some examples already in the file which you should delete. Queries must be in the format in the example file. The filename MUST stay the same (query_list.csv)
    - output folder : This is where the tweets will be stored. There is one .csv file for each query (row) in query_list.csv. The filenames correspond to the index field in query_list.csv.
- Prepare your queries: make sure the CSV query_list is in the correct format with your own queries in.
- Run main.py :
  - open the terminal/command line app and change directory to the project. If the project is in your downloads folder, then just type the following command: 'cd downloads/twitterScraper-master'
  - enter the command 'python main.py'
  - The program should start running and logging tweet collection. At the end there will be a message to say if the run is successful.
- Tweets for the queries should be in the output folder.
    
    