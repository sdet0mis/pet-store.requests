import pytest
import allure
from tests.base_test import BaseTest, fake


class TestFindPet(BaseTest):

    @allure.title("Find pet with correct data")
    @pytest.mark.smoke
    def test_find_pet_with_correct_data(self, some_pet):
        self.pet.find_pet(some_pet.id)
        self.pet.check_status_code()

    @allure.title("Find pet with invalid pet id")
    @pytest.mark.parametrize(
        "pet_id",
        [
            fake.pystr(),
            fake.pyfloat(),
            fake.pybool(),
            None,
            ""
        ]
    )
    def test_find_pet_with_invalid_pet_id(self, pet_id):
        self.pet.find_pet(pet_id)
        self.pet.check_status_code(404)
