from crawl_index import crawl_index
from connect_elastic import ElasticSearch

if __name__ == '__main__':
    file_list = crawl_index()
    elastic_search = ElasticSearch()
    elastic_search.insert_data(file_list)