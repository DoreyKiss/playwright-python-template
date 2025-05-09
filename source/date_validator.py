from datetime import datetime
from typing import Annotated

from pydantic import AfterValidator, BaseModel


def is_valid_date(date_str: str) -> str:
    # parese strptime time es format time strftime.

    my_date = datetime.strptime(date_str, "%Y-%m-%d")
    if my_date.year < 1920 or my_date.year > datetime.now().year:
        raise ValueError(f"Year out of range: {date_str}")
    return date_str


class MyDate(BaseModel):
    dateInput: Annotated[str, AfterValidator(is_valid_date)] = "2023-10-01"
