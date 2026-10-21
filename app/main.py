"""Read/create API for fictional technical-standard references.

This is independent portfolio code, not an adaptation of a corporate system.
"""

import os
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import Base, Norma, make_engine


class NormaCreate(BaseModel):
    codigo: str = Field(min_length=3, max_length=40, pattern=r"^[A-Z0-9][A-Z0-9._-]*$")
    titulo: str = Field(min_length=3, max_length=140)
    revisao: str = Field(min_length=1, max_length=20)
    organismo_emissor: str = Field(min_length=2, max_length=80)

    @field_validator("codigo", mode="before")
    @classmethod
    def normalize_code(cls, value: object) -> object:
        return value.strip().upper() if isinstance(value, str) else value

    @field_validator("titulo", "revisao", "organismo_emissor", mode="before")
    @classmethod
    def trim_text(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value


class NormaRead(NormaCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


def create_app(database_url: str | None = None) -> FastAPI:
    """Application factory allows isolated, repeatable tests with SQLite files."""
    url = database_url or os.getenv("SGQ_DATABASE_URL", "sqlite:///./sgq_portfolio.db")
    engine = make_engine(url)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        Base.metadata.create_all(bind=engine)
        try:
            yield
        finally:
            engine.dispose()

    app = FastAPI(
        title="SGQ Portfolio — Catálogo Fictício",
        description="API demonstrativa independente, sem dados corporativos.",
        version="0.1.0",
        lifespan=lifespan,
    )

    def get_session():
        with Session(engine) as session:
            yield session

    SessionDep = Annotated[Session, Depends(get_session)]

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/normas", response_model=NormaRead, status_code=status.HTTP_201_CREATED)
    def create_norma(data: NormaCreate, session: SessionDep):
        norma = Norma(**data.model_dump())
        session.add(norma)
        try:
            session.commit()
        except IntegrityError as exc:
            session.rollback()
            raise HTTPException(status_code=409, detail="Código já cadastrado") from exc
        session.refresh(norma)
        return norma

    @app.get("/normas", response_model=list[NormaRead])
    def list_normas(
        session: SessionDep,
        limit: Annotated[int, Query(ge=1, le=100)] = 50,
        offset: Annotated[int, Query(ge=0)] = 0,
    ):
        statement = select(Norma).order_by(Norma.codigo, Norma.id).offset(offset).limit(limit)
        return session.scalars(statement).all()

    @app.get("/normas/{codigo}", response_model=NormaRead)
    def get_norma(codigo: str, session: SessionDep):
        normalized = codigo.strip().upper()
        norma = session.scalar(select(Norma).where(Norma.codigo == normalized))
        if norma is None:
            raise HTTPException(status_code=404, detail="Norma não encontrada")
        return norma

    return app


app = create_app()
