import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database_seeding import Seeding
from models.base import Base
from models.user import User
from models.post import Post


@pytest.fixture
def setup():
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)

    yield Session()  # "Pausar" här och skickar tillbaka Session

    Base.metadata.drop_all(engine)
    Session.close_all()


def test_seed_database(setup: Session):
    Seeding.seed_database(setup)

    customer = setup.query(User).first()

    assert customer is not None
    assert customer.passport is not None


def test_create_user_with_same_email(setup: Session):
    user = User(full_name="Kimmo Ahola", email="test@test.se")
    user_2 = User(full_name="Kimmo Ahola", email="test@test.se")

    Seeding.create_user(setup, user)
    Seeding.create_user(setup, user_2)
