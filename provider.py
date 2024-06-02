from random import randint
from Item import Item
from order import Order
import time
class Provider:
    def __init__(self, name, provider_id):
        self.name = name
        self.provider_id = provider_id
        self.inventory = {}

    def find_item_by_name(self, name):
        for item in self.inventory.keys():
            if item.name == name:
                return item
        return None

    def send_order(self, request):
        order_items = {}
        for item, amount in request.items():
            available_amount = self.inventory.get(item, 0)
            if available_amount >= amount:
                order_items[item] = amount
                self.inventory[item] -= amount
            else:
                order_items[item] = available_amount
                self.inventory[item] = 0
        order = Order(status="Собран у поставщика", order_items=order_items,
                      create_order_time= time.datetime.now(), delivery_order_time=None,
                      storekeeper=None, courier=None)
        return order

    def update_stocks(self, what_to_update):
        for item, amount in what_to_update.items():
            if item in self.inventory:
                self.inventory[item] += amount
            else:
                self.inventory[item] = amount
    def print_all_provider_items(self):
        for item, amount in self.inventory.items():
            print(f"Название: {item.name}, Количество: {amount}")
