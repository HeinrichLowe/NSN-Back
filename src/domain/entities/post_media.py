from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from enum import Enum

class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"

@dataclass
class PostMedia:
    id: UUID | None = None
    post_id: UUID | None = None
    media_type: MediaType | None = None
    url: str | None = None
    thumbnail_url: str | None = None
    position: int | None = None
    content_type: str | None = None  # MIME type (image/jpeg, video/mp4, etc)
    width: int | None = None
    height: int | None = None
    duration: int | None = None  # for videos (in seconds)
    size: int | None = None  # size in bytes
    created_at: datetime | None = None
