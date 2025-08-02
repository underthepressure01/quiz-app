from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from flashcard import repo
from flashcard.models import FlashcardTopic, Flashcard
from flashcard.schemas import FlashcardTopicResponseDto, FlashcardResponseDto, FlashcardTopicCreateRequestDto, \
    FlashcardCreateRequestDto


async def get_flashcard_topic_by_id(
        session: AsyncSession,
        topic_id: str,
):
    result = await repo.get_topic_by_id(session, UUID(topic_id))
    return map_topic_to_topic_response_dto(result)

async def get_all_flashcard_topics(
        session: AsyncSession,
):
    result = await repo.get_all_topics(session)
    return [map_topic_to_topic_response_dto(t) for t in result]

async def create_flashcard_topic(
        session: AsyncSession,
        request: FlashcardTopicCreateRequestDto,
) -> FlashcardTopicResponseDto:

    topic = FlashcardTopic(name=request.topic_name)

    result = await repo.create_topic(session, topic)
    return map_topic_to_topic_response_dto(result)

async def delete_flashcard_topic_by_id(
        session: AsyncSession,
        topic_id: str,
):
    result = await repo.delete_topic_by_id(session, UUID(topic_id))
    return result

async def get_flashcards_by_topic_id(
        session: AsyncSession,
        topic_id: str,
):
    result = await repo.get_flashcards_by_topic_id(session, UUID(topic_id))
    return [map_flashcard_to_flashcard_response_dto(t) for t in result]

async def get_flashcard_by_id(
        session: AsyncSession,
        flashcard_id: str,
) -> FlashcardResponseDto:
    result = await repo.get_flashcard_by_id(session, UUID(flashcard_id))
    return map_flashcard_to_flashcard_response_dto(result)

async def create_flashcard(
        session: AsyncSession,
        request: FlashcardCreateRequestDto,
) -> FlashcardResponseDto:
    result = await repo.create_flashcard(session, Flashcard(question=request.question, answer=request.answer, topic_id=request.topic_id))
    return map_flashcard_to_flashcard_response_dto(result)

async def delete_flashcard_by_id(
        session: AsyncSession,
        flashcard_id: str,
) -> bool:
    result = await repo.delete_flashcard_by_id(session, UUID(flashcard_id))
    return result

def map_flashcard_to_flashcard_response_dto(flashcard: Flashcard) -> FlashcardResponseDto:
    return FlashcardResponseDto(
        id=str(flashcard.id),
        question=flashcard.question,
        answer=flashcard.answer,
        topic_id=str(flashcard.topic_id),
    )

def map_topic_to_topic_response_dto(topic: FlashcardTopic) -> FlashcardTopicResponseDto:
    return FlashcardTopicResponseDto(topic_id=str(topic.id), topic_name=topic.name)
