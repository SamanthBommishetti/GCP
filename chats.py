from google.cloud import firestore
from datetime import datetime

db = firestore.Client()

messages = [
    ("alice@gmail.com", "bob@gmail.com", "Hi Bob"),
    ("bob@gmail.com", "alice@gmail.com", "Hi Alice"),
    ("alice@gmail.com", "bob@gmail.com", "How are you?"),
    ("bob@gmail.com", "alice@gmail.com", "I'm good"),
    ("alice@gmail.com", "bob@gmail.com", "Any updates?"),
    ("bob@gmail.com", "alice@gmail.com", "Working on it"),
    ("alice@gmail.com", "bob@gmail.com", "Great"),
    ("bob@gmail.com", "alice@gmail.com", "Will update soon"),
    ("alice@gmail.com", "bob@gmail.com", "Thanks"),
    ("bob@gmail.com", "alice@gmail.com", "No problem")
]

for s, r, m in messages:
    db.collection("chats").add({
        "sender": s,
        "receiver": r,
        "message": m,
        "timestamp": datetime.utcnow()
    })
