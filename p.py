# todo:
# this needs to be thrown away and reworked!
# it technically works to send commands, but it has no awareness of
# who is sending the commands, and it doesnt return fuck all to the
# screen, so any errors in commands a user throws go nowhere..
# if someone does this before me, holler!
#
# changelog:
# april 23, 2017
# at a point i never wrote down i hacked this in to work with my BBS..
# it is very messy as you can see, clean it up if you know what you're
# doing, please :)
# dumb commented out bits are left in to display my stupidity :)
#
# may 09, 2016
# tidied things up here and there in a few commits over the past few days
# i neglected to make the script with the minor safety feature of forcing
# any commands to start with SITE.. otherwise any ftp command at all is
# up for being ran, which is not the point of this script
#
# version one:
# may, 05, 2016
# so, super simple thing to log into an ftp, and issue the command you pass
# in the argument

import logging
import random
import time
import os

from x84.bbs import getterminal, get_ini, goto, gosub
from x84.bbs import echo, showart, syncterm_setfont, LineEditor
from x84.bbs import find_user, get_user, User
from x84.bbs import getsession

from ftplib import FTP_TLS

#from sys import argv
#filename, argument = argv

bye_u = ['exit', 'quit', 'bye']
color_primary = 'red'
color_secondary = 'green'
term = getterminal()
max_attempts = 5
max_length = 90

def do_cmd(term):
    session = getsession()
    sep_ok = getattr(term, color_secondary)(u'::')
    sep_bad = getattr(term, color_primary)(u'::')
    colors = {'highlight': getattr(term, color_primary)}
    echo(u'\r\n\r\n i hope you know glftpd cmds :)') # feel free to change these echoes to personalize your installation
    echo(u'\r\n\r\n if you dont, type quit')
    echo(u'\r\n\r\n basically all this is good for at the moment is for msg and request')
    echo (u'\r\n\r\n e.g \'msg kniffy hi\' or \'request coolthing -for:<you>\'')
    for _ in range(max_attempts):
        echo(u'\r\n\r\n{sep} tYPE cMD -> '.format(sep=sep_ok))
        handle = LineEditor(max_length, colors=colors
                            ).read() or u''

        if handle.strip() == u'':
            continue

        # user says goodbye
        if handle.lower() in bye_u:
            return

        else:
            # do cmd
            person = session.user.handle
#            session.user.handle = person
            ftps = FTP_TLS()
            #ftps.set_debuglevel(2)                  # if you broke something, uncomment this (run it directly, not from eggdrop)
            ftps.connect('127.0.0.1', '1234')        # enter your server and port within the quotes
            ftps.login('cmd', '<make this a non-sysop user please>') # enter your user and pass within the quotes (remember, not a user with privs)
#            ftps.login(person, auth)
            ftps.prot_p()

            ftps.sendcmd('site ' + handle)

            echo(u'\r\n\r\n cmd sent')

            ftps.quit()

#            echo(u'\r\n\r\n{sep} Password: '.format(sep=sep_ok))
#            password = LineEditor(password_max_length,
#                                  colors=colors,
#                                  hidden=hidden_char
#                                  ).read() or u''

#            user = authenticate_user(handle, password)
#            if not user:
#                echo(u'\r\n\r\n{sep} Login failed.'.format(sep=sep_bad))
#                continue

#        goto(top_script, handle=user.handle)

#    echo(u'\r\n\r\n{sep} Too many authentication attempts.\r\n'
#         .format(sep=sep_bad))


def main():

    term = getterminal()

    do_cmd(term)


#print "hi :) running cmd.."

#ftps = FTP_TLS()
#ftps.set_debuglevel(2)					# if you broke something, uncomment this (run it directly, not from eggdrop)
#ftps.connect('127.0.0.1', '1234')			# enter your server and port within the quotes
#ftps.login('cmd', 'asdf')			# enter your user and pass within the quotes (remember, not a user with privs)
#ftps.prot_p()

#ftps.sendcmd('site' + argument)

#print "logged in, what cmd do you want to issue?"
#FANCY = raw_input()

#FANCY = raw_input(promt)

#ftps.sendcmd('site ' + FANCY)

# the tcl script i included will take any output from this python and spam
# it into the channel.. set this how you like, or turn it off
# if you're a tcl guru comment this out and make your tcl do the accounce
#print "cmd sent, sleeping now zzzz"

#ftps.quit()

#quit()

