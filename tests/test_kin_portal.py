from kin_portal import KinPortal, FamilyMember, SharedContent

def test_add_family_member():
    portal = KinPortal()
    portal.add_family_member("Jane Doe", 25)
    assert len(portal.get_family_members()) == 1
    assert portal.get_family_members()[0].name == "Jane Doe"
    assert portal.get_family_members()[0].age == 25

def test_add_shared_content():
    portal = KinPortal()
    portal.add_shared_content("Family Videos", "A collection of family videos")
    assert len(portal.get_shared_content()) == 1
    assert portal.get_shared_content()[0].title == "Family Videos"
    assert portal.get_shared_content()[0].description == "A collection of family videos"

def test_get_instructions():
    portal = KinPortal()
    assert portal.get_instructions() == "Welcome to the Kin Portal! To access shared content, please navigate to the 'Shared Content' section."

def test_get_feedback_added_family_member():
    portal = KinPortal()
    assert portal.get_feedback("added_family_member") == "Family member added successfully!"

def test_get_feedback_added_shared_content():
    portal = KinPortal()
    assert portal.get_feedback("added_shared_content") == "Shared content added successfully!"

def test_get_feedback_invalid_action():
    portal = KinPortal()
    assert portal.get_feedback("invalid_action") == "Invalid action"

def test_get_family_members_empty():
    portal = KinPortal()
    assert len(portal.get_family_members()) == 0

def test_get_shared_content_empty():
    portal = KinPortal()
    assert len(portal.get_shared_content()) == 0
