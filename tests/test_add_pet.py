import pytest
import allure
from tests.base_test import BaseTest, fake


class TestAddPet(BaseTest):

    @allure.title("Add pet with correct data")
    @pytest.mark.smoke
    def test_add_pet_with_correct_data(self):
        self.pet.add_pet(fake.name())
        self.pet.check_status_code()

    @allure.title("Add pet with invalid name")
    @pytest.mark.parametrize(
        "name",
        [
            fake.pyint(),
            fake.pyfloat(),
            fake.pybool(),
            None,
            ""
        ]
    )
    def test_add_pet_with_invalid_name(self, name):
        self.pet.add_pet(name)
        self.pet.check_status_code(400)
