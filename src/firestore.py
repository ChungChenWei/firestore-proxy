import base64

import firebase_admin
from firebase_admin import credentials, firestore
from jose import jwt

cred = credentials.Certificate("credential.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection("token")


def update_token(access_token):
    jwt_token = base64.b64decode(access_token)
    payload = jwt.decode(jwt_token, key=None, options={"verify_signature": False})
    device_id = payload["device_id"]
    collection.document(str(device_id)).set({"access_token": access_token})


def fetch_token(device_id):
    doc = collection.document(str(device_id)).get()
    return doc.to_dict()["access_token"]
