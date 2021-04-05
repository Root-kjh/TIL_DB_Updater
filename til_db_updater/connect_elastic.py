from elasticsearch import Elasticsearch
from settings import DB_CONNECTION, DB_INDEX, INDEX_MAPPING

class ElasticSearch():
    def __init__(self):
        self.es = Elasticsearch([DB_CONNECTION])
        self.es.indices.delete(index=DB_INDEX, ignore=[400, 404])
        self.es.indices.create(index = DB_INDEX, body=INDEX_MAPPING)
    def insert_data(self, file_list):
        for file in file_list:
            file_name = file[0]
            file_path = file[1]
            file_context = file[2]
            doc={
                "name": file_name,
                "path": file_path,
                "context": file_context
            }
            self.es.index(index=DB_INDEX, doc_type="_doc", body=doc)