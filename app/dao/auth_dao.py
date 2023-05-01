from app.dao.model.user import User
from app.dao.serialization.auth import AuthUserSchema


class AuthDAO:

    def __init__(self, session):
        self.session = session

    def create(self, email: str, password_hash: str):
        new_user = User(
            email=email,
            password=password_hash
        )

        self.session.add(new_user)
        self.session.commit()

        return new_user

    def get_by_email(self, email: str):
        user = self.session.query(
            User,
        ).filter(
            User.email == email,
        ).one_or_none()

        if user is not None:
            return user

        return None
