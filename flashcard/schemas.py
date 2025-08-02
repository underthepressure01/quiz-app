from pydantic import BaseModel

class FlashcardTopicCreateRequestDto(BaseModel):
    topic_name: str

class FlashcardTopicResponseDto(BaseModel):
    topic_id: str
    topic_name: str

class FlashcardCreateRequestDto(BaseModel):
    topic_id: str
    question: str
    answer: str

class FlashcardResponseDto(BaseModel):
    id: str
    question: str
    answer: str
    topic_id: str