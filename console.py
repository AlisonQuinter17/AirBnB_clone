#!/usr/bin/env python3
"""Module for HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter."""
    prompt = "(hbnb) "
    allowed_modules = ["BaseModel"]

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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.

        -  With 'split' tokenize the line to be able to verify
            the existence exclusively of the module (args[0])
            and ignore other arguments if there are any.
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
            else:
                if args[0] == self.allowed_modules[0]:
                    instance = BaseModel()
                    instance.save()
                    print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")
            return

        objs = FileStorage().all()
        if args[0]+"."+args[1] in objs:
            print(objs[args[0] + "." + args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")
            return

        objs = FileStorage().all()
        if args[0]+"."+args[1] in objs:
            del(objs[args[0] + "." + args[1]])
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name."""
        objs = FileStorage().all()

        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return

            fill_list1 = []
            for k, v in objs.items():
                if args[0] in k:
                    fill_list1.append(str(v))
            print(fill_list1)

        else:
            fill_list2 = []
            for v in objs.values():
                fill_list2.append(str(v))
            print(fill_list2)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
