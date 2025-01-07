import pytest
import allure
from tests.base_test import BaseTest, fake


class TestGetUser(BaseTest):

    @allure.title("Get user with correct data")
    @pytest.mark.smoke
    def test_get_user_with_correct_data(self, some_user):
        self.user.get_user(some_user["payloads"]["username"])
        self.user.check_status_code()

    @allure.title("Get user with invalid user name")
    @pytest.mark.parametrize(
        "user_name",
        [
            fake.pyint(),
            fake.pyfloat(),
            fake.pybool(),
            None,
            ""
        ]
    )
    def test_get_user_with_invalid_user_name(self, user_name):
        self.user.get_user(user_name)
        self.user.check_status_code(404)
