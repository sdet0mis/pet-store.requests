base_url = "https://petstore.swagger.io/v2/"


class PetEndpoints:

    add_pet = f"{base_url}pet/"
    find_pet = lambda self, pet_id: f"{base_url}pet/{pet_id}/"  # noqa
    delete_pet = lambda self, pet_id: f"{base_url}pet/{pet_id}/" # noqa


class StoreEndpoints:

    add_order = f"{base_url}store/order"
    find_order = lambda self, order_id: f"{base_url}store/order/{order_id}/"  # noqa
    delete_order = lambda self, order_id: f"{base_url}store/order/{order_id}/"  # noqa


class UserEndpoints:

    create_user = f"{base_url}user/"
    get_user = lambda self, user_name: f"{base_url}user/{user_name}/"  # noqa
    delete_user = lambda self, user_name: f"{base_url}user/{user_name}/"  # noqa
