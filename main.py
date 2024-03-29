from dataclasses import dataclass, asdict
from datetime import time

from create_items import create_items_to_provider
from Item import Item
from random import randint

# DONE
# Что должно быть? Id внутри системы складов, id внутри системы поставщика, название, себестоимость


# DONE


class Provider:  # поставщик

    provider_id = randint(1,1000) # пока что реализация такая #TODO сделать уникальный id
    items = dict()
    def __init__(self, name, provider_id):
        self.name = name

    def send_order(self, request):
        """
        :param request:
        :return: [{item: amount},{item: amount}...]
        """

    # send_order - принять и отправить заказ складу

    @classmethod
    def update_stocks(cls,what_to_update):
        '''
        Обновляет товары, если товара нет, то создает
        :param what_to_update: { item : amount}
        '''



    # update_stocks - обновить число товаров на складе

    @classmethod
    def create_stock(cls):
        cls.items = create_items_to_provider(cls.provider_id)

    @classmethod
    def print_all_provider_items(cls):
        print(cls.items)
        for key, value in cls.items.items():
            print(f"Название: {key.name} | Количество: {value}")


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
    items: [Item]
    create_order_time: time
    delivery_order_time: time
    storekeeper: Storekeeper
    courier: Courier


class OrderHandle:
    def __init__(self, status: str, items: [Item], create_order_time: time, delivery_order_time: time,
                 storekeeper: Storekeeper, courier: Courier):
        self.item = Order(status, items, create_order_time, delivery_order_time, storekeeper, courier)

    def get_order(self):
        return asdict(self.item)

    def change_order(self, key, val):
        self.item.__dict__[key] = val


# Что находится в заказе? Статус доставки, список товаров, время создания-время доставки, кто собирал-доставлял


class User:
    def make_order(self):
        # get_order_data_from_user()
        pass

    # сделать заказ

    def take_order(self):
        pass
    # забрать заказ


if __name__ == '__main__':
    provider1 = Provider("Поставщик1", 77)
    provider1.create_stock()
    provider1.print_all_provider_items()
    what_to_update = [{"Чайник":5000}]
    provider1.update_stocks(what_to_update)
    provider1.print_all_provider_items()