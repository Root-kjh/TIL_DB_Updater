# Settings

# REPO
REPO_URL = "https://github.com/Root-kjh/til"
REPO_DIR = "/git/til"

#DB
DB_CONNECTION = {
    "server": "localhost",
    "port": 9200
}
DB_INDEX = "til"

INDEX_MAPPING = {
    "mappings": {
        "properties": {
            "context": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "path": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            }
        }
    }
}