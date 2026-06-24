import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class User:
    id: int
    email: str
    password: str

class KinPortal:
    def __init__(self):
        self.users = {}
        self.photo_album = {}

    def create_account(self, email: str) -> User:
        if email in self.users:
            raise ValueError("Email already exists")
        user_id = len(self.users) + 1
        user = User(id=user_id, email=email, password="temporary_password")
        self.users[email] = user
        return user

    def login(self, email: str, password: str) -> bool:
        if email not in self.users:
            return False
        user = self.users[email]
        return user.password == password

    def add_photo(self, email: str, photo: str):
        if email not in self.users:
            raise ValueError("Email does not exist")
        if email not in self.photo_album:
            self.photo_album[email] = []
        self.photo_album[email].append(photo)

    def get_photo_album(self, email: str) -> Dict[str, list]:
        if email not in self.users:
            raise ValueError("Email does not exist")
        return {email: self.photo_album.get(email, [])}

def generate_invitation_link(email: str) -> str:
    return f"https://kin-portal.com/invite/{email}"

def send_invitation_link(email: str, link: str):
    print(f"Sending invitation link to {email}: {link}")

def main():
    kin_portal = KinPortal()
    email = "user@example.com"
    link = generate_invitation_link(email)
    send_invitation_link(email, link)
    user = kin_portal.create_account(email)
    kin_portal.add_photo(email, "photo1.jpg")
    kin_portal.add_photo(email, "photo2.jpg")
    print(kin_portal.get_photo_album(email))

if __name__ == "__main__":
    main()
