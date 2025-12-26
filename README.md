# GCP Training – Day 1 to Day 10

## Overview of Work Completed During Training

This README documents the hands-on learning and practical work completed during a **10-day Google Cloud Platform (GCP) training program**. The training covered core GCP services including Compute, Networking, Storage, Databases, Messaging, Data Integration, and Command Line operations, with real-time labs and implementations.

---

## Training Modules & Topics Covered

### 1. Compute

* Compute Infrastructure (Regions & Zones)
* Virtual Machines (Compute Engine)
* SSH Keys & OS Login
* Identity Platform (Customer Identity)
* VM Images & Instance Templates
* Shared Image Families
* RAID Configuration with Persistent Disks
* Startup Scripts & Metadata
* Load Balancing & Health Checks
* Managed Instance Groups & Autoscaling
* Cloud Monitoring & Logging
* Alerting Policies
* App Engine / Cloud Run Monitoring

---

### 2. Networking

* VPC Networking Basics
* External (Public) IP Addresses
* Network Interfaces (NICs)
* VPC Firewall Rules
* Network Tags & Service Accounts
* VPC Flow Logs
* Bastion Host & IAP TCP Forwarding
* VPC Routes & Cloud Router (BGP)

---

### 3. Storage

* Cloud Storage (Object Storage)
* Persistent Disk & Hyperdisk (Block Storage)
* Pub/Sub & Firestore (Queue & Table Storage)
* Cloud Tasks
* Storage Buckets & IAM
* Filestore (Managed NFS)
* Partner Storage Services
* Disk Access Control
* Disk Encryption with CMEK
* Cloud Storage Browser & gsutil

---

### 4. Database (Firestore & NoSQL)

* SQL vs NoSQL Concepts
* Introduction to Firestore
* Running Firestore
* Benefits & Use Cases of Firestore
* Serverless Integration (Cloud Functions & Cloud Run)
* Firestore Integration with GCP Services
* Why Firestore for Serverless Applications
* Managed Bigtable / Cassandra Overview
* Drawbacks of Firestore

---

### 5. GCP Service Mapping & Data Integration

* Cloud Data Integration Overview
* Importance of Data Integration in GCP
* Dataplex (Crawler & Metadata Discovery)
* Data Copy & Ingestion (Data Fusion & Dataflow)
* Creating Control Flow & Data Flow
* Scheduling Pipelines using Cloud Scheduler
* Pipeline Monitoring (Cloud Monitoring & Logging)
* Integration with GCP Data Services

---

### 6. Relational Database Service (Cloud SQL)

* Relational Database Concepts
* Relational Databases in GCP
* Setting Up Cloud SQL
* MySQL / PostgreSQL Interfaces
* DB Instances, Storage & Monitoring
* Event Notifications
* Database Access Control
* MySQL Features
* Creating Databases
* Connecting to Database
* Export & Import Operations

---

### 7. Messaging in GCP

* Messaging Concepts & Benefits
* Messaging Options (Pub/Sub, Cloud Tasks, Eventarc)
* Messaging Service Design
* Pub/Sub Basics
* Eventarc Overview
* Streaming with Pub/Sub & Dataflow
* Real-Time Messaging
* Publishers & Subscribers
* Using Pub/Sub
* Benefits & Features
* Queue vs Pub/Sub
* Message Attributes & Filtering
* Raw Message Delivery
* System-to-System Messaging

---

## Command Line Operations (gcloud)

### Authentication & Configuration

```bash
gcloud auth login
gcloud config set project mazenet-001
gcloud config set compute/region asia-south1
```

### Enabling Required Services

```bash
gcloud services enable pubsub.googleapis.com
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable eventarc.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable bigquery.googleapis.com
```

---

## Cloud SQL – Practical Commands

```bash
cloud-sql-proxy.x64.exe mazenet-001:asia-south1:sainathdb --port 3307
mysql -h 127.0.0.1 -P 3307 -u kalyan-0508 -p
USE Managment_system;
```

---

## Pub/Sub – Practical Commands

```bash
gcloud pubsub topics create kalyan-events
gcloud pubsub topics list
gcloud pubsub subscriptions create kalyan-events-sub --topic=kalyan-events
```

---

## BigQuery – Practical Commands

```bash
bq mk --dataset kalyanevents
bq mk --dataset --location=asia-south1 kalyanevents
bq ls
bq mk --table sainathevents.user_events event:STRING,user:STRING,ts:TIMESTAMP
bq ls kalyanevents
```

---

## Cloud Functions – Deployment

```bash
gcloud functions deploy kalyan \
--gen2 \
--region=asia-south1 \
--runtime=python310 \
--source=. \
--entry-point=on_user_create \
--trigger-event-filters="type=google.cloud.firestore.document.v1.created" \
--trigger-event-filters="database=sainath" \
--trigger-event-filters-path-pattern="document=users/{docId}"
```

This function triggers automatically whenever a new document is created in the Firestore `users` collection.

---

## Conclusion

This 10-day GCP training provided strong practical exposure to core cloud concepts, hands-on service configuration, real-time messaging, database integration, and serverless application development. The training helped build a solid foundation for working with production-ready cloud architectures on Google Cloud Platform.
