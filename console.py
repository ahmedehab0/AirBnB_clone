#!/usr/bin/python3

"""console module for the airbnb"""


from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    """command interpeter"""
    
    prompt = '(hbnb) '

    def do_create(self, obj):
        if obj:
            if obj == "BaseModel":
                instance = BaseModel()
                print(instance.id)
                instance.save()
        else:
            print("** class is missing **")

        """creates a new instance of a class 
        if obj:
            obj_dict = {"BaseModel" : BaseModel,
                        "User" : User,
                        "State" : State,
                        "Amenity" : Amenity,
                        "Place" : Place,
                        "Review" : Review}

            for key, value in obj_dict.items():
                if key == obj:
                    class_obj = value
                    break
            if class_obj is None:
                print("** class doesn't exist **")
            else:
                instance = class_obj()
                print(instance.id)
                instance.save()
        else:
            print("** class name missing **")"""

    def emptyline(self):
        """print empty line\n"""
        pass

    def do_EOF(self, line):
        """signal for ending the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
