import elasticsearch

from src import typing


STRATEGIES = {
    "top_k": {"name": "top_k", "k": 10, "similarity": "cosine"},
    # ...
    # suggestion: add more strategy
}


def retrieve_context(input: typing.Question, strategy: str = "top_k") -> str:

    if strategy not in STRATEGIES:
        raise ValueError(f"Strategy unrecognised! Got {strategy}")

    selected_strategy = STRATEGIES[strategy]



    return ""