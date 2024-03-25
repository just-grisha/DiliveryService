from random import randint

from Item import ItemHandle

ITEMS_NAMES = ["Футбольный мяч", "Чайник", "Холодильник", "Кроссовки", "Шампунь", "Наушники", "Подушка", "Фонарик",
               "Джинсы", "Зонт"]


def create_items_to_provider(provider_id):
    """
    функция генерирует(создает) предметы на складе
    store_id пока что пустой, потому что вызвается до определения склада
    :return: dict: {Item:amount}
    """
    items = dict()
    for item_name in ITEMS_NAMES:
        item = ItemHandle(0, provider_id, item_name, randint(100, 3000))
        items[item] = randint(1, 100)

    return items
