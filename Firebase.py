# BivensFinalProject
# Programmer: Joshua Bivens
# Email: jbivens1@cnm.edu
# Purpose: Firebase connection
# Python version: 3.11.2

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()