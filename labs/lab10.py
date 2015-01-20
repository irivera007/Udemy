class LogMessage():
    def __init__(self,fi):
        self.fi=fi
    def read(self):
        try:
            archivo = open(self.fi,'r')
            lines = archivo.readlines()
            for i in lines:
                print i
            archivo.close()
        except:
            print ("Error while reading")
    def write(self, message):
        self.message=message
        try:
            archivo2 = open(self.fi,'a')
            archivo2.write(message)
            archivo2.close()
        except:
            print ("Error while writing")

Test= LogMessage("log.txt")

Test.write("\nError 11 added \nError 12 added")
Test.read()
    