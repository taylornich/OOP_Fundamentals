class Vehicle:
    def __init__(self, registration, type, owner):
        self.registration_number = registration
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of this vehicle has been updated to {new_owner}.")
        