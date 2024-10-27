from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
import json
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.register_composer import register_composer
from src.main.composers.search_by_name_composer import search_by_name_composer
#import controllers.users as UserCtrl
from src.main.routes.users.schemas import BodySchema
#from db import *

router = APIRouter()

@router.post('/register')
def register():
    http_response = request_adapter(Request, register_composer())
    return JSONResponse(http_response.body, http_response.status_code)

"""@router.post("/signup")
async def signup(input: SignupRequest, db_session = DependsConnection) -> SignupResponse:
    try:
        user_id = await UserCtrl.signup(db_session, input)

        return JSONResponse(
            content=user_id,
            status_code=status.HTTP_201_CREATED
        )
    
    except Exception as e:
        return JSONResponse(
            content={'detail': e.args},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
@router.post("/signin")
async def signin(input: SigninRequest, db_session = DependsConnection) -> SigninResponse:
    try:
        login = await UserCtrl.signin(db_session, input)

        print(login)

        if login == None:
            return JSONResponse(
                content={"msg": "User not exist"},
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        
        if login == False:
            return JSONResponse(
                content={"msg": "Invalid Username or Password"},
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        return JSONResponse(
            content=login,
            status_code=status.HTTP_200_OK
        )
    
    except Exception as e:
        return JSONResponse(
            content={'detail': e.args},
            status_code=status.HTTP_400_BAD_REQUEST
        )"""

@router.get('/ping')
def test():
    return 'pong: its works'

@router.get('/search-by-users')
async def search_by_name(request: Request) -> BodySchema:
    http_response = await request_adapter(request, search_by_name_composer())
    print("\n\nResponse: >>> ", vars(http_response), " <<< \n\nEnd-Response.")
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )

"""@router.get('/user')
async def home(access_token: Depends = Depends(UserCtrl.verify_token), db_session = DependsConnection) -> UserResponse:
    username = access_token['sub']['username']
    user = await UserCtrl.session(username, db_session)

    return JSONResponse(
        content=user,
        status_code=status.HTTP_200_OK
    )

@router.get('/refresh-token')
async def refreshToken(refresh_token: Depends = Depends(UserCtrl.verify_token), db_session = DependsConnection) -> UserResponse:
    id = refresh_token['sub']['user_id']
    user = await UserCtrl.refresh_token(db_session, id)

    return JSONResponse(
        content= user,
        status_code=status.HTTP_200_OK
    )"""

"""@router.post("/signup")
async def signup(input: SignupRequest = Depends(), db_session = DependsConnection) -> SignupResponse:
    try:
        user = await UserCtrl.signup(db_session, input)
        return SignupResponse(id=user.id)
    except UserCtrl.exceptions.UserDuplicatedException as err:
        #log.error("error 2  ")
        JSONResponse(
            {"detail": "User already exists"},
            status_code=status.HTTP_400_BAD_REQUEST
        )
        return JSONResponse(err)
    except Exception as err:
        #log.error(err)
        return JSONResponse({"message": "internal server"}, status_code=500)
        
@router.post("/signin")
async def signin(input: SigninRequest, db_session = DependsConnection):
    try:
        login = await UserCtrl.signin(db_session, input)
        if login:
            return JSONResponse({"message" : "You're successfully logged in."}, status_code=200)
    except UserCtrl.exceptions.UserNotFound:
        return JSONResponse({"message": "Invalid Login or password. Please, check the credentials"}, status_code=401)
    except Exception as err:
        #log.error(err)
        return JSONResponse({"message": "Server error."}, status_code=500)
        
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