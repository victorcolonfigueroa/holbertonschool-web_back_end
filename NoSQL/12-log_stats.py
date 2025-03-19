#!/usr/bin/env python3
"""
        Run the script directly to see the log statistics.
"""
from pydoc import doc
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    doc_logs = collection.count_documents({})
    print(f"{doc_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    stats = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{stats} status check")