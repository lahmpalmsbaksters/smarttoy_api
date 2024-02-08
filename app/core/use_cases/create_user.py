from app.core.entities.user import User

class CreateUserUseCase:
    def execute(self, username: str, email: str) -> User:
        # Business logic to create a user
        user_id = 1  # Dummy ID for illustration purposes
        return User(id=user_id, username=username, email=email)
