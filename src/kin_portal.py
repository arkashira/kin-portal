import json
from dataclasses import dataclass
from typing import List

@dataclass
class FamilyMember:
    name: str
    age: int

@dataclass
class SharedContent:
    title: str
    description: str

class KinPortal:
    def __init__(self):
        self.family_members = []
        self.shared_content = []

    def add_family_member(self, name: str, age: int):
        self.family_members.append(FamilyMember(name, age))

    def add_shared_content(self, title: str, description: str):
        self.shared_content.append(SharedContent(title, description))

    def get_family_members(self) -> List[FamilyMember]:
        return self.family_members

    def get_shared_content(self) -> List[SharedContent]:
        return self.shared_content

    def get_instructions(self) -> str:
        return "Welcome to the Kin Portal! To access shared content, please navigate to the 'Shared Content' section."

    def get_feedback(self, action: str) -> str:
        if action == "added_family_member":
            return "Family member added successfully!"
        elif action == "added_shared_content":
            return "Shared content added successfully!"
        else:
            return "Invalid action"

def main():
    portal = KinPortal()
    portal.add_family_member("John Doe", 30)
    portal.add_shared_content("Family Photos", "A collection of family photos")
    print(portal.get_instructions())
    print(portal.get_feedback("added_family_member"))
    print(portal.get_feedback("added_shared_content"))

if __name__ == "__main__":
    main()
