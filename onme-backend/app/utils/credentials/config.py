import os

# Get the Firebase Service Account Key Path from environment variables
FIREBASE_SERVICE_ACCOUNT_KEY = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY", "credentials/serviceAccountKey.json")
