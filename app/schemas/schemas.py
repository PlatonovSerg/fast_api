from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class EduLevel(str, Enum):
    SECONDARY = "Среднее образование"
    SPECIAL = "Средне специальное образование"
    HIGHER = "Высшее образование"


class Person(BaseModel):
    name: str = Field(..., max_length=20)
    surname: str | list[str] = Field(..., max_length=50)
    age: Optional[int] = Field(..., gt=4, le=99)
    is_staf: bool = Field(False, alias="is-stuff")
    education_level: Optional[EduLevel]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Ivan",
                    "surname": "Ivanov",
                    "age": 35,
                    "is_stuf": False,
                    "education_level": "Среднее образование",
                },
                {
                    "name": "Petr",
                    "surname": "Petrov",
                    "age": 50,
                    "is_stuf": True,
                    "education_level": "Среднее образование",
                },
            ]
        },
        "title": "Class for greetings",
        "str_min_length": 2,
    }

    @field_validator("name")
    def name_cant_be_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError("Имя не может состоять из цифр")
        return value
