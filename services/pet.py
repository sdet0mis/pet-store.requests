import requests
import allure
from services.base_service import BaseService
from config.endpoints import PetEndpoints
from config.payloads import PetPayloads
from config.params import PetParams
from config.models import PetModel


class PetService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = PetEndpoints()
        self.payloads = PetPayloads()
        self.params = PetParams()

    @allure.step("Add pet")
    def add_pet(self, name):
        self.response = requests.post(
            headers=self.headers.headers,
            url=self.endpoints.add_pet,
            json=self.payloads.add_pet(name)
        )
        return self.validate(200, PetModel)

    @allure.step("Find pet")
    def find_pet(self, pet_id):
        self.response = requests.get(
            headers=self.headers.headers,
            url=self.endpoints.find_pet(pet_id)
        )

    @allure.step("Delete pet")
    def delete_pet(self, pet_id):
        self.response = requests.delete(
            headers=self.headers.headers,
            url=self.endpoints.delete_pet(pet_id)
        )
