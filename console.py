#!/usr/bin/env python3
"""Module for HBNBCommand class."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter."""
    prompt = "(hbnb) "
    allowed_modules = ["BaseModel", "User", "State", "City",
                       "Amenity", "Place", "Review"]

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
                elif args[0] == self.allowed_modules[1]:
                    instance = User()
                elif args[0] == self.allowed_modules[2]:
                    instance = State()
                elif args[0] == self.allowed_modules[3]:
                    instance = City()
                elif args[0] == self.allowed_modules[4]:
                    instance = Amenity()
                elif args[0] == self.allowed_modules[5]:
                    instance = Place()
                elif args[0] == self.allowed_modules[6]:
                    instance = Review()
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
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
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

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file).
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return

            objs = FileStorage().all()
            instance = args[0] + "." + args[1]
            if instance in objs:

                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return

                if '"' in args[3]:
                    modification = args[3].replace('"', '')
                    the_object = objs[args[0] + "." + args[1]]
                    attribute = args[2]
                    value = modification

                    setattr(the_object, attribute, value)
                    objs[instance].save()
            else:
                print("** no instance found **")
        else:
            print('** class name missing **')
            return

    def default(self, line):
        """
        Retrieve all instances of a class by using: <class name>.all().
        """
        args = line.split('.')

        if len(args) >= 2:
            if args[1][:3] == "all":
                self.do_all(args[0])

            if args[1][:5] == "count":
                self.do_count(args[0])

            if args[1][:4] == "show":
                token = args[1].split('(')
                if len(token) >= 2:
                    self.do_show(args[0] + ' ' + token[1][1:-2])
                else:
                    print("** no instance found **")

            if args[1][:7] == "destroy":
                token = args[1].split('(')
                if len(token) >= 2:
                    self.do_destroy(args[0] + ' ' + token[1][1:-2])
                else:
                    print("** no instance found **")
        else:
            cmd.Cmd.default(self, args)

    def do_count(self, line):
        """
        Retrieve the number of instances of a class: <class name>.count().
        """
        if line:
            objs = FileStorage().all()
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            elif not args[0]:
                print("** class name missing **")
                return
            else:
                container = []
                for k in objs:
                    if k.startswith(args[0]):
                        container += [k]
                print(len(container))
        else:
            print('** class name missing **')

if __name__ == "__main__":
    HBNBCommand().cmdloop()
