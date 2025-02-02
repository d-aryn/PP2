class strw:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Please input a text: ")
    
    def printString(self):
        print(self.text.upper())

text = strw()
text.getString()
text.printString()