#!/usr/bin/env python3
"""Module for HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Handles the End Of File character"""
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

    
