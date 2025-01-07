import pytest
import allure
from tests.base_test import BaseTest, fake


class TestAddOrder(BaseTest):

    @allure.title("Add order with correct data")
    @pytest.mark.smoke
    def test_add_order_with_correct_data(self):
        self.store.add_order(fake.pyint(), fake.pyint())
        self.store.check_status_code()

    @allure.title("Add order with invalid pet id")
    @pytest.mark.parametrize(
        "pet_id, quantity",
        [
            (fake.pystr(), fake.pyint()),
            (fake.pyfloat(), fake.pyint()),
            (fake.pybool(), fake.pyint()),
            (None, fake.pyint()),
            ("", fake.pyint())
        ]
    )
    def test_add_order_with_invalid_pet_id(self, pet_id, quantity):
        self.store.add_order(pet_id, quantity)
        self.store.check_status_code(400)

    @allure.title("Add order with invalid quantity")
    @pytest.mark.parametrize(
        "pet_id, quantity",
        [
            (fake.pyint(), fake.pystr()),
            (fake.pyint(), fake.pyfloat()),
            (fake.pyint(), fake.pybool()),
            (fake.pyint(), None),
            (fake.pyint(), "")
        ]
    )
    def test_add_order_with_invalid_quantity(self, pet_id, quantity):
        self.store.add_order(pet_id, quantity)
        self.store.check_status_code(400)
