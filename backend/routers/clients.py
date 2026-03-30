from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_db
from schemas.client_schema import ClientUpdate, ClientCreate, ClientResponse
from services import client_service


clients_router = APIRouter(prefix="/clients", tags=["Clients"])


@clients_router.post("/", response_model=ClientResponse, status_code=201)
def create_client(data: ClientCreate, db: Session = Depends(get_db)):
    return client_service.create_client(db, data)


@clients_router.get("/", response_model=list[ClientResponse])
def get_clients(db: Session = Depends(get_db)):
    return client_service.get_clients(db)


@clients_router.get("/{client_id}", response_model=ClientResponse)
def get_by_id(client_id: int, db: Session = Depends(get_db)):
    return client_service.get_by_id(db, client_id)


@clients_router.patch("/{client_id}", response_model=ClientResponse)
def update_client(client_id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    return client_service.update_client(db, client_id, data)


@clients_router.delete("/{client_id}", status_code=204)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client_service.delete_client(db, client_id)
