import os

class char:
    """stats = Dex, AC, max HP (just these 3 so far)"""

    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def newchar(self):
        charfile = str(self.name) + '.txt'
        if not os.path.isfile(charfile):
            file = open(self.name + '.txt','a')
            file.write("Name " + str(self.name) + "\nDex " + str(self.stats[0]) + "\nAC " + str(self.stats[1]) + "\nmaxHP " + str(self.stats[2]))
            file.close()
        else:
            print(str(self.name) + " already exists!")

test = char("Joey", [10, 13, 20])
test.newchar()
