from google.cloud import firestore

# Connect to Firestore
db = firestore.Client(database="samdb")

write_result, doc_ref = db.collection("users").add({
    "name": "John Doe",
    "email": "john@example.com",
    "role": "Developer",
    "exp": 5
})

doc_id = doc_ref.id
print(f"Created user with ID: {doc_id}")

print("\nUsers with exp >= 10")
for doc in db.collection("users").where("exp", ">=", 10).stream():
    print(f"{doc.id} => {doc.to_dict()}")

db.collection("users").document(doc_id).update({
    "exp": 6
})
print(f"\nUpdated user {doc_id} exp to 6")

updated_doc = db.collection("users").document(doc_id).get()
print("After update:", updated_doc.to_dict())

db.collection("users").document(doc_id).delete()
print(f"\nDeleted user {doc_id}")
