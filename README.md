# Subreddit Simulator Simulator Bot

[YouTube](https://www.youtube.com/channel/UCot_LXrqq_INixycJJVkE8Q)

The bot can be used on [this](https://www.reddit.com/user/GetterBot12345/comments/900e81/simulating_subreddits/) Reddit thread.

To generate a post, comment the name of a subreddit with our without the r/.
eg.

`r/wellthatsucks`
`wellthatsucks`

The bot should respond unless you commented a subreddit that doesn't exist, has too few posts to generate a new post off of, or the server is not running for whatever reason.  

If you want to run the bot for yourself, follow the instructions below.

1. Make sure you have PRAW downloaded.  If you don't open a terminal and `pip install praw` to get the latest version.
1. Create a new Reddit account.  This isn't exactly necessary, but I would advise running it on a main account
1. Replace the credentials starting on line 8 with `r = praw...` with your valid account details.  To get the correct details, you will need to create a new script under the apps section on your Reddit account.  This can be found in the user preferences.
  1. The client id is the 13 character long string found on the overview of your script eg. `xxxxx-xxxxxxxx`.
  1. The client secret is the first thing listed after clicking edit on your script.
  1. The user agent is a string that is sent to the reddit api as a sort of identification.  Something like "A bot that generates fake posts" or something of the sort should be sufficient.  
  1. The username and password are the username and password of your reddit account.
1. replace the string passed to `r.submission()` on line 57 with the post you want to run the bot on.  You can find a posts id in the URL of any post.  It is the string that appears after the `/comments/`.  For example, the post id of `https://www.reddit.com/user/GetterBot12345/comments/900e81/simulating_subreddits/` is `900e81`.

After you have followed all of the steps, run the Python script and comment some subreddits on the post you are running the bot on.   
