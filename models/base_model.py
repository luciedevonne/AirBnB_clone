import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Initialize a Basemodel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
