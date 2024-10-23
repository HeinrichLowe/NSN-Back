"""from sqlalchemy import select, insert, update, delete, func
from models import *

class PostCommand:
    def new_post(conn, user_id, post):
        with conn.begin() as cur:
            try:
                post.update({"author_id" : user_id})
                sql = insert(Posts).values(post)
                cur.execute(sql)
            except Exception as err:
                print(err)
                raise
            
    def find_post(conn, user_id):
        with conn.begin() as cur:
            try:
                sql = cur.execute(select(Posts).
                                  where(Posts.author_id==user_id, Posts.deleted_at==None).
                                  order_by(Posts.created_at.desc())).all()
                if sql == []:
                    raise FindPostException()
                else:
                    return sql
                
            except Exception as err:
                print(err)

    def edit_post(conn, user_id, post_id, data):
        with conn.begin() as cur:
            try:
                user = cur.execute(select(Users).where(Users.id == user_id)).fetchone()
                
                if not user:
                    raise InvalidUserException()
                
                post = cur.execute(select(Posts).where(Posts.id == post_id, Posts.author_id == user.id, Posts.deleted_at == None)).fetchone()
                    
                if not post:
                    raise PostNotFoundException()
                
                data.update({"updated_at" : func.now()})
                sql = update(Posts).values(data).where(Posts.id == post_id)
                cur.execute(sql)

            except Exception as err:
                print(err)
                raise err

    def soft_delete_post(conn, user_id, post_id):
        with conn.begin() as cur:
            try:
                user = cur.execute(select(Users).where(Users.id == user_id)).fetchone()

                if not user:
                    raise InvalidUserException()

                post = cur.execute(select(Posts).where(Posts.id == post_id).where(Posts.author_id == user.id).where(Posts.deleted_at == None)).fetchone()

                if not post:
                    raise PostNotFoundException()

                sql = update(Posts).values(deleted_at=func.now()).where(Users.id == user.id, Posts.id == post.id)
                cur.execute(sql)

            except Exception as err:
                print(err)
                raise err
            
    def post_verify(conn, post_id):
        with conn.begin() as cur:
            post = cur.execute(select(Posts).where(Posts.id == post_id).where(Posts.deleted_at == None)).fetchone()
            if not post:
                raise PostNotFoundException()
            return post"""