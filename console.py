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
        """command to print the string representation of an instance
            ex: $ show BaseModel 1234-1234-1234
        """
        line_arg = args.split()

        if not args:
            print("** class name missing **")
            return
        if line_arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        (name, m_id) = line_arg
        base_id = storage.all().get(f"{name}.{m_id}")
        if not base_id:
            print("** no instance found **")
            return

        print(base_id)

    def do_destroy(self, args):
        """command to delete instance based on the class name and id"""
        line_arg = args.split()

        if not args:
            print("** class name missing **")
            return
        if line_arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        (name, m_id) = line_arg
        base_id = storage.all().get(f"{name}.{m_id}")
        if not base_id:
            print("** no instance found **")
            return

        del storage.all()[f"{name}.{m_id}"]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
