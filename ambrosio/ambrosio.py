#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from commandlist import Commandlist
import channels as ch
import action as ac


class Ambrosio(object):

    """Class for Ambrosio Personal Digital Butler


    will run or house"""
    def __init__(self):
        super(Ambrosio, self).__init__()
        self.c1 = Commandlist()
        self.channels = []
        self.channels.append(ch.TextChannel())

        self.actions = []
        self.actions.append(ac.MusicPlayer())


    def next_command(self):
        try:
            return self.c1.next()
        except:
            return None
    def update_channels(self):
        for Chan in self.channels:
            while chan.msg_avail():
                self.c1.append(chan.get_msg())


    def execute_command(self, command):
        print "Will execute", command


    def mainloop(self):
        # while True:
        # command = get_command
        # do_command(command)
        # update
        while True:
            command = self.next_command()
            if command:
                self.execute_command(command)
            time.sleep(1)
            self.update_channels()


if __name__ = "__main__";
    amb =  Ambrosio()
    amb.mainloop()
