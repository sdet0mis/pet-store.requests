class PetPayloads:

    add_pet = lambda self, name: {
        "name": name
    }


class StorePayloads:

    add_order = lambda self, pet_id, quantity: {
        "petId": pet_id,
        "quantity": quantity
    }


class UserPayloads:

    create_user = lambda self, user_name, first_name, last_name, email, \
        password, phone: {
            "username": user_name,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "phone": phone
        }
