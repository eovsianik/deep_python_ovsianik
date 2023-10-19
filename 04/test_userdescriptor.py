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


def test_new_wrong_password():
    user19 = User("Julia", "jivanova@dp.com", "Julia_2003")
    assert user19.password == "Julia_2003"
    with pytest.raises(ValueError):
        user19.change_password("qiwi")
    assert user19.password == "Julia_2003"


def test_del_username():
    user9 = User("Natalia", "nivanova@dp.com", "pass12345")
    assert user9.password == "pass12345"
    user9.delete_account()
    with pytest.raises(KeyError):
        user9.password
        user9.email
        user9.username
        user9.backup_email


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


def test_with_backup_email():
    user21 = User("Daria", "dkim@dp.com", "Daria2000", "dtzoy@dp.com")
    assert user21.username == "Daria"
    assert user21.email == "dkim@dp.com"
    assert user21.password == "Daria2000"
    assert user21.backup_email == "dtzoy@dp.com"


def test_with_backup_email1():
    user29 = User("Larisa", "lvong@dp.com", "Larisa1997")
    assert user29.username == "Larisa"
    assert user29.email == "lvong@dp.com"
    assert user29.password == "Larisa1997"
    user29.backup_email = "lling@dp.com"
    assert user29.backup_email == "lling@dp.com"


def test_with_wrong_backup_email():
    user31 = User("Lina", "lvolt@dp.com", "Lina1996")
    assert user31.username == "Lina"
    assert user31.email == "lvolt@dp.com"
    assert user31.password == "Lina1996"
    with pytest.raises(ValueError):
        user31.backup_email = "voltdp.com"
    assert user31.backup_email is None


def test_del_with_backup_email():
    user35 = User("Lana", "lavolt@dp.com", "Lana1996", "laling@dp.com")
    assert user35.username == "Lana"
    assert user35.email == "lavolt@dp.com"
    assert user35.password == "Lana1996"
    user35.delete_account()
    with pytest.raises(KeyError):
        user35.password
        user35.email
        user35.username
        user35.backup_email


def test_get_all_accounts():
    spisok = [
        ("Alina", "avasileva@dp.com", "Alina1997", None),
        ("Elena", "eivanova@dp.com", "password1", None),
        ("EKaterina", "ekivanova@dp.com", "qwerty2023", None),
        ("Julia", "jivanova@dp.com", "Julia_2003", None),
        ("Natalia", "nkim@dp.com", "pass123465", None),
        ("Daria", "dkim@dp.com", "Daria2000", "dtzoy@dp.com"),
        ("Larisa", "lvong@dp.com", "Larisa1997", "lling@dp.com"),
        ("Lina", "lvolt@dp.com", "Lina1996", None),
    ]
    getusers = User.get_all_users()
    assert spisok == getusers
