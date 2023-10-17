from userdescriptor import User
import pytest


def test_new_user():
    user1 = User("Alina", "avasileva@dp.com", "Alina1997")
    assert user1.username == "Alina"
    assert user1.email == "avasileva@dp.com"
    assert user1.password == "Alina1997"


def test_wrong_password_only_letters():
    with pytest.raises(ValueError):
        user2 = User("Alena", "aivanova@dp.com", "nonumbers")


def test_wrong_password_only_digits():
    with pytest.raises(ValueError):
        user2 = User("Alena1", "aivanova@dp.com", "123456789")


def test_wrong_password_only_symbols():
    with pytest.raises(ValueError):
        user2 = User("Alena2", "aivanova@dp.com", "&*&*&*&*&*&*&*&")


def test_short_password():
    with pytest.raises(ValueError):
        user2 = User("Alena3", "aivanova@dp.com", "4non4")


def test_same_name():
    user2 = User("Elena", "eivanova@dp.com", "password1")
    with pytest.raises(ValueError):
        user3 = User("Elena", "esmirnova@dp.com", "password2")


def test_wrong_email_at():
    with pytest.raises(ValueError):
        user3 = User("Olesya", "osmirnovadp.com", "password3")


def test_wrong_email_dot():
    with pytest.raises(ValueError):
        user3 = User("Olga", "oivanova@dpcom", "password4")


def test_wrong_email_both():
    with pytest.raises(ValueError):
        user3 = User("Katerina", "kivanovadpcom", "password5")


def test_new_password():
    user3 = User("EKaterina", "ekivanova@dp.com", "password5")
    assert user3.password == "password5"
    user3.change_password("qwerty2023")
    assert user3.password == "qwerty2023"
    assert user3.password != "password5"


def test_del_username():
    user9 = User("Natalia", "nivanova@dp.com", "pass12345")
    assert user9.password == "pass12345"
    user9.delete_account()
    with pytest.raises(KeyError):
        user9.password
        user9.email
        user9.username


def test_del_user_and_create_with_same_name():
    user10 = User("Natalia", "nivanova@dp.com", "pass12345")
    assert user10.password == "pass12345"
    user10.delete_account()
    with pytest.raises(KeyError):
        user10.password
        user10.email
        user10.username
    user11 = User("Natalia", "nkim@dp.com", "pass123465")
    assert user11.username == "Natalia"
    assert user11.email == "nkim@dp.com"
    assert user11.password == "pass123465"


def test_get_all_accounts():
    spisok = [
        ("Alina", "avasileva@dp.com", "Alina1997"),
        ("Elena", "eivanova@dp.com", "password1"),
        ("EKaterina", "ekivanova@dp.com", "qwerty2023"),
        ("Natalia", "nkim@dp.com", "pass123465"),
    ]
    getusers = User.get_all_users()
    assert spisok == getusers
