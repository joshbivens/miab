# Programmer: Josh Bivens
# Email: thejoshbivens@gmail.com
# Purpose:
#   A service class for interacting with Firestore.


from Firebase import db
from datetime import datetime
import random

class FirestoreService:
    @staticmethod
    def post_message(message):
        doc_ref = db.collection("messages").document()
        timestamp = FirestoreService.get_timestamp()
        try:
            doc_ref.set({
                "message": message,
                "timestamp": timestamp
            })
        except Exception as e:
            print("Error posting to Firestore: ", e)

    @staticmethod
    def get_random_message():
        messages_ref = db.collection("messages")
        total_count = len(messages_ref.get())

        if total_count == 0:
            return None
        
        random_index = random.randint(0, total_count - 1)

        random_message_query = messages_ref.order_by(u"timestamp").limit(1).offset(random_index)
        random_message_doc = random_message_query.get()

        if not random_message_doc:
            return None
        
        random_message_data = random_message_doc[0].to_dict()
        message = random_message_data.get("message")
        timestamp = random_message_data.get("timestamp")

        return message, timestamp

    @staticmethod
    def get_timestamp():
        now = datetime.now()
        timestamp = now.strftime("%B %d, %Y - %I:%M%p")
        return timestamp