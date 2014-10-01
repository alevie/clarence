#! /usr/env python
# Purpose:        Provide a continuous text-to-speech prompt for espeak
# Requirements:   Python standard libraries

import cmd
import os
import subprocess
import sys


class CLI(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.prompt = 'Clarence> '

  def do_exit(self, line):
    print 'Goodbye!'
    return True

  def do_intro(self, line):
    self.say('Hello. My name is Clarence.')

  def do_version(self, line):
    self.say('I am Clarence 2.0')

  def default(self,line=''):
    self.say(line)

  def say(self,line):
    line = line.lower()
    line = line.replace('adalyn','addalynn') # Use these lines to correct pronunciation
    args = ['espeak', '-v', 'en-us', '-a', '200', '-s', '150', '"%s"' % line]
    subprocess.call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def which(program):
  # Checks to see if function exists
  def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
  fpath, fname = os.path.split(program)
  if fpath:
    if is_exe(program):
      return program
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      path = path.strip('"')
      exe_file = os.path.join(path, program)
      if is_exe(exe_file):
        return exe_file
  return None


def main():
  os.system('clear')
  # Check if espeak is installed
  if which('espeak') is None:
    sys.exit('espeak is not installed')
  # Ensure script is run as root
  if not os.geteuid() == 0:
    sys.exit('Script must be run as root')
  try:
    foo = CLI()
    foo.cmdloop()
  except: #catch ctrl-c event to exit
    pass


if __name__ == '__main__':
  main()
  
