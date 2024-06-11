from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)  # Call the superclass constructor
        self.email = ""  # Initialize email attribute
        self.password = ""  # Initialize password attribute
        self.first_name = ""  # Initialize first_name attribute
        self.last_name = ""  # Initialize last_name attribute

    def __str__(self):
        """Return string representation of User instance"""
        return "[User] ({}) {}".format(self.id, self.__dict__)  # Format string with class name, id, and attributes
