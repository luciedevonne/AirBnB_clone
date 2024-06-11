from models.base_model import BaseModel

class Review(BaseModel):
    """Review class for AirBnB objects."""
    place_id = ""
    user_id = ""
    text = ""