from enum import Enum
from pydantic import BaseModel


class Question(BaseModel):
    text: str
    # ...

class Models(Enum):
    pass

class RagModels(Models):
    t5_base = "t5-base"
    # ...
