from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int
    provider_id: int
    store_id: int = 0

    def __key(self):
        return (self.name,self.store_id)

    def __hash__(self):  # делаем hashable чтобы класс можно было использовать в качестве ключа словаря
        return hash(self.__key())
