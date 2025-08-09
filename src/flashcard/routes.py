from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_session
from src.flashcard import service
from src.flashcard.schemas import FlashcardTopicCreateRequestDto, FlashcardTopicResponseDto, FlashcardResponseDto, \
    FlashcardCreateRequestDto

flashcard_router = APIRouter()

@flashcard_router.get("/flashcards/topic", response_model=List[FlashcardTopicResponseDto], tags=["Flashcard Topic"])
async def get_flashcards_topic(session: AsyncSession = Depends(get_session)):
    return await service.get_all_flashcard_topics(session)

@flashcard_router.get("/flashcards/topic/{topic_id}", response_model=FlashcardTopicResponseDto, tags=["Flashcard Topic"])
async def get_flashcard_topic_by_id(topic_id: str, session: AsyncSession = Depends(get_session)) -> FlashcardTopicResponseDto:
    return await service.get_flashcard_topic_by_id(session, topic_id)

@flashcard_router.post("/flashcards/topic", tags=["Flashcard Topic"])
async def create_flashcard_topic(request: FlashcardTopicCreateRequestDto, session=Depends(get_session)):
    return await service.create_flashcard_topic(session, request)

@flashcard_router.delete("/flashcards/topic", tags=["Flashcard Topic"])
async def delete_flashcard_topic_by_id(topic_id: str, session=Depends(get_session)):
    return await service.delete_flashcard_topic_by_id(session, topic_id)

@flashcard_router.get("/flashcards/by-topic", response_model=List[FlashcardResponseDto], tags=["Flashcard"])
async def get_flashcards_by_topic_id(topic_id: str,session: AsyncSession = Depends(get_session)):
    return await service.get_flashcards_by_topic_id(session, topic_id)

@flashcard_router.get("/flashcards/by-id", response_model=FlashcardResponseDto, tags=["Flashcard"])
async def get_flashcard_by_id(flashcard_id: str, session: AsyncSession = Depends(get_session)):
    return await service.get_flashcard_by_id(session, flashcard_id)

@flashcard_router.post("/flashcards", response_model=FlashcardResponseDto, tags=["Flashcard"])
async def create_flashcard(request: FlashcardCreateRequestDto, session=Depends(get_session)):
    return await service.create_flashcard(session, request)

@flashcard_router.delete("/flashcards", tags=["Flashcard"])
async def delete_flashcard(flashcard_id: str, session=Depends(get_session)):
    return await service.delete_flashcard_by_id(session, flashcard_id)
