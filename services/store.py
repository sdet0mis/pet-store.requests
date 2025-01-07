import requests
import allure
from services.base_service import BaseService
from config.endpoints import StoreEndpoints
from config.payloads import StorePayloads
from config.params import StoreParams
from config.models import OrderModel


class StoreService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = StoreEndpoints()
        self.payloads = StorePayloads()
        self.params = StoreParams()

    @allure.step("Add order")
    def add_order(self, pet_id, quantity):
        self.response = requests.post(
            headers=self.headers.headers,
            url=self.endpoints.add_order,
            json=self.payloads.add_order(pet_id, quantity)
        )
        return self.validate(200, OrderModel)
