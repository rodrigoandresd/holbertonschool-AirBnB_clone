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

    def do_all(self, name):
        """Print  all string representation of all
        instances based or not on the class name
        """
        storage_ = storage.all()
        if name:
            if name != "BaseModel":
                print("** class doesn't exist **")
                return

        print([str(value) for key, value in storage_.items()])

    def do_update(self, args):
        """"""
        line_arg = args.split()

        if not args:
            print("** class name missing **")
            return

        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        if len(line_arg) == 2:
            print("** attribute name missing")
            return

        if len(line_arg) == 3:
            print("** value missing **")
            return

        (m_name, m_id, name_attr, value_attr) = line_arg
        if m_name != BaseModel:
            print("** class doesn't exist **")
            return

        base = storage.all().get(f"{m_name}.{m_id}")
        if not base:
            print("** no instance found **")
            return

        storage_ = storage.all()
        storage_.__setitem__()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
