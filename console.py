#!/usr/bin/python3
"""Command interpreter for AirBnB project"""
import cmd
from models.base_model import BaseModel
from models import storage

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
        """EOF command to exit the program"""
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
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return  # Print error message if class name is missing
        args = arg.split()
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
            return  # Print error message if class name is missing
        args = arg.split()
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
            del storage.all()[key]  # Delete the instance
            storage.save()  # Save changes to JSON file
        except KeyError:
            print("** class doesn't exist **")  # Print error message if class doesn't exist

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = []
        if not arg:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)  # Print string representations of all instances
            return
        try:
            class_name = eval(arg).__name__
            for obj in storage.all().values():
                if type(obj).__name__ == class_name:
                    objs.append(str(obj))
            print(objs)  # Print string representations of instances of specified class
        except NameError:
            print("** class doesn't exist **")  # Print error message if class doesn't exist

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return  # Print error message if class name is missing
        args = arg.split()
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
            if len(args) < 3:
                print("** attribute name missing **")
                return  # Print error message if attribute name is missing
            if len(args) < 4:
                print("** value missing **")
                return  # Print error message if value is missing
            attr_name = args[2]
            attr_value = args[3]
            obj = storage.all()[key]
            setattr(obj, attr_name, attr_value)  # Update attribute value
            storage.save()  # Save changes to JSON file
        except KeyError:
            print("** class doesn't exist **")  # Print error message if class doesn't exist

#This block ensures that the code is executed only when the script is run directly
#(not when imported as a module). It creates an instance of HBNBCommand 
#and starts the command loop, allowing users to interact with the command interpreter.
if __name__ == '__main__':
    HBNBCommand().cmdloop()
