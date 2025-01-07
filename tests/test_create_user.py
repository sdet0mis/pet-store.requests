import pytest
import allure
from tests.base_test import BaseTest, fake


class TestCreateUser(BaseTest):

    @allure.title("Create user with correct data")
    @pytest.mark.smoke
    def test_create_user_with_correct_data(self):
        self.user.create_user(fake.user_name(), fake.first_name(),
                              fake.last_name(), fake.email(), fake.password(),
                              fake.phone_number())
        self.user.check_status_code()

    @allure.title("Create user with invalid user name")
    @pytest.mark.parametrize(
        "user_name, first_name, last_name, email, password, phone",
        [
            (fake.pyint(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.pyfloat(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.pybool(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (None, fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            ("", fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number())
        ]
    )
    def test_create_user_with_invalid_user_name(self, user_name, first_name,
                                                last_name, email, password,
                                                phone):
        self.user.create_user(user_name, first_name, last_name, email,
                              password, phone)
        self.user.check_status_code(400)

    @allure.title("Create user with invalid first name")
    @pytest.mark.parametrize(
        "user_name, first_name, last_name, email, password, phone",
        [
            (fake.user_name(), fake.pyint(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.pyfloat(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.pybool(), fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), None, fake.last_name(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), "", fake.last_name(),
             fake.email(), fake.password(), fake.phone_number())
        ]
    )
    def test_create_user_with_invalid_first_name(self, user_name, first_name,
                                                 last_name, email, password,
                                                 phone):
        self.user.create_user(user_name, first_name, last_name, email,
                              password, phone)
        self.user.check_status_code(400)

    @allure.title("Create user with invalid last name")
    @pytest.mark.parametrize(
        "user_name, first_name, last_name, email, password, phone",
        [
            (fake.user_name(), fake.first_name(), fake.pyint(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.pyfloat(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.pybool(),
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), None,
             fake.email(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), "",
             fake.email(), fake.password(), fake.phone_number())
        ]
    )
    def test_create_user_with_invalid_last_name(self, user_name, first_name,
                                                last_name, email, password,
                                                phone):
        self.user.create_user(user_name, first_name, last_name, email,
                              password, phone)
        self.user.check_status_code(400)

    @allure.title("Create user with invalid email")
    @pytest.mark.parametrize(
        "user_name, first_name, last_name, email, password, phone",
        [
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.pystr(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.pyint(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.pyfloat(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.pybool(), fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             None, fake.password(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             "", fake.password(), fake.phone_number())
        ]
    )
    def test_create_user_with_invalid_email(self, user_name, first_name,
                                            last_name, email, password,
                                            phone):
        self.user.create_user(user_name, first_name, last_name, email,
                              password, phone)
        self.user.check_status_code(400)

    @allure.title("Create user with invalid password")
    @pytest.mark.parametrize(
        "user_name, first_name, last_name, email, password, phone",
        [
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.pybool(), fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), None, fake.phone_number()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), "", fake.phone_number())
        ]
    )
    def test_create_user_with_invalid_password(self, user_name, first_name,
                                               last_name, email, password,
                                               phone):
        self.user.create_user(user_name, first_name, last_name, email,
                              password, phone)
        self.user.check_status_code(400)

    @allure.title("Create user with invalid phone")
    @pytest.mark.parametrize(
        "user_name, first_name, last_name, email, password, phone",
        [
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.pystr()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.pyint()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.pyfloat()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), fake.pybool()),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), None),
            (fake.user_name(), fake.first_name(), fake.last_name(),
             fake.email(), fake.password(), "")
        ]
    )
    def test_create_user_with_invalid_phone(self, user_name, first_name,
                                            last_name, email, password,
                                            phone):
        self.user.create_user(user_name, first_name, last_name, email,
                              password, phone)
        self.user.check_status_code(400)
