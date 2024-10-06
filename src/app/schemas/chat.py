from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field




class Chat(BaseModel):
    text: Annotated[str, Field(min_length=1, max_length=63206, examples=["This is the content of my post."])]

class Query(BaseModel):
    prompt: str
    model: str = "llama3"