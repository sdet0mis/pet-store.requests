import pytest
import allure
from tests.base_test import BaseTest, fake


class TestDeleteUser(BaseTest):

    @allure.title("Delete user with correct data")
    @pytest.mark.smoke
    def test_get_user_with_correct_data(self, some_user):
        self.user.delete_user(some_user["payloads"]["username"])
        self.user.check_status_code()

    @allure.title("Delete user with invalid user name")
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
        self.user.delete_user(user_name)
        self.user.check_status_code(404)
