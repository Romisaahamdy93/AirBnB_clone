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

class HBNBCommand(cmd.Cmd):
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
    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            storage.save()

     def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handles the EOF signal, exits the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

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

     def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, instance_id = arg.split()
            instances = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            print(instances.get(key))
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, instance_id = arg.split()
            instances = models.storage.all()
            key = "{}.{}".format(class_name, instance_id)
            del instances[key]
            models.storage.save()
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        instances = models.storage.all()
        if arg:
            try:
                class_name = eval(arg).__name__
                filtered_instances = {k: v for k, v in instances.items() if class_name in k}
                print([str(v) for v in filtered_instances.values()])
            except NameError:
                print("** class doesn't exist **")
        else:
            print([str(v) for v in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name, instance_id, attribute, value = args[0], args[1], args[2], args[3]
            key = "{}.{}".format(class_name, instance_id)
            instances = models.storage.all()
            instance = instances.get(key)

            if not instance:
                print("** no instance found **")
                return

            if attribute not in dir(instance):
                print("** attribute name missing **")
                return

            setattr(instance, attribute, type(getattr(instance, attribute))(value))
            instance.save()

        except IndexError:
            print("** instance id missing **")
        except ValueError:
            print("** value missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
