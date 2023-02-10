#!/usr/bin/python3
"""
Module console
contains the Entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    '''

    '''
    prompt = '(hbnb) '
    def do_EOf(self, line):
        '''
        Exit from console
        '''
        print()
        return True
    def do_quit(self, line):
        '''type quit to exit'''
        return True
    def emptyline(self):
        """"""
        pass
    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_instance = line()
            class_instance.save()
            print(class_instance.id)
    
    def do_show(self, line):
        return     

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
