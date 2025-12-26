import functions_framework
import base64
import json

@functions_framework.cloud_event
def con_pubsub(cloud_event):
    msg = cloud_event.data.get("message", {})

    # get base64 data safely
    encoded_data = msg.get("data")

    if not encoded_data:
        print("No data received in Pub/Sub message")
        return

    # decode base64
    data = base64.b64decode(encoded_data).decode("utf-8")

    print("PUB/SUB MESSAGE RECEIVED")
    print("Raw data:", data)

    # parse JSON safely
    try:
        print(json.loads(data))
    except json.JSONDecodeError:
        print("Data is not valid JSON")
