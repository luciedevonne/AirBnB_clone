#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

#This block ensures that the code is executed only when the script is run directly
#(not when imported as a module). It creates an instance of HBNBCommand 
#and starts the command loop, allowing users to interact with the command interpreter.
if __name__ == '__main__':
    HBNBCommand().cmdloop()
