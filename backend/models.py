from typing import Literal
from sqlalchemy import DATETIME, TIME, ForeignKey, String, Integer
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column
from app import db

PRIORITY = Literal["urgent, important", "not urgent, important", "urgent, not important", "not urgent, not important"]
MOOD = Literal["Motivated", "Tired", "Struggling"]
GOAL_TYPE = Literal["Personal", "Professional", "Health"]
GOAL_STATUS = Literal["pending", "done"]

class Users(db.Model):
    __table_args__ = {'schema': 'schema1'}
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email
        }


class Tasks(db.Model):
    __table_args__ = {'schema': 'schema2'}
    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    priority: Mapped[PRIORITY] = mapped_column(
        sqlalchemy.Enum("urgent, important", "not urgent, important", "urgent, not important", "not urgent, not important", name="priority"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema2.user_id"))
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema2.session_id"))
    goal_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema2.goal_id"))

    def to_json(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority
        }


class Sessions(db.Model):
    __table_args__ = {'schema': 'schema3'}
    session_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_time: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    end_time: Mapped[DATETIME] = mapped_column(DATETIME, nullable=False)
    duration: Mapped[TIME] = mapped_column(TIME, nullable=False)
    breaks: Mapped[int] = mapped_column(nullable=False)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema3.Tasks.task_id"))
    mood_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema3.Moods.mood_id"))

    def to_json(self):
        return {
            "session_id": self.session_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": self.duration,
            "breaks": self.breaks
        }


class Moods(db.Model):
    __table_args__ = {'schema': 'schema4'}
    mood_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mood_status: Mapped[MOOD] = mapped_column(
        sqlalchemy.Enum("Motivated", "Tired", "Struggling", name="mood_status")
    )
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema4.Sessions.session_id"))

    def to_json(self):
        return {
            "mood_id": self.mood_id,
            "mood_status": self.mood_status
        }


class Goals(db.Model):
    __table_args__ = {'schema': 'schema5'}
    goal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    goal_type: Mapped[GOAL_TYPE] = mapped_column(
        sqlalchemy.Enum("Personal", "Professional", "Health", name="goal_type")
    )
    goal_status: Mapped[GOAL_STATUS] = mapped_column(
        sqlalchemy.Enum("pending", "done", name="goal_status")
    )
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("schema5.Tasks.task_id"))

    def to_json(self):
        return {
            "goal_id": self.goal_id,
            "goal_type": self.goal_type,
            "goal_status": self.goal_status
        }

