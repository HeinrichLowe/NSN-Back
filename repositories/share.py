"""from sqlalchemy import select, insert, update, func
from models import *
from controllers import *


class ShareCommand:

    def share_post(conn, user_id, post_id):
        with conn.begin() as cur:
            try:
                user = UserCommand.user_verify(conn, user_id)
                if not user:
                    raise InvalidUserException
                
                post = PostCommand.post_verify(conn, post_id)
                if not post:
                    raise Exception
                
                data = {"post_id" : post.id, "author_id" : user.id}
                cur.execute(insert(Shares).values(data))
            
            except:
                raise ShareException
            
    def soft_delete_share(conn, user_id, share_id):
        with conn.begin() as cur:
            try:
                user = UserCommand.user_verify(conn, user_id)
                if not user:
                    raise InvalidUserException
                
                sql = update(Shares).values(deleted_at = func.now()).where(Shares.id == share_id, Shares.author_id == user.id, Shares.deleted_at == None)
                cur.execute(sql)

            except:
                raise ShareException
"""

