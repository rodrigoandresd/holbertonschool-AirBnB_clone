#!/usr/bin/python3

"""
Program that contains the entry point of the command interpreter
"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
