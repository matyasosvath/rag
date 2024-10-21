import json
import os
import time

from datasets import load_dataset
from elasticsearch import Elasticsearch

__doc__ = """upload first 10.000 documents to Elasticsearch"""

# recommendation: automate script or create separate pipeline/service given the use case and update frequency, data load etc...

INDEX_NAME= "wikipedia"
LIMIT = 1_000
INDEX_MAPPING_PATH = "wikipedia.mapping.json"


def create_connection() -> Elasticsearch:

    port = os.getenv("PORT", "9234")
    host = os.getenv("PORT", "localhost")
    user_name = os.getenv("ES_USERNAME", "elastic")
    password = os.getenv("ES_USERNAME", "elasticpass")
    # api key and cert usage is recommended instead

    es = Elasticsearch(f"https://{host}:{port}", basic_auth=(user_name, password), verify_certs=False)

    return es


def create_index(es_client: Elasticsearch, index_name: str, index_path: str) -> None:

    with open(index_path, "r") as f:
        mapping_contents = json.load(f)
        print(f"File is loaded from {index_path}")

    if not mapping_contents:
        raise RuntimeError("Mapping is None!")

    es_client.indices.create(index=index_name, body=mapping_contents)


def main() -> None:

    es_client = create_connection()

    create_index(es_client, INDEX_NAME, INDEX_MAPPING_PATH)

    start_time = time.time()

    data = load_dataset(INDEX_NAME, "20220301.en") # 6.458.670 document

    n = len(data["train"])

    for i, page in enumerate(data["train"]):

        if i == LIMIT:
            break

        es_client.create(index=INDEX_NAME, document=page, id=page["id"])
        # bulk import is recommended

        print(f"Processed {n}/{i + 1} pages")
        print(f"Processed pages in {time.time() - start_time} seconds")


if __name__ == "__main__":
    # to the reviewer, if anything goes wrong, you can reset
    # curl --insecure -u elastic:elasticpass  -X DELETE https://localhost:9234/wikipedia

    main()