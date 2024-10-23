"""from sqlalchemy import select, insert, update, func
from src.infra.db.models import User, Friend, Like, Post, Post_Comment, Share


class CommentCommand:
    def comment(conn, user_id, post_id, data):
        with conn.begin() as cur:
            try:
                user = cur.execute(select(User).where(User.id == user_id)).fetchone()
                if not user:
                    raise Exception()
                
                post = cur.execute(select(Post).where(Post.id == post_id, Post.deleted_at == None)).fetchone()
                if not post:
                    raise Exception()

                data.update({"post_id" : f"{post.id}", "author_id" : f"{user.id}"})
                sql = insert(Post_Comment).values(data)
                cur.execute(sql)

            except Exception as err:
                raise err

    def comments(conn, user_id, post_id):
        with conn.begin() as cur:
            try:
                user = cur.execute(select(User).where(User.id == user_id, User.deleted_at == None)).fetchone()
                if not user:
                    raise Exception()
                
                post = cur.execute(select(Post).where(Post.id == post_id, Post.author_id == user.id, Post.deleted_at == None)).fetchone()
                if not post:
                    raise Exception()
                
                sql = cur.execute(select(Post_Comment).\
                    where(Post_Comment.post_id == post.id, Post_Comment.deleted_at == None).\
                    order_by(Post_Comment.created_at.desc())).all()
                
                if sql == []:
                    raise Exception()

                return sql

            except Exception as err:
                raise err

    def comment_edit(conn, user_id, post_id, comment_id, data):
        with conn.begin() as cur:
            try:
                user = cur.execute(select(User).where(User.id == user_id)).fetchone()
                if not user:
                    raise Exception()
                
                post = cur.execute(select(Post).where(Post.id == post_id, Post.deleted_at == None)).fetchone()
                if not post:
                    raise Exception()
                
                comment = cur.execute(select(Post_Comment).where(Post_Comment.id == comment_id, Post_Comment.post_id == post.id, Post_Comment.author_id == user.id, Post_Comment.deleted_at == None)).fetchone()
                if not comment:
                    raise Exception()
                
                data.update({"updated_at" : f"{func.now()}"})
                sql = update(Post_Comment).values(data).where(Post_Comment.id == comment.id, Post_Comment.post_id == post.id, Post_Comment.author_id == user.id, Post_Comment.deleted_at == None)
                cur.execute(sql)
                
            except Exception as err:
                raise err
            
    def soft_delete_comment(conn, user_id, post_id, comment_id):
        with conn.begin() as cur:
            try:
                user = cur.execute(select(User).where(User.id == user_id)).fetchone()
                if not user:
                    raise Exception()
                
                post = cur.execute(select(Post).where(Post.id == post_id, Post.deleted_at == None)).fetchone()
                if not post:
                    raise Exception()
                
                comment = cur.execute(select(Post_Comment).where(Post_Comment.id == comment_id, Post_Comment.author_id == user.id, Post_Comment.deleted_at == None)).fetchone()
                if not comment:
                    raise Exception()
                
                sql = update(Post_Comment).values(deleted_at=func.now()).where(Post_Comment.id == comment.id, Post_Comment.post_id == post.id, Post_Comment.author_id == user.id, Post_Comment.deleted_at == None)
                cur.execute(sql)

            except Exception as err:
                raise err
            
    def comment_verify(conn, post, comment_id):
            with conn.begin() as cur:
                comment = cur.execute(select(Post_Comment).where(Post_Comment.id == comment_id, Post_Comment.post_id == post.id, Post_Comment.deleted_at == None)).fetchone()
                if not comment:
                    raise Exception()
                return comment"""