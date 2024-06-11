import json  

class FileStorage:
    """Serializing/deserializing AirBnB objects to/from JSON file."""
    
    __file_path = "file.json"  # File path for JSON file
    __objects = {}  #Dictionary to store class object.id eg (BaseModel object with id=1, the key will be BaseModel.1)

    def all(self):
        """Return dictionary of all objects."""
        return self.__objects  # Return dictionary of objects

    def new(self, obj):
        """Add new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)  # Generate key for object
        self.__objects[key] = obj  # Add object to dictionary with key

    def save(self):
        """Serialize __objects to JSON file."""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}  # Create dictionary of serialized objects
        with open(self.__file_path, 'w') as f:  # Open file in write mode
            json.dump(serialized_objs, f)  # Write serialized objects to file

    def reload(self):
        """Deserialize JSON file to __objects."""
        try:  # Try to execute the following code
            with open(self.__file_path, 'r') as f:  # Open file in read mode
                loaded_objs = json.load(f)  # Load objects from file
            for key, obj_dict in loaded_objs.items():  # Iterate over loaded objects
                class_name = obj_dict['__class__']  # Get class name from object dict
                del obj_dict['__class__']  # Remove '__class__' key from object dict
                self.__objects[key] = globals()[class_name](**obj_dict)  # Create object instance and add to dictionary
        except FileNotFoundError:  # If file not found
            pass  # Continue execution without raising exception
