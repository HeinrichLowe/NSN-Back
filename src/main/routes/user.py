# pylint: disable = broad-exception-caught

# Third-party imports
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

# Local imports
from src.errors.error_handler import handle_errors
from src.main.adapters.request_adapter import request_adapter

# Composers
from src.main.composers.user import (
    signup_composer,
    signin_composer,
    search_by_name_composer,
    get_basic_user_info_composer,
    verify_token_composer
)

# Schemas
from src.presentation.schemas.user_schemas import (
    SignupRequest,
    SignupResponse,
    SigninRequest,
    SigninResponse,
    SearchByNameRequest,
    SearchByNameResponse,
    UserResponse
)

router = APIRouter()

@router.get('/ping')
def ping():
    return 'pong: its works'

@router.post('/signup')
async def signup(request: Request) -> SignupResponse:
    http_response = None
    try:
        http_response = await request_adapter(request, signup_composer(), SignupRequest)
    except Exception as err:
        http_response = handle_errors(err)
    return JSONResponse(http_response.body, http_response.status_code)

@router.post('/signin')
async def signin(request: Request) -> SigninResponse:
    http_response = None
    try:
        http_response = await request_adapter(request, signin_composer(), SigninRequest)
    except Exception as err:
        http_response = handle_errors(err)
    return JSONResponse(http_response.body, http_response.status_code)

@router.get('/search-by-name')
async def search_by_name(request: Request) -> SearchByNameResponse:
    http_response = None
    try:
        http_response = await request_adapter(request, search_by_name_composer(), SearchByNameRequest)
    except Exception as err:
        http_response = handle_errors(err)
    return JSONResponse(http_response.body, http_response.status_code)

@router.get('/user')
async def user(request: Request) -> UserResponse:
    try:
        http_response = await request_adapter(request, verify_token_composer())
        user_info = await get_basic_user_info_composer().handle(http_response.body["sub"])
    except Exception as err:
        http_response = handle_errors(err)
        return JSONResponse(http_response.body, http_response.status_code)
    return JSONResponse(user_info.body, user_info.status_code)

"""@router.get('/refresh-token')
async def refreshToken(refresh_token: Depends = Depends(UserCtrl.verify_token), db_session = DependsConnection) -> UserResponse:
    id = refresh_token['sub']['user_id']
    user = await UserCtrl.refresh_token(db_session, id)

    return JSONResponse(
        content= user,
        status_code=status.HTTP_200_OK
    )

@router.put("/{user_logged}/change-password")
def change_password(user_logged:int, conn = Depends(Connection.db_session)):
    data = Request.json
    print(type(user_logged))
    try:
        user = UserCommand.search_by_id(conn, user_logged)
        UserCommand.update_inf(conn, user, data)
    except SearchByIDException as err:
        print(err)
        return {"message": f"{err}"}, 400
    except Exception as err:
        print(err)
        return {"message": f"{err}"}, 500
    return {"Message" : "Password Changed Successfully!"}, 201

@router.get("/<user_logged>/my-profile")
def my_profile(user_logged):
    conn = router.config["conn"]
    try:
        profile = UserCommand.my_profile(conn, user_logged)
        return_profile = []
        for rprofile in profile:
            return_profile.append({"Full Name:" : rprofile.full_name, "Username:" : rprofile.username, "Email:" : rprofile.email, "Birthday:" : rprofile.birthday, "Member since: " : rprofile.created_at})
    except Exception as err:
        print(err)
        return {"message" : f"{err}"}, 500
    return return_profile, 201

@router.get("/users/<name>")
def find_users(name):
    conn = router.config["conn"]
    try:
        users = UserCommand.find_user(conn, name)
        return_users = []
        for user in users:
            return_users.append({"id" : user.id, "full_name" : user.full_name})
    except Exception as err:
        return {"message": f"{err}"}, 500
    return return_users, 201

@router.post("/<user_logged>/add-friend")
def add_friend(user_logged):
    conn = router.config["conn"]
    data = Request.json
    user = {"user_id" : f"{UserCommand.search_by_id(conn, user_logged).id}"}
    try:
        UserCommand.add_friend(conn, user, data)
    except AddFriendException as err:
        return{"message" : f"{err}"}, 400
    except Exception as err:
        return {"message": f"{err}"}, 500
    return {"message" : "Congratulations, you are friends now!"}, 201

@router.delete("/<user_logged>/delete-account")
def delete_user_account(user_logged):
    conn = router.config["conn"]
    try:
        user = UserCommand.search_by_id(conn, user_logged)
        UserCommand.soft_delete_user(conn, user)
    except Exception as err:
        return {"message": f"{err}"}, 500
    return {"message" : "Account deleted successfully!"}, 201

@router.delete("/<user_logged>/<friend_id>/delete-friend")
def delete_friend(user_logged, friend_id):
    conn = router.config["conn"]
    try:
        user = UserCommand.search_by_id(conn, user_logged)
        friend = UserCommand.search_by_id(conn, friend_id)
        UserCommand.delete_friend(conn, user, friend)
    except Exception as err:
        return {"message": f"{err}"}, 500
    return {"message" : "Successfully broken friendship!"}, 201

@router.get("/<user_logged>/friends-list")
def friends_list(user_logged):
    conn = router.config["conn"]
    try:
        friends_list = []
        user = UserCommand.search_by_id(conn, user_logged)        
        friends_id = UserCommand.friends_select(conn, user)
        for friend in friends_id:
            friends_list.append({"full_name" : friend.full_name, "id" : friend.id})
    except Exception as err:
        print(err)
    return friends_list, 201"""