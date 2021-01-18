from typing import List
from enum import Enum
from pydantic import BaseModel


class PlaceAvailability(BaseModel):
    id: str


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

    def __eq__(self, other):
        return self.id == other.id


class PlaceReservation(BaseModel):
    id: str
    state: PlaceReservationState
    creationDate: str
    dossier: Dossier

    def __eq__(self, other):
        return self.id == other.id

