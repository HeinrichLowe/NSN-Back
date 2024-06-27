from fastapi import status

class UserDuplicatedException(Exception):
    pass 


class UserNotFound(Exception):
    pass