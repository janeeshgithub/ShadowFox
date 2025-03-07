# Base Class
class MobilePhone:
    def __init__(self, brand, model, screen_type="Touch Screen", network_type="4G/5G",
                 dual_sim=False, front_camera="8MP", rear_camera="12MP",
                 ram="4GB", storage="64GB"):
        self.brand = brand
        self.model = model
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def receive_call(self):
        print(f"Incoming call on {self.brand} {self.model}...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.rear_camera} rear camera on {self.brand} {self.model}.")

    def get_specs(self):
        return (f"Brand: {self.brand}, Model: {self.model}, Screen: {self.screen_type}, "
                f"Network: {self.network_type}, Dual SIM: {self.dual_sim}, "
                f"Front Camera: {self.front_camera}, Rear Camera: {self.rear_camera}, "
                f"RAM: {self.ram}, Storage: {self.storage}")


# Apple Child Class
class Apple(MobilePhone):
    def __init__(self, model, front_camera="12MP", rear_camera="48MP", ram="4GB", storage="128GB"):
        super().__init__("Apple", model, front_camera=front_camera, rear_camera=rear_camera, 
                         ram=ram, storage=storage, dual_sim=False)

    def use_face_id(self):
        print(f"Using Face ID on {self.model}.")

    def get_specs(self):
        return f"{super().get_specs()}, Face ID: Yes"


# Samsung Child Class
class Samsung(MobilePhone):
    def __init__(self, model, front_camera="16MP", rear_camera="32MP", ram="8GB", storage="256GB", dual_sim=True):
        super().__init__("Samsung", model, front_camera=front_camera, rear_camera=rear_camera, 
                         ram=ram, storage=storage, dual_sim=dual_sim)

    def use_s_pen(self):
        print(f"Using S-Pen on {self.model}.")

    def get_specs(self):
        return f"{super().get_specs()}, S-Pen Support: {'Yes' if 'Note' in self.model else 'No'}"


# Creating objects for Apple
iphone_13 = Apple("iPhone 13", front_camera="12MP", rear_camera="48MP", ram="4GB", storage="128GB")
iphone_14 = Apple("iPhone 14 Pro", front_camera="12MP", rear_camera="48MP", ram="6GB", storage="256GB")

# Creating objects for Samsung
galaxy_s21 = Samsung("Galaxy S21", front_camera="16MP", rear_camera="32MP", ram="8GB", storage="128GB")
galaxy_note20 = Samsung("Galaxy Note 20", front_camera="16MP", rear_camera="48MP", ram="12GB", storage="512GB")

# Testing functionality
print(iphone_13.get_specs())
iphone_13.make_call("+1234567890")
iphone_13.use_face_id()

print("\n" + galaxy_note20.get_specs())
galaxy_note20.receive_call()
galaxy_note20.use_s_pen()
