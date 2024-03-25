from dataclasses import dataclass, asdict
from datetime import time


@dataclass
class Item:
    store_id: int
    provider_id: int
    name: str
    price: float


# DONE
# Что должно быть? Id внутри системы складов, id внутри системы поставщика, название, себестоимость

class ItemHandle:
    def __init__(self, store_id: int, provider_id: int, name: str, price: float):
        self.item = Item(store_id, provider_id, name, price)

    def get_item(self):
        return asdict(self.item)

    def change_item(self, key, val):
        self.item.__dict__[key] = val



# DONE

class Provider:  # поставщик
    def send_order(self):
        pass

    # send_order - принять и отправить заказ складу

    def update_stocks(self):
        pass

    # update_stocks - обновить число товаров на складе


# TODO

class Worker:
    name: str
    age: int
    month_time: time
    is_bysy: bool

    def get_order(self):  #
        pass

    # принять заказ, если возможно

    def get_shift(self):  # отработка по времени

        pass  # докрутить статрт рабочей смены придумать график и т.д.
    # получить смену, когда работает


class Courier(Worker):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_order(self):
        pass


class Storekeeper(Worker):
    pass


class Store:
    items: [Item]
    def print_all_items(self):
        print("Название   |   стоимость")
        for item in self.items:
            print(item.name, "|", item.price * 2)

    def send_request(self):
        pass

    # send_request - отправить заказ для провайдера (что привезти)

    def take_order(self):
        # set_storkeeper
        pass

    # принять заказ и начать его обрабатывать

    def set_courier(self, items):
        pass

    # дать заказу курьера

    def set_storekeeper(self):
        pass

    # дать заказу кладовщика

    def get_worker(self):
        pass

    # взять работника к себе и дать ему смену


@dataclass
class Order:
    status: str
    items: list(Item)
    create_order_time: time
    delivery_order_time: time
    storekeeper: Storekeeper
    courier: Courier


# Что находится в заказе? Статус доставки, список товаров, время создания-время доставки, кто собирал-доставлял


class User:
    def make_order(self):
        pass

    # сделать заказ

    def take_order(self):
        pass
    # забрать заказ


if __name__ == '__main__':
    pass
