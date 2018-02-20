import praw
import pickle
import time
from Structures.Queue import Queue

#initialize reddit instance with proper credentials in praw.ini
reddit = praw.Reddit('summonbot')

#get subreddit
sub = reddit.subreddit('GlobalOffensive')

#command that we will respond to
command = '!fridgegif'

queueFile = 'FridgeQueue.p'
dataFile = 'FridgeData.p'

#Determine if we need to reply to this commment
def valid_comment(comment):
    if(command in comment.body.lower()):
        #unpack data
        queue = pickle.load(open(queueFile, 'rb'))
        #create if empty
        if not queueFile:
            queue = Queue()

        data = pickle.load(open('FridgeData.p', 'rb'))

        #comment already in queue, or already processed
        if(queue.contains(comment.id) or comment.id in [entry[0] for entry in data]):
            return False

        comment.refresh()
        for child in comment.replies:
            if child.author.name == 'summon-bot':
                #this comment has already been replied to, but it passed our
                #queue for some reason. need to store
        return True
    return False
