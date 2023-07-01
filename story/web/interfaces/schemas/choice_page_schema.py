from typing import Optional
from interfaces.schemas.choice_schema import Choice
from interfaces.schemas.page_schema import Page


class ChoiceWithPage(Choice):
    page: Optional[Page]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True