from abc import ABC, abstractmethod
from typing import Dict

class ITokenGenerator(ABC):
    """Interface for token generation and verification.
    
    Implementations of this interface should:
    1. Keep the logic for generating tokens (access and refresh) as private methods
    2. Implement the generation of both tokens (access and refresh)
    3. Ensure that generated tokens follow the JWT standard
    
    Recommended implementation example:
    ```python
    class ConcreteTokenGenerator(ITokenGenerator):
        def __init__(self):
            # necessary configurations
            
        async def __generate_access_token(self, user_data: Dict) -> Dict:
            # private logic for access token
            
        async def __generate_refresh_token(self, user_data: Dict) -> Dict:
            # private logic for refresh token
            
        async def create_tokens(self, user_data: Dict) -> Dict:
            # uses private methods to generate tokens
            
        async def verify_token(self, token: str) -> Dict:
            # verification logic
    ```
    """

    @abstractmethod
    async def verify_token(self, token: str) -> Dict:
        """Verifies the validity of a token."""

    @abstractmethod
    async def create_tokens(self, user_data: Dict) -> Dict:
        """Creates access_token and refresh_token for the user.
        
        This implementation should use separate private methods
        for generating each type of token."""
