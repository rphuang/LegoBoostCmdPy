import time
from IotLib.log import Log
from IotLib.config import Config
from IotLib.pyUtils import timestamp
from LegoLib.boostCommandBot import BoostCommandBot

class BoostCmd(object):
    """ class to control Lego Boost with input commands or file """

    def __init__(self, boostConfig, camera=None):
        self.bot = BoostCommandBot('Boost', parent=None, camera=None, config=boostConfig)

    def run(self):
        time.sleep(1)
        while True:
            try:
                msg0 = input("command? ");
                if not msg0:
                    Log.info ('bye ...')
                    break
                if not self._executeCommand(msg0):
                    break
            except KeyboardInterrupt:
                Log.info ('KeyboardInterrupt  . . .\n')
                break

        try:
            Log.info('Stopping bot ')
            self.bot.shutOff()
        except:
            pass

    def _help(self):
        print ('Control Lego Boost with command line or text file contains commands. Available commands:')
        print ('  0 - stop')
        print ('  i - forward')
        print ('  m - back')
        print ('  k - right')
        print ('  j - left')
        print ('  motorAB  - run both A B motors at specified speed')
        print ('  motorA   - run motor A at specified speed')
        print ('  motorB   - run motor B at specified speed')
        print ('  motorExt - run motor Ext at specified speed')
        print ('  start    - connect and start up (initialize) Lego Boost')
        print ('  shutoff  - shut off the Lego Boost')
        print ('  run      - load and execute commands from file (default: boostCommand.txt)')
        print ('  sleep    - sleep in seconds (default: 1.0)')
        print ('  help     - print this help menu')
        print ('Examples:')
        print ('  motorAB 100 - run both A B motors at full speed')
        print ('  motorAB.pos 200 - run both A B motors to position 200')
        print ('  motorAB 100,50  - run motor A at speed 100, motor B at speed 50')
        print ('  run testCmds.txt - load and execute commands from testCmds.txt')

    def _doCommandFromFile(self, fileName):
        ''' load commands from file and send to the bot '''
        Log.action('Loading command file: %s' %fileName)
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line) == 0:
                    pass
                elif '#' == line[0]:
                    pass
                else:
                    self._executeCommand(line)

    def _executeCommand(self, cmdstr):
        ''' execute the command str. returns False to quit '''
        msg = cmdstr.lower()
        if 'end' in msg or '2' == msg:
            Log.info ('bye ...')
            return False
        try:
            if 'i' == msg or 'forward' == msg:
                value = int(getValue(cmdstr, 90))
                self.bot.forward(value)
            elif 'm' == msg or 'back' == msg:
                value = int(getValue(cmdstr, 90))
                self.bot.backward(value)
            elif 'k' == msg or 'right' == msg:
                value = int(getValue(cmdstr, 45))
                self.bot.turnRight(value)
            elif 'j' == msg or 'left' == msg:
                value = int(getValue(cmdstr, 45))
                self.bot.turnLeft(value)
            elif '0' == msg or 'stop' == msg:
                self.bot.stop()
            elif 'start' == msg:
                self.bot.connectAndStartUp()
            elif 'shutoff' == msg:
                self.bot.shutOff()
            elif '?' == msg or 'help' == msg:
                self._help()
            elif 'sleep' in msg:
                value = float(getValue(cmdstr, 1.0))
                Log.info('Sleeping %f seconds ...' %value)
                time.sleep(value)
            elif 'run' in msg or 'load' in msg:
                self._doCommandFromFile(getValue(cmdstr, 'botCommands.txt'))
            else:
                cmd, value = getCmdAndValue(cmdstr)
                self.bot.doCommand(cmd, value)
            return True
        except Exception as e:
            Log.error (str(e))
            return False

def getCmdAndValue(cmdstr):
    ''' get both command and value from the str '''
    try:
        cmd, value = cmdstr.split(' ')
        return (cmd, value)
    except:
        return (cmdstr, '')

def getValue(cmdstr, default):
    ''' get the command value from the str '''
    try:
        cmd, value = cmdstr.split(' ')
        return value
    except:
        return default

if __name__ == '__main__':
    boostConfig = Config('boostconfig.txt', autoSave=True)
    cmd = BoostCmd(boostConfig)
    cmd.run()
