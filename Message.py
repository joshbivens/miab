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
        # Get count of records
        messages_ref = cls.db.collection("messages")
        total_count = len(messages_ref.get())

        if total_count == 0:
            return None
        
        # Make random idex
        random_index = random.randint(0, total_count - 1)

        # Get random record
        random_message_query = messages_ref.order_by(u"timestamp").limit(1).offset(random_index)
        random_message_doc = random_message_query.get()

        if not random_message_doc:
            return None
        
        # Set message data
        random_message_data = random_message_doc[0].to_dict()
        message = random_message_data.get("message")
        timestamp = random_message_data.get("timestamp")

        # Return tuple
        return message, timestamp

