"""Persistence models for the public, synthetic catalogue."""

from sqlalchemy import String, UniqueConstraint, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Norma(Base):
    __tablename__ = "normas"
    __table_args__ = (UniqueConstraint("codigo", name="uq_normas_codigo"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codigo: Mapped[str] = mapped_column(String(40), nullable=False)
    titulo: Mapped[str] = mapped_column(String(140), nullable=False)
    revisao: Mapped[str] = mapped_column(String(20), nullable=False)
    organismo_emissor: Mapped[str] = mapped_column(String(80), nullable=False)


def make_engine(database_url: str):
    """Restrict this first portfolio increment to a local SQLite database."""
    if not database_url.startswith("sqlite:///"):
        raise ValueError("Esta demonstração suporta apenas URLs sqlite:/// locais")
    return create_engine(database_url, connect_args={"check_same_thread": False})
