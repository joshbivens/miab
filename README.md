![](https://img.shields.io/github/downloads/miab/note/total?style=plastic) ![](https://img.shields.io/github/last-commit/miab/note)

# Message In A Bottle

Message In A Bottle is a simple Python application that allows users to send and receive messages stored in a Firestore database. The application features a graphical user interface built with Tkinter.

## Features

- **Send Messages**: Users can send a message using the text entry field and send button.
- **Random Messages**: Users receive a random message from the database when they submit a message of their own.
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

Populate your Firestore database with dummy messages using the `PopulateDB.py` script:
```bash
python populate_db.py
```