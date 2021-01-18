import uvicorn
import datetime
from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from model import (
    PlaceAvailability,
    PlaceReservationRequest,
    PlaceReservation,
    PlaceReservationState,
    Dossier,
)


# Data for our small world.

place_availability1 = PlaceAvailability(id="A1")

place_availabilities = {}
place_availabilities[place_availability1.id] = place_availability1

dossier1 = Dossier(id="D0", phone="076 562 8114")

place_reservation1 = PlaceReservation(
    id="PR0",
    state=PlaceReservationState.BOOKED,
    creationDate=str(datetime.datetime.now()),
    dossier=dossier1,
)


place_reservations = {}
place_reservations[place_reservation1.id] = place_reservation1


# The API

app = FastAPI(
    description="A small API to Reserve Places.",
    title="API to Reserve Places in an Inventory",
    version="0.0.2",
)


@app.get("/", tags=["version"])
def get_version():
    return {"API to Reserve Places in an Inventory": "v.0.0.2"}


## Place-availabilities


@app.get(
    "/place-availabilities/",
    response_model=List[PlaceAvailability],
    tags=["place-availabilities"],
)
def read_place_availabilities():
    return list(place_availabilities.value())


## Place-reservations


@app.get(
    "/place-reservations/",
    response_model=List[PlaceReservation],
    tags=["place-reservations"],
)
def read_place_reservations():
    return list(place_reservations.values())


@app.get(
    "/place-reservations/{id}",
    response_model=PlaceReservation,
    tags=["place-reservations"],
)
def read_place_reservations(id: str):
    if id in place_reservations:
        return place_reservations[id]
    else:
        return JSONResponse(
            status_code=404, content=f"PlaceReservationId '{id}' not found"
        )


@app.post(
    "/place-reservations/", response_model=PlaceReservation, tags=["place-reservations"]
)
def create_place_reservation(placeReservationRequest: PlaceReservationRequest):
    if not id in place_reservations:
        dossier = Dossier(
            id=f"D2",
            name=placeReservationRequest.name,
            phone=placeReservationRequest.phone,
            date=placeReservationRequest.date,
        )
        placeReservation = PlaceReservation(
            id=f"PR2",
            state=PlaceReservationState.PREBOOKED,
            creationDate=str(datetime.datetime.now()),
            dossier=dossier,
        )
        place_reservations[id] = placeReservation
        return placeReservation
    else:
        return JSONResponse(
            status_code=404, content=f"PlaceReservation with id '{id}' already exists"
        )


@app.patch(
    "/place-reservations/{id}",
    response_model=PlaceReservation,
    tags=["place-reservations"],
)
def patch_place_reservations(id: str):
    if id in place_reservations:
        updated_PlaceReservation = place_reservations[id]
        updated_PlaceReservation.state = PlaceReservationState.BOOKED
        place_reservations[id] = updated_PlaceReservation
        return updated_PlaceReservation
    else:
        return JSONResponse(
            status_code=404, content=f"PlaceReservationId '{id}' not found"
        )


@app.delete("/place-reservations/{id}", tags=["place-reservations"])
def delete_place_reservations(id: str):
    print(str(place_reservations))
    if id in place_reservations:
        del place_reservations[id]
        return JSONResponse(
            status_code=200, content=f"PlaceReservation with id '{id}' deleted"
        )
    else:
        return JSONResponse(
            status_code=404, content=f"PlaceReservationId '{id}' not found"
        )


# Start server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
