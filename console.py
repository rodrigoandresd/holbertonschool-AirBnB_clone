#!/usr/bin/python3

"""
Program that contains the entry point of the command interpreter
"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
import cmd
import json


class HBNBCommand(cmd.Cmd):
    """
    Initialization command Interpreter
    """
    model_tags = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]
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
        if args not in self.model_tags:
            print("** class doesn't exist **")
            return

        if args == "BaseModel":
            base = BaseModel()
        if args == "User":
            base = User()
        if args == "State":
            base = State()
        if args == "City":
            base = City()
        if args == "Place":
            base = Place()
        if args == "Amenity":
            base = Amenity()
        if args == "Review":
            base = Review()

        base.save()
        print(base.id)

    def do_show(self, args):
        """command to print the string representation of an instance
            ex: $ show BaseModel 1234-1234-1234
        """
        line_arg = args.split()
        m_name, m_id = line_arg

        if not args:
            print("** class name missing **")
            return
        if m_name not in self.model_tags:
            print("** class doesn't exist **")
            return
        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        base_id = storage.all().get(f"{m_name}.{m_id}")
        if not base_id:
            print("** no instance found **")
            return

        print(base_id)

    def do_destroy(self, args):
        """command to delete instance based on the class name and id"""
        line_arg = args.split()
        m_name, m_id = line_arg

        if not args:
            print("** class name missing **")
            return
        if m_name not in self.model_tags:
            print("** class doesn't exist **")
            return
        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        base_id = storage.all().get(f"{m_name}.{m_id}")
        if not base_id:
            print("** no instance found **")
            return

        del storage.all()[f"{line_arg[0]}.{m_id}"]
        storage.save()

    def do_all(self, name):
        """Print  all string representation of all
        instances based or not on the class name
        """
        storage_ = storage.all()
        if name:
            if name not in self.model_tags:
                print("** class doesn't exist **")
                return

        print([str(value) for key, value in storage_.items()])

    def do_update(self, args):
        """"""
        line_arg = args.split()
        m_name, m_id, name_attr, value_attr = line_arg
        if not args:
            print("** class name missing **")
            return

        if len(line_arg) == 1:
            print("** instance id missing **")
            return

        if len(line_arg) == 2:
            print("** attribute name missing **")
            return

        if len(line_arg) == 3:
            print("** value missing **")
            return

        if m_name not in self.model_tags:
            print("** class doesn't exist **")
            return

        base = storage.all().get(f"{m_name}.{m_id}")
        if not base:
            print("** no instance found **")
            return

        setattr(storage.all()[f"{line_arg[0]}.{m_id}"],
                name_attr, value_attr.strip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
