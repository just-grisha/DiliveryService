from dataclasses import dataclass, asdict


@dataclass
class Item:
    name: str
    price: int


@dataclass
class ProviderItem(Item):
    provider_id: int

    def __key(self):
        return (self.name, self.provider_id)

    def __hash__(self):  # делаем hashable чтобы класс можно было использовать в качестве ключа словаря
        return hash(self.__key())


@dataclass
class StoreItem:
    item: Item
    Store_id: int
