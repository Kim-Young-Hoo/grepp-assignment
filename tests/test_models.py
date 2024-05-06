import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from db.base import Base
from db.models.exam import Exam, ExamSlot
from db.models.reservation import Reservation
from db.models.user import User


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', connect_args={"check_same_thread": False})
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        self.session = self.Session()

    def tearDown(self):
        print("tear down")
        self.session.rollback()
        self.session.close()
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()

    def test_create_user(self):
        user = User(
            name="김영후",
            email="chrishoho8902@gmail.com",
            password="1234",
            role="user"
        )
        self.session.add(user)
        self.session.commit()
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "chrishoho8902@gmail.com")

    def test_create_exam(self):
        exam = Exam(
            title="모의 코딩테스트",
            description="코딩테스트를 시행합니다"
        )
        self.session.add(exam)
        self.session.commit()
        self.assertIsNotNone(exam.id)
        self.assertEqual(exam.title, "모의 코딩테스트")



if __name__ == "__main__":
    unittest.main()
