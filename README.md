# pyLamb_duh
Repo for Python Lambda 

Then the function will retweet the tweet to twitter. My hope is to help spread awareness for the need for speakers and papers for technical conferences and summits.  

## chucksTwitter.py
This Lambda Function is scheduled by Cloudwatch Rule and when run will hit a fun Chuck Norris API. I added a **chuckagories** list so that others could easily add or remove the catagories that they wanted to be returned by API.  It takes the response and posts it to twitter. 
* this also needs to be updated to work with new longer format.

## urbanLambdaTwitBot.py
This Lambda Function is scheduled by Cloudwatch Rule and when run will scrape urbandictionary for todays word, format it and tweet it.  
* needs to be updated to new longer tweet standards, but it does create a link back to Urban Dictionary in short url in case the definition is too long for twiiter.
