
class Store:
    def __init__(self, name, store_id, location, open_time, close_time):
        self.name = name
        self.store_id = store_id
        self.location = location
        self.open_time = open_time
        self.close_time = close_time
        self.inventory = {}
        self.providers = []

    def add_provider(self, provider):
        self.providers.append(provider)


    def is_open(self, current_time):
        return self.open_time <= current_time.time() <= self.close_time

    def calculate_delivery_time(self, user_coords):
        distance = ((self.location[0] - user_coords[0])**2 + (self.location[1] - user_coords[1])**2)**0.5
        delivery_time = distance * 30 + 60 + 60  # 30 сек на единицу расстояния, 1 мин на выход со склада, 1 мин на доставку
        return delivery_time

    def find_item_by_name(self, name):
        for item, quantity in self.inventory.items():
            if item.name == name:
                return item

    def process_user_order(self, user_order):
        available_items = {}
        for item, quantity in user_order.items():
            name_of_user_item = item.name
            store_item = self.find_item_by_name(name_of_user_item)
            if self.inventory[store_item]>= quantity:
                available_items[item] = quantity
                self.inventory[item] = self.inventory[item] - quantity
            else:
                available_items[item] = self.inventory.get(item, 0)
                self.inventory[item] = 0
        return available_items

    def start_work(self, order, storekeeper, courier,user_adress):
        order.storekeeper = storekeeper
        order.courier = courier
        storekeeper.perform_work(order)
        courier.perform_work(order,self.location,user_adress)

    def print_all_items(self):
        for item, quantity in self.inventory.items():
            print(f"{item.name}: {quantity}")

    def receive_stock(self, items):
        for item, quantity in items.items():
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
