from typing import Literal
from datetime import datetime, timedelta
from sqlalchemy import DateTime, Time, ForeignKey, String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app import db

# Enums for specific field types
PRIORITY = Literal[
    "urgent, important",
    "not urgent, important",
    "urgent, not important",
    "not urgent, not important",
]
MOOD = Literal["Motivated", "Tired", "Struggling"]
GOAL_TYPE = Literal["Personal", "Professional", "Health"]
GOAL_STATUS = Literal["pending", "done"]


class Users(db.Model):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20))
    last_name: Mapped[str] = mapped_column(String(20))
    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(20))

    def to_json(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }


class Tasks(db.Model):
    __tablename__ = "tasks"
    task_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(255))
    priority: Mapped[PRIORITY] = mapped_column(
        Enum(
            "urgent, important",
            "not urgent, important",
            "urgent, not important",
            "not urgent, not important",
            name="priority",
        ),
        nullable=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id"), nullable=False
    )
    session_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("sessions.session_id", ondelete="CASCADE"), nullable=True
    )
    goal_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("goals.goal_id", ondelete="CASCADE"), nullable=True
    )

    def to_json(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
        }


class Sessions(db.Model):
    __tablename__ = "sessions"
    session_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    start_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
    end_time: Mapped[DateTime] = mapped_column(DateTime)
    duration: Mapped[DateTime] = mapped_column(Time)
    breaks: Mapped[int] = mapped_column(Integer, default=0)
    task_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tasks.task_id", ondelete="CASCADE"), nullable=True
    )
    mood_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("moods.mood_id", ondelete="CASCADE"), nullable=True
    )

    def set_duration(self):
        if self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            self.duration = (datetime.min + delta).time()

    def to_json(self):
        return {
            "session_id": self.session_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": self.duration,
            "breaks": self.breaks,
        }


class Moods(db.Model):
    __tablename__ = "moods"
    mood_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    mood_status: Mapped[MOOD] = mapped_column(
        Enum(
            "happy",
            "sad",
            "neutral",
            "excited",
            "stressed",
            "relaxed",
            name="mood_status",
        )
    )
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("sessions.session_id"))

    def to_json(self):
        return {"mood_id": self.mood_id, "mood_status": self.mood_status}


class Goals(db.Model):
    __tablename__ = "goals"
    goal_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    goal_type: Mapped[GOAL_TYPE] = mapped_column(
        Enum("personal", "professional", "health", name="goal_type")
    )
    goal_status: Mapped[GOAL_STATUS] = mapped_column(
        Enum("pending", "in progress", "done", name="goal_status"), default="pending"
    )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"))
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("tasks.task_id"))

    def to_json(self):
        return {
            "goal_id": self.goal_id,
            "goal_type": self.goal_type,
            "goal_status": self.goal_status,
        }
