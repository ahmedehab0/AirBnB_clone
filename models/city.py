"""city module"""


import models
from models.base_model import BaseModel


class City(BaseModel):
    """city class"""

    state_id = ""
    name = ""
