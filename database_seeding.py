from sqlalchemy.orm import Session

from models.user import Passport, User


class Seeding:
    @staticmethod
    def seed_database(session: Session):
        if session.query(User).count() == 0:
            user = User(
                full_name="Kimmo Ahola",
                email="test@test.se",
                passport=Passport(),  # We can use this way of creating object since we use relationships
            )
            session.add(user)
            session.commit()

    @staticmethod
    def create_user(session: Session, user: User):
        # Since email is unique we need to check if the user already exists
        # If we try to add two users with the same email we get an error
        existing_user = session.query(User).where(User.email == user.email).first()

        if not existing_user:
            session.add(user)
            session.commit()
