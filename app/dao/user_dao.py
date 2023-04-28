from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).one_or_none()

    def get_all(self):
        return self.session.query(User).all()

    def update(self, data):
        self.session.add(data)
        self.session.commit()
        return data
