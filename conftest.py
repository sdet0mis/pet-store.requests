import pytest
import allure
from services.user import UserService
from services.pet import PetService
from config.payloads import UserPayloads
from tests.base_test import fake


@allure.step("Some user")
@pytest.fixture()
def some_user():
    payloads = UserPayloads().create_user(fake.user_name(), fake.first_name(),
                                          fake.last_name(), fake.email(),
                                          fake.password(), fake.phone_number())
    UserService().create_user(**payloads)
    model = UserService().get_user(payloads["username"])
    yield {"payloads": payloads, "model": model}
    UserService().delete_user(payloads["username"])


@allure.step("Some pet")
@pytest.fixture()
def some_pet():
    return PetService().add_pet(fake.name())
