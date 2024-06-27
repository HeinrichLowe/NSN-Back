from db.base import Base
from .user import User
from .friend import Friend
from .post import Post
from .post_comment import Post_Comment
from .like import Like
from .share import Share

target_metadata = [Base.metadata]