"""from sqlalchemy import select, insert, delete
from models.migrations import *
from controllers import *

class LikeCommand:
    
    def like(conn, user_id, post_id, comment_id):
        with conn.begin() as cur:
            try:
                comment = select(Post_Comment).where(Post_Comment.post_id == post_id, Post_Comment.id == comment_id)
                cur.execute(comment).one

                if comment:
                    data = {"post_id" : post_id, "author_id" : user_id}
                    sql = insert(Like).values(data)
                    cur.execute(sql)
            except:
                raise Exception()
            
    def dislike(conn, user_id, post_id, comment_id):
        with conn.begin() as cur:
            try:
                comment = select(Post_Comment).where(Post_Comment.post_id == post_id, Post_Comment.id == comment_id)
                if comment:
                    sql = delete(Like).where(Like.author_id == user_id, Like.post_id == post_id)
                    cur.execute(sql)
            except:
                raise Exception()"""