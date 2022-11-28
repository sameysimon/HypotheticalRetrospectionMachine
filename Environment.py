import json
import io

class Environment:
    def __init__(self):
        self.Model = {}

    def readFile(self, file):
        with io.open(file) as data_file:
            self.Model = json.load(data_file)

    def writeFile(self, fileName):
        with io.open(file=fileName, mode='w') as file:
            json.dump(self.Model, file)



