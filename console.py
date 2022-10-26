#!/usr/bin/python3

"""
Program that contains the entry point of the command interpreter
"""
from models.base_model import BaseModel
from models import storage
import cmd
import json


class HBNBCommand(cmd.Cmd):
    """

    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """command to exit program"""
        return True

    def do_EOF(self, args):
        """End of File, exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, args):
        """Create command to create an instance"""
        if not args:
            print("** class name missing **")
            return
        if args != "BaseModel":
            print("** class doesn't exist **")
            return

        base = BaseModel()
        base.save()
        print(base.id)

    def do_show(self, args):
        """"""        
        if not args:
            print("** class name missing **")
            return
        if args != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
