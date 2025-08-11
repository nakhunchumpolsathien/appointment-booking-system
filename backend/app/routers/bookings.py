from fastapi import APIRouter, Depends, HTTPException
from ..deps import get_current_user, admin_required
from ..schemas import BookingCreate, BookingOut, BookingUpdate
from ..storage import add_booking, list_all, list_by_owner, get_booking, delete_booking

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.get("", response_model=list[BookingOut])
def list_bookings(user=Depends(get_current_user)):
    if user.is_admin:
        return [BookingOut(id=b.id, owner=b.owner, slot=b.slot) for b in list_all()]
    return [BookingOut(id=b.id, owner=b.owner, slot=b.slot) for b in list_by_owner(user.username)]

@router.post("", response_model=BookingOut, status_code=201)
def create_booking(payload: BookingCreate, user=Depends(get_current_user)):
    b = add_booking(user.username, payload.slot)
    return BookingOut(id=b.id, owner=b.owner, slot=b.slot)

@router.put("/{booking_id}", response_model=BookingOut)
def update_booking(booking_id: str, payload: BookingUpdate, user=Depends(get_current_user)):
    b = get_booking(booking_id)
    if not b:
        raise HTTPException(status_code=404, detail="Not found")
    if not user.is_admin and b.owner != user.username:
        raise HTTPException(status_code=403, detail="Forbidden")
    b.slot = payload.slot
    return BookingOut(id=b.id, owner=b.owner, slot=b.slot)

@router.delete("/{booking_id}", status_code=204)
def delete(booking_id: str, user=Depends(get_current_user)):
    b = get_booking(booking_id)
    if not b:
        return
    if not user.is_admin and b.owner != user.username:
        raise HTTPException(status_code=403, detail="Forbidden")
    delete_booking(booking_id)

@router.get("/admin/all", response_model=list[BookingOut], dependencies=[Depends(admin_required)])
def admin_all():
    return [BookingOut(id=b.id, owner=b.owner, slot=b.slot) for b in list_all()]
