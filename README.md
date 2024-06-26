![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Firebase Badge](https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&logoColor=000&style=for-the-badge)

# Message In A Bottle

A simple Python app that allows users to send and receive messages stored in a Firestore database. The application features a GUI built with Tkinter.

## Features

- **Send Messages**: Users can send a message using the text entry field and send button.
- **Random Messages**: Users receive a random message from the database when they submit a message of their own.
- **Timestamps**: Each message is timestamped when submitted.

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