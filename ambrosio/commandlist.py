

class commandlist(object):

    def __init__(self):
        super(commandlist, self).__init__()
        self.commands = []

    def next(self):
        return self.commands.pop(0)

    def append(self, command):
        self.commands.append(command)

    def length(self):
        pass
