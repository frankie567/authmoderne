from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...storage.sqlalchemy import Base


class OAuthClient(Base):
    __tablename__ = "oauth_clients"

    client_id: Mapped[str] = mapped_column(
        String(128), primary_key=True, unique=True, nullable=False
    )
