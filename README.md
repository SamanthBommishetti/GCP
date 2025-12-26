# Synopsis of  Topics

# Compute

Understood GCP global infrastructure: Regions and Zones

Created and managed Virtual Machines (Compute Engine)

Configured SSH keys, OS Login, startup scripts, and metadata

Worked with custom images, instance templates, and shared image families

Implemented Managed Instance Groups (MIGs) with autoscaling

Configured load balancing and health checks

Monitored applications using Cloud Monitoring and Logging

Created alerting policies for VM health and performance

Observed monitoring for App Engine and Cloud Run

# Networking

Learned VPC networking fundamentals

Configured external/public IPs and network interfaces

Implemented VPC firewall rules using network tags and service accounts

Enabled and analyzed VPC Flow Logs

Accessed private resources using Bastion host and IAP TCP forwarding

Worked with VPC routes and Cloud Router (BGP concepts)

# Storage

Used Cloud Storage for object storage and IAM-based access control

Worked with Persistent Disks and Hyperdisk for block storage

Understood Pub/Sub and Firestore as queue and table storage

Implemented Cloud Tasks for asynchronous execution

Configured disk encryption using CMEK

Explored Filestore (managed NFS) and partner storage services

Managed storage access using IAM and gsutil

Database – Firestore & NoSQL

Compared SQL vs NoSQL databases

Learned Firestore architecture, benefits, and limitations

Created and ran Firestore in Native mode

Integrated Firestore with Cloud Functions and Cloud Run

Understood why Firestore is ideal for serverless applications

Explored Bigtable and Cassandra use cases

Identified Firestore drawbacks (cost, complex queries)

# Cloud SQL (RDS)

Learned relational database fundamentals in GCP

Set up Cloud SQL (MySQL/PostgreSQL)

Connected securely using Cloud SQL Proxy

Created databases and tables

Managed users, permissions, and monitoring

Performed import/export operations

# Messaging in GCP

Understood messaging concepts and benefits

Worked with Pub/Sub, Cloud Tasks, and Eventarc

Designed publisher–subscriber architectures

Compared queue-based vs event-based messaging

Used message attributes and filtering

Implemented real-time messaging pipelines

Integrated Pub/Sub with Dataflow for streaming concepts

# GCP Data Integration & Mapping

Learned importance of data integration in GCP

Explored Dataplex for metadata discovery

Used Data Fusion and Dataflow for ingestion

Created control flows and data flows

Scheduled pipelines using Cloud Scheduler

Monitored pipelines with Cloud Monitoring and Logging

#Integrated pipelines with BigQuery and other GCP services

# Command-Line Tools Used

Authenticated and configured projects using gcloud

Enabled required APIs (Pub/Sub, Cloud Functions, Eventarc, Cloud Run, BigQuery)

Managed datasets and tables using BigQuery CLI

#Created Pub/Sub topics and subscriptions

Deployed 2nd-gen Cloud Functions

Connected to Cloud SQL using Cloud SQL Proxy

Pub/Sub → Cloud Functions → BigQuery (End-to-End Pipeline)
Implementation Summary

# Created a Pub/Sub topic and subscription for user events

Published JSON messages containing user activity data

# Deployed a Cloud Function triggered by Pub/Sub messages

Decoded and processed messages inside the function

Inserted processed data into a BigQuery table in real time

End-to-End Flow

Events are published to Pub/Sub

Pub/Sub triggers a Cloud Function

The function processes and enriches the data

Final records are stored in BigQuery for analytics


# SYNOPSIS ON PUB SUB
Google Cloud Pub/Sub – Fully managed, real-time pub/sub messaging for asynchronous communication.
Architecture
•	Publishers → Topics (message storage) → Subscriptions → Subscribers (pull/push delivery).
•	Control Plane (routers assign clients); Data Plane (forwarders handle traffic with replication across clusters/disks).
•	Message Flow: Publish → Persist (N clusters, M disks) → Ack publisher → Deliver to subscribers → Ack/delete.
Core Components List
•	Topics: Message feeds with optional schemas.
•	Subscriptions: Pull (fetch) or push (webhook) endpoints.
•	Messages: Payload + attributes; lifecycle (unacked → redeliver → dead- letter).
Key Features Table

Feature	Benefit
At-least-once delivery	Reliable with retries
Global scalability	Millions msg/sec, low latency
Dead-letter queues	Handles failures gracefully
Integrations	Eventarc, Dataflow, BigQuery
Use Cases & Demo
•	Event streaming (GCS events via Event arc), IoT, analytics.
•	Quick Setup: gcloud pubsub topics create my-topic; gcloud pubsub subscriptions create my-sub --topic=my-topic.




# COMMANDS TO EXECUTE  pubsub
gcloud services enable pubsub.googleapis.com


gcloud services list --enabled | grep pubsub


gcloud pubsub topics create user-events


gcloud pubsub topics list

gcloud pubsub subscriptions create user-event-sub --topic=user-events

gcloud pubsub subscriptions list

gcloud pubsub topics publish user-events --message='{"event": "User_Created", "user": "Samanth"}'

gcloud pubsub subscriptions pull user-event-sub --limit=5 --auto-ack





