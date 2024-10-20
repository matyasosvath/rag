from datasets import load_dataset
from elasticsearch import Elasticsearch


__doc__ = """upload documents to Elasticsearch"""

# recommendation: automate script or create separate pipeline/service given the use case and update frequency, data load etc...



data = load_dataset("wikipedia", "20220301.en") # 6458670 document


for datum in data["train"]:
    print(datum)
    break

