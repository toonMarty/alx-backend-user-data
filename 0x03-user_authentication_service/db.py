#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        This method saves a user to the database
        Args:
            email(str): the user's email
            hashed_password(str): the user's hashed_password
        Return:
             new_user(User): a user instance
        """
        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        This method takes in arbitrary keyword arguments and
        returns the first row found in the users table as filtered by the
        method's input argument
        """
        session = self._session
        our_user = session.query(User).filter_by(**kwargs).first()

        if not our_user:
            raise NoResultFound
        return our_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        This method updates a user given the user_id and
        arbitrary keyword arguments (fields we want to update)
        Args:
            user_id(int): the user id
            kwargs: an arbitrary keyword argument(s)
        Return:
             None
        """

        user_to_mod = self.find_user_by(id=user_id)

        for key, val in kwargs.items():
            if key not in user_to_mod.__dict__:
                raise ValueError
            setattr(user_to_mod, key, val)
        return None
