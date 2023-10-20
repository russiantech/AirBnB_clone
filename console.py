#!/usr/bin/python3
<<<<<<< HEAD
""" The HBnB console. """
=======

""" def HBnB console."""

>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
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
<<<<<<< HEAD
    """
    Defines the HolbertonBnB cmd interpreter.

    Attributes:
        prompt (str): command prompt.
=======

    """HolbertonBnB commandline interpreter.

    Attributes:
        prompt (str): Command prompt.
>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
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
<<<<<<< HEAD
        """ Do nothing if empty line is received """
=======

        """ don't do anything when an empty line is received """

>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
        pass

    def default(self, arg):

<<<<<<< HEAD
        """ Default behavior for cmd module for invalid inputs """
=======
        """ default cmd module behaviour when input is invalid"""
>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60

        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
<<<<<<< HEAD
        match = re.search(r"\.", arg)
=======

        match = re.search(r"\.", arg)

>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
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

    def do_quit(self, arg):
<<<<<<< HEAD
        """ Quit command to exit the program. """
=======

        """  exit the program quietly (with this command)"""

>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
        return True

    def do_EOF(self, arg):

<<<<<<< HEAD
        """ EOF signal to exit the program. """

        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>
        Creates a new class instance & print its id.
        """
=======
        """ EOF program exit signal """

        print("")

        return True

    def do_create(self, arg):

        """ 
	use: create <class>
        Create new class instance & print its id.
        """

>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):

<<<<<<< HEAD
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Displays str repr of a class instance of a given id.
        """

=======
        """ 
	use: show <class> <id> or <class>.show(<id>)
        display str repr of a class instance of a given id.
        """
>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):

<<<<<<< HEAD
        """ Usage: destroy <class> <id> or <class>.destroy(<id>)
        Del a class instance of a given id."""

        argl = parse(arg)
        objdict = storage.all()
=======
        """ 
	use: destroy <class> <id> / <class>.destroy(<id>)
        del a class instance of a given id.
	"""

        argl = parse(arg)
        objdict = storage.all()

>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):

<<<<<<< HEAD
        """ Usage: all or all <class> or <class>.all()
        Displays str repr of * instances of a given class.
        If no class is specified, displays * instantiated objects."""
=======
        """
	use: all or all <class> or <class>.all()
        disp. str repr of all instances of a given class.
        If no class is specified, displays * instantiated objects.
	"""
>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60

        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):

<<<<<<< HEAD
        """ Usage: count <class> or <class>.count()
        Retrieves num of instances of a given class."""
=======
        """
	use: count <class> or <class>.count()
        counts/gets the numb of instances of a given class.
	"""
>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60

        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):

<<<<<<< HEAD
        """ Will update a class instance given an id by adding/updating
        a given attribute key/value pair or dict."""
=======
        """
	use: update <class> <id> <attribute_name> <attribute_value> /
       <class>.update(<id>, <attribute_name>, <attribute_value>) /
       <class>.update(<id>, <dictionary>)
        updates a class instance of a given id by adding or updating
        a given key/value pair attr of a dict """
>>>>>>> 19bec6a4bef1f758da54335ef624c8be3dad4c60

        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
