import os
from typing import List, Optional

from elasticsearch import Elasticsearch
from src import typing


def retrieve_context(
    input: typing.Question,
    index_name: str = "wikipedia",
    top_k: int = 3,
    similarity: Optional[str] = "bm25"
) -> str:

    es_client = create_connection()

    print(f"ES: {es_client}")

    documents = search(es_client, input.text, index_name, similarity)

    return " ".join(doc for doc in documents[:top_k])


def create_connection() -> Elasticsearch:

    user_name = os.getenv("ELASTIC_USERNAME", "elastic")
    password = os.getenv("ELASTIC_PASSWORD", "elasticpass")
    host = os.getenv("ES_HOST", "es01")
    ca_cert = "./ca.crt"
    # api key and cert usage is recommended instead

    es_client = Elasticsearch(f"https://{host}:9200", ca_certs=ca_cert, basic_auth=(user_name, password))

    return es_client


def search(
    es_client: Elasticsearch,
    input: str,
    index_name:str,
    similarity: Optional[str] = None
) -> List[str]:

    """
    curl --insecure -u elastic:elasticpass -X GET https://localhost:9234/wikipedia/_search -H 'Content-Type: application/json' -d '{  "query": {    "match": { "text": "hello"}  }}'
    """

    query = {
        "query": {
            "match_all": {}
        }
    }

    response = es_client.search(index=index_name, body=query)

    results = [hit['_source']['text'] for hit in response['hits']['hits']]

    # suggestion: audit logs

    return results