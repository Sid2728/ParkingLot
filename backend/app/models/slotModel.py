from pydantic import BaseModel

class Slot(BaseModel):
    slotId : str
    isAvailable: bool