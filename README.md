# DataBreachBot

### Goal
The goal of this bot was to create a twitter page that could be a one stop shop for company breach news, faster than the outlets. Ideally it would provide keywords you could follow to keep up with.

### Method
The tools used here were Python, Numpy, Pandas, Seaborn, REGEX and AWS.
This databreach bot was created using Twitter's API. I used REGEX to find stems of words like "breaching", "breached", etc. and summize them into "breach". 
After these tweets were scraped, I wanted to visualize the data using numpy and seaborn. 
The graph you see on these tweets is the culmination of what has been trending and using the keyword stems.


### Infrastructure
The bot was then deployed into an EC2 instance and would trigger automatically using cronjobs. 
I had further plans to tag and attach company names to the tweets to make an actual monitor for company breaches, but I delayed too long and now Twitter's API is no longer free.
