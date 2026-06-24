from kin_portal import KinPortal, User, generate_invitation_link, send_invitation_link

def test_create_account():
    kin_portal = KinPortal()
    email = "user@example.com"
    user = kin_portal.create_account(email)
    assert user.id == 1
    assert user.email == email
    assert user.password == "temporary_password"

def test_login():
    kin_portal = KinPortal()
    email = "user@example.com"
    kin_portal.create_account(email)
    assert kin_portal.login(email, "temporary_password") == True
    assert kin_portal.login(email, "wrong_password") == False

def test_add_photo():
    kin_portal = KinPortal()
    email = "user@example.com"
    kin_portal.create_account(email)
    kin_portal.add_photo(email, "photo1.jpg")
    assert kin_portal.get_photo_album(email) == {email: ["photo1.jpg"]}

def test_get_photo_album():
    kin_portal = KinPortal()
    email = "user@example.com"
    kin_portal.create_account(email)
    kin_portal.add_photo(email, "photo1.jpg")
    kin_portal.add_photo(email, "photo2.jpg")
    assert kin_portal.get_photo_album(email) == {email: ["photo1.jpg", "photo2.jpg"]}

def test_generate_invitation_link():
    email = "user@example.com"
    link = generate_invitation_link(email)
    assert link == f"https://kin-portal.com/invite/{email}"

def test_send_invitation_link():
    email = "user@example.com"
    link = generate_invitation_link(email)
    send_invitation_link(email, link)
    # No assertion, just testing that it runs without error

def test_create_account_duplicate_email():
    kin_portal = KinPortal()
    email = "user@example.com"
    kin_portal.create_account(email)
    try:
        kin_portal.create_account(email)
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == "Email already exists"

def test_login_non_existent_email():
    kin_portal = KinPortal()
    email = "user@example.com"
    assert kin_portal.login(email, "password") == False

def test_add_photo_non_existent_email():
    kin_portal = KinPortal()
    email = "user@example.com"
    try:
        kin_portal.add_photo(email, "photo1.jpg")
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == "Email does not exist"

def test_get_photo_album_non_existent_email():
    kin_portal = KinPortal()
    email = "user@example.com"
    try:
        kin_portal.get_photo_album(email)
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) == "Email does not exist"
