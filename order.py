from dataclasses import dataclass
from datetime import time

from Item import Item
from main import Storekeeper, Courier


@dataclass
class Order:
    status: str
    items: {Item: int}
    create_order_time: time
    delivery_order_time: time
    storekeeper: Storekeeper
    courier: Courier
