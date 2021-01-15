from typing import List
from enum import Enum
from pydantic import BaseModel


class PlaceReservationRequest(BaseModel):
    name: str
    phone: str
    date: str


class PlaceReservationState(str, Enum):
    PREBOOKED = "PREBOOKED"
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"


class Dossier(BaseModel):
    id: str
    phone: str


class PlaceReservation(BaseModel):
    id: str
    state: PlaceReservationState
    creationDate: str
    dossier: Dossier
