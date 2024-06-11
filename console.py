#!/usr/bin/python3
"""Command interpreter for AirBnB project"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '  # Custom prompt for the command interpreter

    def emptyline(self):
        """Empty line behavior"""
        pass  # No action when user inputs an empty line

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True  # Exit the program when the user inputs 'quit'

    def do_EOF(self, arg):
        """End of File command to exit the program"""
        print()  # Print a newline
        return True  # Exit the program when the user inputs EOF (Ctrl+D)

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return  # Print error message if class name is missing
        try:
            new_instance = eval(arg)()  # Create a new instance of the specified class
            new_instance.save()  # Save the new instance
            print(new_instance.id)  # Print the ID of the new instance
        except NameError:
            print("** class doesn't exist **")  # Print error message if class doesn't exist

    def do_show(self, arg):
        """Prints the string representation of an instance based on its ID"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return  # Print error message if class name is missing
        try:
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return  # Print error message if instance ID is missing
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return  # Print error message if instance doesn't exist
        print(storage.all()[key])  # Print the string representation of the instance
    except KeyError:
        print("** class doesn't exist **")  # Print error message if class doesn't exist

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]  # Delete the instance
            storage.save()  # Save changes to JSON file
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print("** class name missing **")
            return  # Print error message if class name is missing
        try:
            class_name = eval(arg).__name__
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return  # Print error message if class doesn't exist
            objs = [str(obj) for obj in storage.classes()[class_name].values()]
            print(objs)
        except NameError:
            print("** class doesn't exist **")  # Print error message if class doesn't exist

    def do_update(self, arg):
        """Updates an instance based on the class name and id with a dictionary"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** dictionary missing **")
                return
            # Convert dictionary string representation to a dictionary object
            dict_str = ' '.join(args[2:])
            update_dict = eval(dict_str)
            obj = storage.all()[key]
            for k, v in update_dict.items():
                if hasattr(obj, k):
                    setattr(obj, k, v)  # Update attribute value
            storage.save()  # Save changes to JSON file
        except KeyError:
            print("** class doesn't exist **")

    def do_count(self, arg):
    """Retrieves the number of instances of a class"""
    if not arg:
        print("** class name missing **")
        return  # Print error message if class name is missing
    try:
        class_name = eval(arg).__name__
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return  # Print error message if class doesn't exist
        count = len(storage.classes()[class_name])
        print(count)
    except NameError:
        print("** class doesn't exist **")  # Print error message if class doesn't exist

#This block ensures that the code is executed only when the script is run directly
#(not when imported as a module). It creates an instance of HBNBCommand 
#and starts the command loop, allowing users to interact with the command interpreter.
if __name__ == '__main__':
    HBNBCommand().cmdloop()
