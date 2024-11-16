import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Firebase credentials path from .env
cred_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")

# Initialize Firebase App
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Firestore utility functions
def save_to_firestore(collection: str, data: dict) -> str:
    """
    Save data to a Firestore collection and return the document ID.
    """
    doc_ref = db.collection(collection).add(data)
    return doc_ref[1].id


def get_document(collection: str, doc_id: str) -> dict:
    """
    Retrieve a document from a Firestore collection by ID.
    """
    doc = db.collection(collection).document(doc_id).get()
    return doc.to_dict() if doc.exists else None


def update_document(collection: str, doc_id: str, updates: dict) -> str:
    """
    Update a Firestore document with the provided data.
    """
    doc_ref = db.collection(collection).document(doc_id)
    doc_ref.update(updates)
    return doc_id
