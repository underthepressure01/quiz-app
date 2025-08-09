from typing import List
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.flashcard.models import FlashcardTopic, Flashcard


async def get_topic_by_id(session: AsyncSession, topic_id) -> FlashcardTopic:
    result = await session.execute(select(FlashcardTopic).where(FlashcardTopic.id == topic_id))

    return result.scalar_one_or_none()

async def get_all_topics(session: AsyncSession) -> List[FlashcardTopic]:
    result = await session.execute(select(FlashcardTopic))

    return list(result.scalars().all())


async def create_topic(session: AsyncSession, topic: FlashcardTopic) -> FlashcardTopic:
    session.add(topic)
    await session.commit()
    await session.refresh(topic)

    return topic

async def delete_topic(session: AsyncSession, topic: FlashcardTopic)-> bool:
    await session.delete(topic)
    await session.commit()

    return True

async def delete_topic_by_id(session: AsyncSession, topic_id) -> bool:
    await session.execute(delete(FlashcardTopic).where(FlashcardTopic.id == topic_id))
    await session.commit()

    return True

async def get_flashcard_by_id(session: AsyncSession, flashcard_id: UUID) -> Flashcard:
    result = await session.execute(select(Flashcard).where(Flashcard.id == flashcard_id))

    return result.scalar_one_or_none()

async def get_flashcards_by_topic_id(session: AsyncSession, flashcard_topic_id: UUID) -> List[Flashcard]:
    result = await session.execute(select(Flashcard).where(Flashcard.topic_id == flashcard_topic_id))

    return list(result.scalars().all())

async def create_flashcard(session: AsyncSession, flashcard: Flashcard) -> Flashcard:
    session.add(flashcard)
    await session.commit()
    await session.refresh(flashcard)

    return flashcard

async def delete_flashcard_by_id(session: AsyncSession, flashcard_id: UUID) -> bool:
    await session.execute(delete(Flashcard).where(Flashcard.id == flashcard_id))
    await session.commit()

    return True