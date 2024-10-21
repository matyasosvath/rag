from enum import Enum
from pydantic import BaseModel


class Question(BaseModel):
    text: str
    # ...

class Models(Enum):
    pass

class RagModels(Models):
    gpt2_small = "gpt2-small"
    # ...
