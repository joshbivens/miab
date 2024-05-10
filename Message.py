# BivensFinalProject
# Programmer: Joshua Bivens
# Email: jbivens1@cnm.edu
# Purpose: Send messages to a database, retrieve messages from a database
# Python version: 3.11.2

from Firebase import db
from datetime import datetime
import random

class Message:
    db = db

    def __init__(self, user_input):
        self.user_input = user_input
        self.doc_ref = self.db.collection("messages").document()

    def post_to_firestore(self):
        if self.user_input is None:
            print("No input retrieved.")
            return

        try:
            timestamp = self.get_timestamp()
            self.doc_ref.set({
                "message": self.user_input,
                "timestamp": timestamp
            })
        except Exception as e:
            print("Error posting to Firestore: ", e)

    @staticmethod
    def get_timestamp():
        now = datetime.now()
        timestamp = now.strftime("%B %d, %Y - %I:%M%p")
        return timestamp

    @classmethod
    def get_random_message(cls):
        # Get all documents in the "messages" collection
        docs = cls.db.collection("messages").get()

        # If there are no documents, return None
        if not docs:
            return None

        # Generate a random index
        random_index = random.randint(0, len(docs) - 1)

        # Get the document at the random index
        random_doc = docs[random_index]

        # Set random message and timestamp
        message = random_doc.to_dict().get("message")
        timestamp = random_doc.to_dict().get("timestamp")

        # Remove the selected document from the docs list
        # to prevent repeats
        del docs[random_index]

        # Return as a tuple
        return message, timestamp
