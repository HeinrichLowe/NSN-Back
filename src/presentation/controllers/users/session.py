import datetime
#from repositories import UserCommand
#from models.user import User

async def session(username, db_session):
    user =  await UserCommand.search_by_username(db_session, User(
        username=username.lower()
    ))

    return {
        'id': user.id.hex,
        'username': user.username,
        'name': user.full_name,
        'avatar': user.avatar,
        'email': user.email,
        'birthday': user.birthday.strftime('%d/%m/%Y')
    }