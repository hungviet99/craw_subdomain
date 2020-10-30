import json, requests
from elasticsearch import Elasticsearch
import craw_domain 

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es = Elasticsearch()

def search_by_index_and_id(_id):
    """Lấy ra database trong elasticsearch
    """
    res = es.get(
        index="subdomain",
        id=_id
        )
    return res

def insert_db_elastic(domain, data):
    """Ghi dữ liệu vào Elasticsearch
    """
    res = es.index(
        index="subdomain",
        id=domain,
        body=data
        )
    return res

def update_db_elastic(_id, update_data):
    """Update dữ liệu vào elasticsearch
    """
    res = es.update(
        index="subdomain",
        id=_id,
        body=update_data
    )
    return res

def main(mydomain, sub_all):
    try:
        """Nếu có dữ liệu thì update dữ liệu mới
        """
        res = search_by_index_and_id(mydomain)
        update_data = {
            "doc": sub_all
        }
        update_db_elastic(mydomain, update_data)
    except:
        """Nếu không có dữ liệu thì ghi dữ liệu vào db
        """
        insert_db_elastic(mydomain, sub_all)
    return 