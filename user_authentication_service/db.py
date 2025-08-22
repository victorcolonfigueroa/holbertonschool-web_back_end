#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find the first row in the users table filtered by kwargs.
        Raises NoResultFound if no user is found.
        Raises InvalidRequestError if query arguments are invalid.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        This method will use find_user_by to locate the user to update,
        then will update the user's attributes as passed in the kwargs
        then commit the changes to the database
        if an argument that does not correspond to a user attribute is passed,
        raise a ValueError
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise ValueError
                setattr(user, key, value)
            self._session.commit()
        except ValueError:
            raise ValueError