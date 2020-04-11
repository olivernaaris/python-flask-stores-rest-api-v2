from typing import Dict, Union

from db import db

UserJSON = Dict[str, Union[int, str]]


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @classmethod
    def json(cls) -> UserJSON:
        return {"id": self.id, "username": self.username}

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def save_to_db(cls) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_from_db(cls) -> None:
        db.session.delete(self)
        db.session.commit()
