import requests
import allure
from services.base_service import BaseService
from config.endpoints import UserEndpoints
from config.payloads import UserPayloads
from config.params import UserParams
from config.models import UserModel


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = UserEndpoints()
        self.payloads = UserPayloads()
        self.params = UserParams()

    @allure.step("Create user")
    def create_user(
        self,
        username,
        firstName,
        lastName,
        email,
        password,
        phone
    ):
        self.response = requests.post(
            headers=self.headers.headers,
            url=self.endpoints.create_user,
            json=self.payloads.create_user(
                username,
                firstName,
                lastName,
                email,
                password,
                phone
            )
        )

    @allure.step("Get user")
    def get_user(self, user_name):
        self.response = requests.get(
            headers=self.headers.headers,
            url=self.endpoints.get_user(user_name)
        )
        return self.validate(200, UserModel)

    @allure.step("Delete user")
    def delete_user(self, user_name):
        self.response = requests.delete(
            headers=self.headers.headers,
            url=self.endpoints.delete_user(user_name)
        )
