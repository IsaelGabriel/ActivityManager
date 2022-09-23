# Modules
import pyrebase
import streamlit as st
from datetime import datetime

# Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyCV9lkDOWZT8jWne9-uUOZkhsvh6o1wYa4",
    'authDomain' : "activity-manager-1a519.firebaseapp.com",
    'projectId' : "activity-manager-1a519",
    'databaseURL' : "https://console.firebase.google.com/u/1/project/activity-manager-1a519/database/activity-manager-1a519-default-rtdb/data/~2F",
    'storageBucket' : "activity-manager-1a519.appspot.com",
    'messagingSenderId' : "33786015877",
    'appId' : "1:33786015877:web:72f2669f4b9f1f4ec7b9ec",
    'measurementId' : "G-F9DKTNVCJC"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Databases
db = firebase.database()
storage = firebase.storage()