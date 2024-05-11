# Message In A Bottle

Message In A Bottle is a simple Python application that allows users to send and receive messages stored in a Firestore database. The application features a graphical user interface built with Tkinter.

## Features

- **Send Messages**: Users can send messages using the provided text entry field and send button.
- **Random Messages**: Users can receive random messages from the database when they submit a message of their own.
- **Receive Messages**: Messages are retrieved from Firestore and displayed in the application's message display area.
- **Timestamps**: Each message is timestamped.

## Installation

To run the Message In A Bottle application locally, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/joshbivens/miab.git
   ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Link your own empty [Firestore](https://firebase.google.com/docs/firestore/quickstart). The app looks for a `serviceAccountKey.json` file.

4. Run the app:
    ```bash
    python main.py
    ```

## Populating Firestore with Dummy Messages

If you'd like to populate your Firestore database with dummy messages for testing purposes, you can use the `PopulateDB.py` script provided in the repository. Follow these steps:

1. Ensure you have the necessary permissions and access to your Firestore database.

2. Run the `PopulateDB.py` script:
   ```bash
   python PopulateDB.py
   ```