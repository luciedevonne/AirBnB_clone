import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class for AirBnB objects."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance"""
        if kwargs:  # Check if kwargs (keyword arguments) exist
            for key, value in kwargs.items():  
                if key == 'created_at' or key == 'updated_at': 
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')  # Convert string to datetime object
                elif key != '__class__':  
                    setattr(self, key, value)  # Set attribute with key and value
            if 'id' not in kwargs:  
                self.id = str(uuid.uuid4())  # Generate unique identifier and convert to string
            if 'created_at' not in kwargs:  
                self.created_at = self.updated_at = datetime.now()  # Set created_at and updated_at to current datetime
        else:  # If kwargs is empty
            self.id = str(uuid.uuid4())  # Generate unique identifier and convert to string
            self.created_at = self.updated_at = datetime.now()  # Set created_at and updated_at to current datetime

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__) # Format string with class name, id, and attributes

    def save(self):
        """Update updated_at attribute with current datetime."""
        self.updated_at = datetime.now()  # Update updated_at to current datetime

    def to_dict(self):
        """Return dictionary representation of BaseModel instance."""
        new_dict = self.__dict__.copy()  # Copy instance dictionary
        new_dict['__class__'] = type(self).__name__  # Add class name to dictionary
        new_dict['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format string
        new_dict['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format string
        return new_dict  # Return dictionary
