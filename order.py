from dataclasses import dataclass
from datetime import datetime
from Item import Item
from workers import Storekeeper, Courier

from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from Item import Item
from workers import Storekeeper, Courier

@dataclass
class Order:
    id: int
    status: str
    order_items: Dict[Item, int]
    create_order_time: datetime
    delivery_order_time: datetime
    storekeeper: Storekeeper
    courier: Courier
