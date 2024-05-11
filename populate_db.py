# Programmer: Josh Bivens
# Email: thejoshbivens@gmail.com
# Purpose:  
#   Prefills the Firestore with dummy entries. The get_random_timestamp
#   function generates a random timestamp from the last year. A new random
#   timestamp is set to each dummy message's timestamp.
        

from Firebase import db
from datetime import datetime, timedelta
import random

messages = [
    "Winning isn’t everything, but wanting to win is.",
    "I am not a product of my circumstances. I am a product of my decisions.",
    "Every child is an artist.  The problem is how to remain an artist once he grows up.",
    "You can never cross the ocean until you have the courage to lose sight of the shore.",
    "I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
    "Either you run the day, or the day runs you.",
    "Whether you think you can or you think you can’t, you’re right.",
    "The two most important days in your life are the day you are born and the day you find out why.",
    "Whatever you can do, or dream you can, begin it.  Boldness has genius, power and magic in it.",
    "The best revenge is massive success.",
]

# Generate a random timestamp within the past year
def get_random_timestamp():
    now = datetime.now()
    past_year = now - timedelta(days=365)
    random_timestamp = random.uniform(past_year.timestamp(), now.timestamp())
    return datetime.fromtimestamp(random_timestamp).strftime("%B %d, %Y - %I:%M%p")

# Populate Firestore
for i in range(len(messages)):
    message = messages[i]
    timestamp = get_random_timestamp()

    doc_ref = db.collection("messages").document()
    doc_ref.set({
        "message": message,
        "timestamp": timestamp
    })