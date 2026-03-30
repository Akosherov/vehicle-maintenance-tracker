from sqlalchemy.orm import Session
from sqlalchemy import select

from common.exceptions import ConflictError, NotFoundError
from data.models import Client
from schemas.client_schema import ClientUpdate, ClientCreate


def create_client(db: Session, data: ClientCreate) -> Client:
    if data.email:
        existing = db.scalars(select(Client).where(Client.email == data.email)).first()
        if existing:
            raise ConflictError("A client with that email already exists")
    client = Client(**data.model_dump())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def get_clients(db: Session) -> list[Client]:
    return list(db.scalars(select(Client)).all())


def get_by_id(db: Session, client_id: int) -> Client:
    client = db.scalars(select(Client).where(Client.id == client_id)).first()
    if not client:
        raise NotFoundError(f"Client with ID {client_id} not found")
    return client


def update_client(db: Session, client_id: int, data: ClientUpdate) -> Client:
    client = get_by_id(db, client_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(client, field, value)
    db.commit()
    db.refresh(client)
    return client


def delete_client(db: Session, client_id: int) -> None:
    client = get_by_id(db, client_id)
    db.delete(client)
    db.commit()
