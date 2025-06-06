from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()


class AttivitaQuery(BaseModel):
    data_da: Optional[str] = None
    data_a: Optional[str] = None
