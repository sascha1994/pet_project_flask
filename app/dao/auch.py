from app.dao.base import BaseDAO
from app.dao.model.user import UserModel
from app.dao.serialization.auth import AuthUserSchema


class AuthDAO(BaseDAO):

    def create(self, email: str, password_hash: str) -> AuthUserSchema:
        new_user = UserModel(
            email=email,
            password_hash=password_hash
        )

        self.session.add(new_user)
        self.session.commit()

        return AuthUserSchema().dump(new_user)

    def get_by_email(self, email: str):
        user = self.session.query(
            UserModel,
        ).filter(
            UserModel.email == email,
        ).one_or_none()

        if user is not None:
            return AuthUserSchema().dump(user)

        return None
