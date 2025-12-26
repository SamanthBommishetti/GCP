from google.cloud import firestore
from datetime import datetime, timedelta
import random

# Initialize Firestore
db = firestore.Client()
collection_ref = db.collection("user_activity_logs")

# Wide variety of values
users = [f"U{1000+i}" for i in range(50)]  # 50 users

activities = [
    "product_click",
    "view_page",
    "add_to_cart",
    "remove_from_cart",
    "wishlist_add",
    "search",
    "checkout_start"
]

products = [
    "iphone15", "samsung_s24", "macbook_air", "dell_xps",
    "airpods_pro", "sony_headphones", "ipad_pro", "pixel_8",
    "oneplus_12", "boat_earbuds", "nike_shoes", "adidas_shoes",
    "apple_watch", "fitbit_charge", "canon_dslr"
]

categories = [
    "electronics", "mobiles", "laptops", "accessories",
    "fashion", "fitness", "cameras"
]

devices = ["mobile", "desktop", "tablet"]

# Firestore batch (max 500 per batch)
batch = db.batch()
batch_size = 0

start_time = datetime.utcnow() - timedelta(days=1)

for i in range(1000):
    doc_ref = collection_ref.document()

    product = random.choice(products)

    data = {
        "user_id": random.choice(users),
        "activity_type": random.choice(activities),
        "category": random.choice(categories),
        "product": product,
        "page": f"/product/{product}",
        "device": random.choice(devices),
        "timestamp": start_time + timedelta(seconds=i * random.randint(1, 5))
    }

    batch.set(doc_ref, data)
    batch_size += 1

    # Commit every 500 writes
    if batch_size == 500:
        batch.commit()
        batch = db.batch()
        batch_size = 0

# Commit remaining writes
if batch_size > 0:
    batch.commit()

print("✅ Successfully inserted 1000 diverse user activity records")
