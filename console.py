#!/usr/bin/python3
""" This file imports the cmd module """
import cmd, json
from models import storage
from models.base_model import BaseModel
""" console.py """

classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand method. The console and master driving program """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command. Exits the program
        """
        #print("")
        return True

    def do_EOF(self, line):
        """EOF command. Exits the program
        """
        #print("")
        return True

    def do_create(self, line):
        """ Create command. Creates a new instance, saves to
        JSON file, and prints the id. Must be create BaseModel
        """
        print(line)
        if len(line) is 0:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            line = BaseModel()
            line.save()
            print(line.id)

    def do_show(self, line):
        """ Show command. Displays information based on the
        class name and id, if valid
        """
        if len(line) is 0:
            print("** class name missing **")
            return
        line = line.split(" ")
        if line[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(line) is 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        line = '.'.join(line)
        if line in all_objs.keys():
            my_line = line.split(".")
            print(all_objs[line])
        else:
            print("** no instance found **")


    def do_destroy(self, line):
        if len(line) is 0:
            print("** class name missing **")
            return
        line = line.split(" ")
        if line[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(line) is 1:
            print("** instance id missing **")
            return
        #if value not in line.id:
        #    print("** no instance found **")
        with open('file.json', 'w') as overwrite:
            with open('file.json', 'r') as source:
                for text in source:
                    element = json.loads(text.strip())
                    if line in element:
                        del element[line]
                    overwrite.write(json.dumps(element))

    def do_all(self, line):
        new_list = []
        if len(line) is 0:
            all_inst = storage.all()
            for obj_id in all_inst.keys():
                new_list.append(all_inst[obj_id])
            print(new_list)
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            all_inst = storage.all()
            for obj_id in all_inst.keys():
                check_inst = obj_id.split(".")
                if line == check_inst[0]:
                    new_list.append(all_inst[obj_id])
            print(new_list)

    def do_update(self, line, value, attribute, att_content):
        if len(line) is 0:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        elif len(value) is 0:
            print("** instance id missing **")
        elif value not in line.id:
            print("** no instance found **")
        elif len(attribute) is 0:
            print("** attribute name missing **")
        elif len(att_content) is 0:
            print("** value missing **")
        else:
            print("Will implement later")

if __name__ == '__main__':
    """ Import protection """
    HBNBCommand().cmdloop()
