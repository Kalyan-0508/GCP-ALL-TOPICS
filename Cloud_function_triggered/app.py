def on_file_upload(event, context):
    file_name = event["name"]
    bucket = event["bucket"]
    size = event.get("size", "unknown")

    print("New file uploaded")
    print(f"Bucket: {bucket}")
    print(f"File: {file_name}")
    print(f"Size: {size}")


    