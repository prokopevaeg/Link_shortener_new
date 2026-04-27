from typing import Protocol, Optional

from nlp.domain.entities import User


class UserRepositoryInterface(Protocol):
    async def get_by_email(self, email: str) -> Optional[User]: ...
