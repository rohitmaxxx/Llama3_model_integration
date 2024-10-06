from typing import Annotated, Any

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from ...api.dependencies import get_current_user
from ...core.db.database import async_get_db
from ...core.exceptions.http_exceptions import ForbiddenException, NotFoundException
from ...core.utils.cache import cache
from ...crud.crud_posts import crud_posts
from ...crud.crud_users import crud_users
from ...schemas.post import PostCreate, PostCreateInternal, PostRead, PostUpdate
from ...schemas.user import UserRead
from ...schemas.chat import Chat, Query
from ...api.dependencies import get_current_user

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import requests

router = APIRouter(tags=["chat"])


TEMPLATE = """
Answer the below question.

Here is the conversation history: {context}

Question: {question}
"""


@router.post("/chat", response_model=Chat, status_code=201)
async def chat(
    current_user: Annotated[UserRead, Depends(get_current_user)],
    query: Query,
) -> Chat:
    try:
        # model = OllamaLLM(model="llama3", host="http://host.docker.internal:11434/api/generate")
        # prompt = ChatPromptTemplate.from_template(TEMPLATE)
        
        # chain = prompt | model
        # data = chain.invoke({"context": "", "question": body.text})
        data = {
                "prompt": query.prompt,
                "model": query.model
                }
        result = requests.post("http://host.docker.internal:8001/chat", json=data)
        if result.status_code == 200:  # Ensure the request was successful
            response_data = result.json()
            data['text'] = response_data['answer']
        print("==================== data ", data)
        return data
    except Exception as e:
        return {"text": str(e)}