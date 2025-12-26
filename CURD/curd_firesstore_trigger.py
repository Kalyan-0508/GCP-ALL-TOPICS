import functions_framework
 
@functions_framework.cloud_event
def on_user_create(event):
    data = event.data
    # triggered when a doc is created in firestore
    value = data.get('value', {})
    fields = value.get('fields', {})
 
    name = fields.get('name', {}).get("stringValue")
    email = fields.get('email', {}).get("stringValue")
    exp = fields.get('exp', {}).get("integerValue")
    role = fields.get('role', {}).get("stringValue")
 
    print("New Firestore document created:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Exp: {exp}")
    print(f"Role: {role}")

    