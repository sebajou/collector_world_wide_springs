from datetime import date

from beanie import Document
from pydantic import BaseModel


class SpringComposition(Document, BaseModel):
    elementName: str
    formula: str
    quantity: str
    unity: str


class SpringPrice(Document, BaseModel):
    price: int
    money: str
    by: str
    country: str


class SpringLocalisation(Document, BaseModel):
    longitude: int
    lattitude: int


class Spring(Document, BaseModel):
    class Settings:
        name = ("springs")

    id: str
    name: str
    composition: list[SpringComposition]
    description: str
    brand: str
    price: list[SpringPrice]
    localisation: SpringLocalisation
    startExploitationDate: date
