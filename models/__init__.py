from models.engine.file_storage import FileStorage  

# Create a unique FileStorage instance for the application
storage = FileStorage()

# Call reload() method on the storage variable to load data from JSON file
storage.reload()
