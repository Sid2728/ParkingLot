from typing import List
from models.slotModel import Slot

class SlotRepository:
    def __init__(self):
        self.slots ={
            1: Slot(slotId= "1", isAvailable= False),
            2: Slot(slotId= "2", isAvailable= True)
        }
    
    def getAllAvailableSlots(self) -> List[Slot]:
           return [slot for slot in self.slots.values() if slot.isAvailable]
    