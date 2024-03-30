from random import randint

from create_items import create_items_to_provider


class Provider:  # поставщик

    provider_id = randint(1, 1000)  # пока что реализация такая TODO сделать уникальный id
    items = dict()

    def __init__(self, name, provider_id):
        self.name = name

    def find_item_by_name(self, name):
        for item in self.items.keys():
            if item.name == name:
                return item
        return None

    def send_order(self, request):
        """
        :param request: {item: amount}
        :return: {item: amount}
        """
        order = dict()
        # что если такого товара не существует?
        for key, value in request.items():
            available_amount = self.items[key]
            order[self.items[key]] = available_amount - request[key]
            self.items[key] -= request[key]
        return order

    # send_order - принять и отправить заказ складу

    def update_stocks(self, what_to_update):
        '''
        Обновляет товары, если товара нет, то создает
        :param what_to_update: { item : amount}
        '''
        # что делать когда нет такого товара?
        for key, value in what_to_update.items():
            item = self.find_item_by_name(key)
            if item is not None:
                self.items[item] += value

    # update_stocks - обновить число товаров на складе

    def create_stock(self):
        self.items = create_items_to_provider(self.provider_id)

    def print_all_provider_items(self):
        print(self.items)
        for key, value in self.items.items():
            print(f"Название: {key.name} | Количество: {value}")

