from google.cloud import firestore

# Connect to named Firestore database
db = firestore.Client(database="preethidb")

# ---------------- CREATE ----------------
doc_ref = db.collection("users").add({
    "name": "John Doe",
    "email": "john@example.com",
    "role": "Developer",
    "exp": 5
})

doc_id = doc_ref[1].id
print(f"Created user with ID: {doc_id}")

# ---------------- READ ----------------
print("\nUsers with exp >= 5:")
query = db.collection("users").where("exp", ">=", 5)

for doc in query.stream():
    print(doc.id, "=>", doc.to_dict())

# ---------------- UPDATE ----------------
db.collection("users").document(doc_id).update({
    "exp": 6
})
print(f"\nUpdated user {doc_id} exp to 6")

# ---------------- DELETE ----------------
delete_query = db.collection("users").where("name", "==", "John Doe")

for doc in delete_query.stream():
    db.collection("users").document(doc.id).delete()
    print(f"Deleted user {doc.id}")