from abc import ABC, abstractmethod
from typing import Dict

class ITokenVerifier(ABC):
    """Interface for token verification.
    
    Implementations of this interface should:
    1. Keep the logic for verifying tokens as private methods
    2. Implement the verification of tokens
    3. Ensure that verified tokens follow the JWT standard
    
    Recommended implementation example:
    ```python
    class ConcreteTokenVerifier(ITokenVerifier):
        def __init__(self):
            # necessary configurations

        async def verify_token(self, token: str) -> Dict:
            # verification logic
    ```
    """

    @abstractmethod
    async def verify_token(self, token: str) -> Dict:
        """Verifies the validity of a token."""
