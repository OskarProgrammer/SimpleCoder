import os as system
from time import sleep

def check(filename:str)->bool:
    if system.path.exists(filename):
        return True
    else:
        return False
    
class FileOpener:

    def __init__ (self,filename):
        self.filename = filename
        
    def open(self):
        if check (self.filename):
            print("File found")
        else:
            print("File does not exist ")
            raise FileExistsError
        self.file  = open(self.filename,"r")
        print("File opened successfully ")
        return self.file
    
    def read(self):
        lista = [line for line in self.file]
        if len(lista)==0:
            return " No data in file "
        return lista
    
    def clear(self):
        self.file.close()
        self.file = open(self.filename,"w").close()
        self.file = open(self.filename,"a")
        return self.file

    def write(self,string):
        self.file.write(string)

    def close (self,*args):
        print("File closed successfully")
        self.file.close()

# -----------------------------------------------------------------------------------------


class Coder:

    def __init__ (self,filename):

        self.filename = filename

        self.plik = FileOpener(self.filename)

        self.plik.open()

    def read(self):

        print("Reading the file...")
        self.data = self.plik.read()
        print("Reading finished...")
    
    def coding(self):
        print("Clearing the file...")

        self.plik.clear()
        
        print("Clearing finished")
        
        
        print("Coding the file...")

        final = []

        for i in range(0,len(self.data)):
            coded = [str(ord(self.data[i][z])) for z in range(0,len(self.data[i]))]
            string = ' '.join(coded)
            final.append(string)
            final.append("\n")
        
        data_changed = ''.join(final)
        self.plik.write(data_changed)

        print("Coding finished")

        
    def exit(self):
        self.plik.close()

        


    