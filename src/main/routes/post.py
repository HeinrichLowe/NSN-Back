from fastapi import APIRouter, Depends, Request, HTTPException, status
"""from controllers import posts
from db import *"""

router = APIRouter()

@router.post("/<user_logged>/new-post")
def new_post(user_logged):
    conn = router.config["conn"]
    data = Request.json
    try:
        PostCommand.new_post(conn, user_logged, data)
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return {"message" : "Post created successfully."}, 201

@router.get("/<user_logged>/find-post")
def find_post(user_logged):
    conn = router.config["conn"]
    try:
        posts = PostCommand.find_post(conn, user_logged)
        return_posts = []
        for post in posts:
            return_posts.append({"title" : post.title, "content" : post.content, "created_at" : post.created_at, "updated_at" : post.updated_at})
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return return_posts, 201

@router.put("/<user_logged>/<post>/edit-post")
def edit_post(user_logged, post):
    conn = router.config["conn"]
    data = Request.json
    try:
        PostCommand.edit_post(conn, user_logged, post, data)
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return {"message" : "Post edited successfully."}

@router.delete("/<user_logged>/<post>/delete-post")
def delete_post(user_logged, post):
    conn = router.config["conn"]
    try:
        PostCommand.soft_delete_post(conn, user_logged, post)
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return {"message" : "Post deleted successfully."}, 201

@router.post("/<user>/<post>/share")
def share_post(user, post):
    conn = router.config["conn"]
    try:
        ShareCommand.share_post(conn, user, post)
    except ShareException as err:
        return {"message" : f"{err}"}, 400
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return {"message" : "Post shared successfully."}, 201

@router.put("/<user>/<share>/unshare")
def share_delete(user, share):
    conn = router.config["conn"]
    try:
        ShareCommand.soft_delete_share(conn, user, share)
    except ShareException as err:
        return {"message" : f"{err}"}, 400
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return {"message" : "Post unshared successfully."}, 201

@router.post("/<user_logged>/<post>/comment-post")
def comment(user_logged, post):
    conn = router.config["conn"]
    data = Request.json
    try:
        CommentCommand.comment(conn, user_logged, post, data)
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return {"message" : "Comment successfully made."}, 201

@router.get("/<user_logged>/<post>/comments")
def comments(user_logged, post):
    conn = router.config["conn"]
    try:
        comments = CommentCommand.comments(conn, user_logged, post)
        return_comments = []
        for comment in comments:
            return_comments.append({"content" : comment.content, "created_at" : comment.created_at, "updated_at" : comment.updated_at})
    except Exception as err:
        return {"message" : f"{err}"}, 500
    return return_comments, 201

@router.put("/<user_logged>/<post>/<comment>/comment-edit")
def comment_edit(user_logged, post, comment):
    conn = router.config["conn"]
    data = Request.json
    try:
        CommentCommand.comment_edit(conn, user_logged, post, comment, data)
    except Exception as err:
        return {"message" : f"{err}"}, 500
    return {"message" : "Comment successfully edited."}, 201

@router.delete("/<user_logged>/<post>/<comment>/comment-delete")
def comment_delete(user_logged, post, comment):
    conn = router.config["conn"]
    try:
        CommentCommand.soft_delete_comment(conn, user_logged, post, comment)
    except Exception as err:
        return {"message" : f"{err}"}, 500
    return {"message" : "Comment successfully deleted."}, 201

@router.post("/<user>/<post>/<comment>/like")
def like(user, post, comment):
    conn = router.config["conn"]
    try:
        LikeCommand.like(conn, user, post, comment)
    except LikeException as err:
        return {"message" : f"{err}"}, 400
    except Exception as err:
        return {"message" : f"{err}"}, 500
    return {"message" : "Like"}, 201

@router.post("/<user>/<post>/<comment>/dislike")
def dislike(user, post, comment):
    conn = router.config["conn"]
    try:
        LikeCommand.dislike(conn, user, post, comment)
    except LikeException as err:
        return {"message" : f"{err}"}, 400
    except Exception as err:
        return {"message" : f"{err}"}, 500
    return {"message" : "Dislike"}, 201