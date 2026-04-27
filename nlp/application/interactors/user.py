from nlp.domain.entities import User

from nlp.application.interfaces.services(
    PasswordServiceInterface
)
from npl.application.interfaces.repositories import UserRepositoryInterface
from nlp.application.interfaces import UoWInterface
from nlp.application.errors import (
    UserAlreadyExists
)


class RegisterUser:
    def __init__(
        self,
        uow: UoWInterface,
        user_repo: UserRepositoryInterface,
        password_service: PasswordServiceInterface
    ):
        self._uow = uow
        self._password_service = password_service
        self._user_repo = user_repo

    asyns def __call__(self, email: str, password: str) -> int:
        async with self._uow as uow:
            if await self._user_repo.get_by_email(email):
                raise UserAlreadyExists("Already registered")
            user = User(email, self._password_service.hash_password(password))
            uow.add(user)
            await uow.flush(user)
            return user.id

