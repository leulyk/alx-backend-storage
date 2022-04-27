#!/usr/bin/env python3

"""
   A Python module that provides some stats about Nginx logs stored in MongoDB:

"""

from pymongo import MongoClient


def log_stats(logs):
    """
        Method that provides stats about Nginx logs:
            - Database: logs
            - Collection: nginx
            - Display (same as the example):
            - First line: x logs where x is the number of documents in this
              collection
            - Second line: Methods:
            - 5 lines with the number of documents with the
              method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
            - One line with the number of documents with:
                - Method=GET
                - Path=/status
    """
    print('{} logs'.format(logs.count_documents({})))
    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        log_matches = logs.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, log_matches))
    print("{} status check".format(
        logs.count_documents({'method': 'GET', 'path': '/status'})))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.dump.nginx
    log_stats(logs)
