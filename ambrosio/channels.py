

class Channel(object):
    """Channel class """
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name

class TextChannel(object):
    """ Channel class, reads commands form file"""
    def __init__(self, name):
        super(TextChannel, self).__init__()
        self.messages = []
        with open("messages.txt","r") as f:  #with open, obre i tanca com f.open i f.close ni que hi hagi errors
            for line in f:
                self.messages.append(line)


    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0
        
