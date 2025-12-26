import functions_framework
import json
 
@functions_framework.cloud_event
def on_user_create(cloud_event):
    """
    Cloud Functions Gen 2
    Triggered when a Firestore document is CREATED
    Database: preethidb
    Collection: users
    """
 
    # Raw Firestore event payload
    data = cloud_event.data or {}
 
    # Firestore document data
    value = data.get("value", {})
    fields = value.get("fields", {})
 
    def get_string(field):
        return fields.get(field, {}).get("stringValue")
 
    def get_int(field):
        val = fields.get(field, {}).get("integerValue")
        return int(val) if val is not None else None
 
    # Extract fields safely
    name = get_string("name")
    roll_no= get_string("roll_no")
    branch= get_string("branch")
    group= get_string("group")
    email = get_string("email")
    role = get_string("role")
    exp = get_int("exp")
 
    # Structured logs (best practice)
    print("FIRESTORE CREATE EVENT RECEIVED ")
    print(json.dumps({
        "document": value.get("name"),
        "name": name,
        "email": email,
        "roll_no": roll_no,
        "branch": branch,
        "group": group,
        "role": role,
        "exp": exp
    }, indent=2))
 
    # Optional: business logic placeholder
    if exp is not None and exp < 0:
        print(" Invalid experience value detected")
 
    print(" Function execution completed successfully")


# import functions_framework
 
# @functions_framework.cloud_event
# def on_user_create(event):
#     data = event.data
#     # triggered when a doc is created in firestore
#     value = data.get('value', {})
#     fields = value.get('fields', {})
 
#     name = fields.get('name', {}).get("stringValue")
#     email = fields.get('email', {}).get("stringValue")
#     exp = fields.get('exp', {}).get("integerValue")
#     role = fields.get('role', {}).get("stringValue")
 
#     print("New Firestore document created:")
#     print(f"Name: {name}")
#     print(f"Email: {email}")
#     print(f"Exp: {exp}")
#     print(f"Role: {role}")