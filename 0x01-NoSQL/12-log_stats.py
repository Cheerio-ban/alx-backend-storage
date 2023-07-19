#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

def get_logs():
    """Gets logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    # get number of documents in collection
    docs_num = nginx_logs.count_documents({})
    get_num = nginx_logs.count_documents({'method': 'GET'})
    post_num = nginx_logs.count_documents({'method': 'POST'})
    put_num = nginx_logs.count_documents({'method': 'PUT'})
    patch_num = nginx_logs.count_documents({'method': 'PATCH'})
    delete_num = nginx_logs.count_documents({'method': 'DELETE'})
    get_status = nginx_logs.count_documents({'method': 'GET',
                                             'path': '/status'})
    print("{} logs".format(docs_num))
    print("Methods:")
    print("    method GET: {}".format(get_num))
    print("    method POST: {}".format(post_num))
    print("    method PUT: {}".format(put_num))
    print("    method PATCH: {}".format(patch_num))
    print("    method DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))


if __name__ == "__main__":
    get_logs()
