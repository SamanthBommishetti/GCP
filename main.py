import functions_framework
import base64
import json
from google.cloud import bigquery
from datetime import datetime

bq_client = bigquery.Client()

@functions_framework.cloud_event
def pubsubtobigquery(cloud_event):
    message = cloud_event.data.get("message")

    if not message or "data" not in message:
        print("❌ No Pub/Sub message data")
        return

    payload = base64.b64decode(message["data"]).decode("utf-8")
    print("📩 RAW PAYLOAD:", payload)

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        print("❌ Invalid JSON:", payload)
        raise e

    row = {
        "event": data.get("event"),
        "user": data.get("user"),
        "ts": datetime.utcnow().isoformat()
    }

    table_id = "samproject-481503.user_events_ds_sam.user_events"

    errors = bq_client.insert_rows_json(table_id, [row])
    if errors:
        print("❌ BigQuery insert failed:", errors)
        raise RuntimeError(errors)

    print("✅ BigQuery insert successful:", row)
