#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            class_and_method = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", class_and_method[1])
            if match is not None:
                command = [class_and_method[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_dict.keys():
                    call = "{} {}".format(class_and_method[0], command[1])
                    return command_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        class_name = parse(arg)[0]
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        args = parse(arg)
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        args = parse(arg)
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = parse(arg)
        if args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if args and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif not args:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = parse(arg)
        count = 0
        for obj in storage.all().values():
            if args and args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = parse(arg)
        obj_dict = storage.all()

        if not args or len(args) < 2:
            print("** class name or instance id missing **")
            return False

        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in obj_dict:
            print("** no instance found **")
            return False

        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False

        instance = obj_dict[instance_key]

        if len(args) == 4:
            attribute_name, attribute_value = args[2], args[3]
            setattr(instance, attribute_name, attribute_value)
        elif isinstance(eval(args[2]), dict):
            for key, value in eval(args[2]).items():
                setattr(instance, key, value)

        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
