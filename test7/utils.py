from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    'jhondoe': {
        'username': 'jhondoe',
        'hashed_password': pwd_context.hash('secret'),
    }
}

def get_user(username: str):
    user = fake_users_db.get(username)
    if user:
        return user
    return None

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)