from app.repository.slotRepository import SlotRepository

def testGetAllAvailableSlots():
    repo = SlotRepository()
    availableSlots = repo.getAllAvailableSlots()
    assert all(slot.isAvailable for slot in availableSlots)
