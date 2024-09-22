import unittest
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Users, Tasks, Sessions, Moods, Goals
from datetime import datetime, timedelta
from app import db

class TestDatabaseModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """set memory in SQLite DB for all tests"""
        cls.engine = create_engine('sqlite:///:memory:')
        db.create_all(bind=cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        """clean up Database after all tests"""
        db.metadata.drop_all(bind=cls.engine)

    def setUp(self):
        """set up new database session"""
        self.session = self.Session()

    def tearDown(self):
        """close session after each test"""
        self.session.close()

    def test_user_creation(self):
        new_user = Users(
            first_name="Alphonse",
            last_name="Mugisha",
            username="mugisha",
            email="prudent.nkubito@gmail.com",
        )

        self.session.add(new_user)
        self.session.commit()

        self.assertIsNotNone(new_user.user_id)
        self.assertEqual(new_user.first_name, "Alphonse")
        self.assertEqual(new_user.username, "mugisha")

    def test_task_creation(self):
        new_task = Tasks(
            title="Complete project",
            description="Completed",
            priority="urgent, important",
            user_id=1
        )
        self.session.add(new_task)
        self.session.commit()

        self.assertIsNotNone(new_task.task_id)
        self.assertEqual(new_task.title, "Complete project")
        self.assertEqual(new_task.priority, "urgent, important")

    def test_session_duration(self):
        start_time = datetime.utcnow()
        end_time = start_time + timedelta(hours=1)

        new_session = Sessions(
            start_time=start_time,
            end_time=end_time,
            breaks=1
        )
        new_session.set_duration()

        self.session.add(new_session)
        self.session.commit()

        self.assertIsNotNone(new_session.session_id)
        self.assertIsNotNone(new_session.duration)
        self.assertEqual(new_session.duration.seconds // 3600, 1)
        self.assertEqual(new_session.breaks, 1)

if __name__ == '__main__':
    unittest.main()
