import praw
import details
import markovify
from time import sleep

details = details.Details()

r = praw.Reddit(client_id = details.client_id,
                         client_secret = details.client_secret,
                         user_agent = details.user_agent,
                         username = details.username,
                         password = details.password)


def getNewPosts(subreddit):
    sub = r.subreddit(subreddit)
    try:
        cache = open('cache/' + sub.display_name + '.json', 'r').read().split('\n')
        print('read')
    except:
        cache = []
        print('new')
    new = []
    try:
        for post in sub.new(limit = 500):
            if post.title not in cache:
                new.append(post.title)
    except:
        None
    with open('cache/' + sub.display_name + '.json', 'a+') as file:
        file.write(''.join([i if ord(i) < 128 else ' ' for i in '\n'.join(new)]))

def genPost(subreddit):
    sub = r.subreddit(subreddit)
    # getNewPosts(subreddit)
    text = open('cache/' + sub.display_name + '.json').read()
    model = markovify.Text(text)
    return model.make_sentence()

def getNoCache(subreddit):
    sub = r.subreddit(subreddit)
    temp = ''
    for post in sub.new(limit = 250):
        temp += post.title + ' '
    return temp

def genNoCache(subreddit):
    model = markovify.Text(getNoCache(subreddit))
    return model.make_sentence()


cache = []

print('started')

while 1:
    post = r.submission('900e81')
    for comment in post.comments:
        if comment.id not in cache:
            try:
                body = comment.body
                req = body.replace('r/', '').split()
                print(req[0])
                comment.reply(genNoCache(req[0]))
                cache.append(comment.id)
            except:
                None
    sleep(10)
