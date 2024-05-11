# Programmer: Josh Bivens
# Email: thejoshbivens@gmail.com
# Purpose:
#   Message class. Serves as a model for managing message data and 
#   provides an interface for interacting with Firestore.


from firestore_service import FirestoreService

class Message:
    def __init__(self, user_input):
        self.user_input = user_input

    def post_to_firestore(self):
        if self.user_input is None:
            print("No input retrieved.")
            return

        FirestoreService.post_message(self.user_input)

    @classmethod
    def get_random_message(cls):
        return FirestoreService.get_random_message()




