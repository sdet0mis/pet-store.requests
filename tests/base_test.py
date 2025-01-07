from faker import Faker
from services.pet import PetService
from services.store import StoreService
from services.user import UserService

fake = Faker()


class BaseTest:

    def setup_method(self):
        self.pet = PetService()
        self.store = StoreService()
        self.user = UserService()
