# pyLamb_duh
Repo for Python Lambda 

## speakersBot.py
This Lambda Function is scheduled by Cloudwatch Rule and when run will **query** the Twitter API for tweets that contain either "call for speakers" OR "submit your talk" and filter out and **retweeted** tweets.  It will then check for technical keywords in the tweet like 'redhat', 'red hat', 'kubernetes', 'ansible', 'tech', 'hacker', 'opensource', 'data science', 'pipeline', 'sysops', 'devops', 'automation' to hopefully keep the tweets related to technical space.

Then the function will retweet the tweet to twitter. My hope is to help spread awareness for the need for speakers and papers for technical conferences and summits.  