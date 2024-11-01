from passlib.hash import pbkdf2_sha256
from src.domain.protocols.cryptography import IHashComparer

Sha = pbkdf2_sha256

class PasslibHashHandler(IHashComparer):
    def compare(self, income_password: str, stored_password: str) -> bool:
        return Sha.verify(income_password, stored_password)
