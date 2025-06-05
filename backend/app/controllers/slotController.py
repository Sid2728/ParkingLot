from fastapi import APIRouter
from repository.slotRepository import SlotRepository
from models.slotModel import Slot
from typing import List

router = APIRouter()
repo = SlotRepository()

@router.get("/slots", response_model=List[Slot])
def get_available_slots():
    return repo.getAllAvailableSlots()
