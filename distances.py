import random
import time
import numpy as np


def findKeyDistances(map):
    line1 = map[0] 
    line2 = map[1]
    line3 = map[2]
    distances = {
                                        #qa
        line1[0]+line2[0] : 1.032,
        line2[0]+line1[0] : 1.032,
        #az
        line2[0]+line3[0] : 1.118,
        line3[0]+line2[0] : 1.118,
        #qz
        line1[0]+line3[0] : 2.138,
        line3[0]+line1[0] : 2.138,

                                        #ws
        line1[1]+line2[1] : 1.032,
        line2[1]+line1[1] : 1.032,
        #sx
        line2[1]+line3[1] : 1.118,
        line3[1]+line2[1] : 1.118,
        #wx
        line1[1]+line3[1] : 2.138,
        line3[1]+line1[1] : 2.138,

                                        #ed
        line1[2]+line2[2] : 1.032,
        line2[2]+line1[2] : 1.032,
        #dc
        line2[2]+line3[2] : 1.118,
        line3[2]+line2[2] : 1.118,
        #ec
        line1[2]+line3[2] : 2.138,
        line3[2]+line1[2] : 2.138,

                                        #f
        #fr
        line1[3]+line2[3] : 1.032,
        line2[3]+line1[3] : 1.032,
        #fv
        line2[3]+line3[3] : 1.118,
        line3[3]+line2[3] : 1.118,
        #ft
        line2[3]+line1[4] : 1.247,
        line1[4]+line2[3] : 1.247,
        #fg
        line2[3]+line2[4] : 1,
        line2[4]+line2[3] : 1,
        #fb
        line2[3]+line3[4] : 1.803,
        line3[4]+line2[3] : 1.803,
                                        #r
        #rt
        line1[3]+line1[4] : 1,
        line1[4]+line1[3] : 1,
        #rg
        line1[3]+line2[4] : 1.605,
        line2[4]+line1[3] : 1.605,
        #rb
        line1[3]+line3[4] : 2.661,
        line3[4]+line1[3] : 2.661,
        #rv
        line1[3]+line3[3] : 2.138,
        line3[3]+line1[3] : 2.138,
                                        #t
        #tg
        line1[4]+line2[4] : 1.032,
        line2[4]+line1[4] : 1.032,
        #tb
        line1[4]+line3[4] : 2.138,
        line3[4]+line1[4] : 2.138,
        #tv
        line1[4]+line3[3] : 1.032,
        line3[3]+line1[4] : 1.032,
                                        #g
        #gb
        line2[4]+line3[4] : 1.118,
        line3[4]+line2[4] : 1.118,
        #gv 
        line2[4]+line3[3] : 1.118,
        line3[3]+line2[4] : 1.118,
                                        #b
        #bv
        line3[4]+line3[3] : 1,
        line3[3]+line3[4] : 1,

        #left hand

                                        #j
        #ju
        line2[6]+line1[6] : 1.032,
        line1[6]+line2[6] : 1.032,
        #jy
        line2[6]+line1[5] : 1.605,
        line1[5]+line2[6] : 1.605,
        #jh
        line2[6]+line2[5] : 1,
        line2[5]+line2[6] : 1,
        #jn
        line2[6]+line3[5] : 1.118,
        line3[5]+line2[6] : 1.118,
        #jm
        line2[6]+line3[6] : 1.118,
        line3[6]+line2[6] : 1.118,
                                        #u
        #uy
        line1[5]+line1[6] : 1,
        line1[6]+line1[5] : 1,
        #uh
        line2[5]+line1[6] : 1.247,
        line1[6]+line2[5] : 1.247,
        #un
        line3[5]+line1[6] : 2.015,
        line1[6]+line3[5] : 2.015,
        #um
        line3[6]+line1[6] : 2.138,
        line1[6]+line3[6] : 2.138,
                                        #y
        #yh
        line1[5]+line2[5] : 1.032,
        line2[5]+line1[5] : 1.032,
        #yn
        line1[5]+line3[5] : 2.138,
        line3[5]+line1[5] : 2.138,
        #ym
        line1[5]+line3[6] : 2.661,
        line3[6]+line1[5] : 2.661,
                                        #h
        #hn
        line2[5]+line3[5] : 1.118,
        line3[5]+line2[5] : 1.118,
        #hm
        line2[5]+line3[6] : 1.803,
        line3[6]+line2[5] : 1.803,
                                        #n
        #nm
        line3[5]+line3[6] : 1,
        line3[6]+line3[5] : 1,

                                        #ki
        line2[7]+line1[7] : 1.032,
        line1[7]+line2[7] : 1.032,
        #k,
        line2[7]+line3[7] : 1.118,
        line3[7]+line2[7] : 1.118,
        #i,
        line1[7]+line3[7] : 2.138,
        line3[7]+line1[7] : 2.138,
                                        #lo
        line2[8]+line1[8] : 1.032,
        line1[8]+line2[8] : 1.032,
        #l.
        line2[8]+line3[8] : 1.118,
        line3[8]+line2[8] : 1.118,
        #o.
        line1[8]+line3[8] : 2.138,
        line3[8]+line1[8] : 2.138,
                                        #;p
        line2[9]+line1[9] : 1.032,
        line1[9]+line2[9] : 1.032,
        #;/
        line2[9]+line3[9] : 1.118,
        line3[9]+line2[9] : 1.118,
        #p/
        line1[9]+line3[9] : 2.138,
        line3[9]+line1[9] : 2.138,
     }  
    
    
    return distances

def fingerStartPos(map):
    line2 = map[1]
    finger_location =  {"finger1": line2[0],
                        "finger2": line2[1],
                        "finger3": line2[2],
                        "finger4": line2[3],
                        "finger5": line2[6],
                        "finger6": line2[7],
                        "finger7": line2[8],
                        "finger8": line2[9]}
    return finger_location


qwertyMap = ['qwertyuiop',
             'asdfghjkl;',
             'zxcvbnm,./']

DvorakMap = ['/,.pyfgcrl',
             'aoeuidhtns',
             ';qjkxbmwvz']


def convertMapToFinger(map):
    line1 = map[0]
    line2 = map[1]
    line3 = map[2]
    newMap={"finger1": [line1[0],line2[0],line3[0]],
            "finger2": [map[0][1],line2[1],line3[1]],
            "finger3": [line1[2],line2[2],line3[2]],
            "finger4": [line1[3],line2[3],line3[3],line1[4],line2[4],line3[4]],
            "finger5": [line1[5],line2[5],line3[5],line1[6],line2[6],line3[6]],
            "finger6": [line1[7],line2[7],line3[7]],
            "finger7": [line1[8],line2[8],line3[8]],
            "finger8": [line1[9],line2[9],line3[9]],
            }
    return newMap




def findDistance(input, maps, distanceList, locations):
    avaliableChars = "qwertyuiopasdfghjkl;zxcvbnm,./"
    finger_location = locations
    total_dist = 0
    for char in input:  #for each letter in the input
        if char != ' ' and char in avaliableChars: #except spaces
            for finger in maps:   #checks which finger can type the letter (char)            
                    for i in maps[finger]:
                        if char == i:
                            type_finger = finger #set a variable of the finger to type
            if finger_location[type_finger] != char:      #if its location is not the target:   
                distance_to_travel = finger_location[type_finger]+char          #get variable from dictonary
                total_dist += distanceList[distance_to_travel]                     #and add it to the total distance
                #print(char, "distance: ", distanceList[distance_to_travel])
                #print("from:", finger_location[type_finger], " to: ", char)
                finger_location[type_finger] = char                             #sets the location to the letter that was just typed

    return(total_dist)

input = '''import inspect


from typing import Callable

from allocation.adapters import orm, redis_eventpublisher
from allocation.adapters.notifications import (
    AbstractNotifications,
    EmailNotifications,
)
from allocation.service_layer import handlers, messagebus, unit_of_work


def bootstrap(
    start_orm: bool = True,
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlAlchemyUnitOfWork(),
    notifications: AbstractNotifications = None,
    publish: Callable = redis_eventpublisher.publish,
) -> messagebus.MessageBus:

    if notifications is None:
        notifications = EmailNotifications()

    if start_orm:
        orm.start_mappers()

    dependencies = {"uow": uow, "notifications": notifications, "publish": publish}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)
    import hashlib
import os
import random
import binascii
import ecdsa
import base58
import datetime
import webbrowser
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
import json
import hmac
import base64

start_time = datetime.datetime.now()

def bip(num):
    with open('BIP0039.txt', 'r') as f:
        words = f.read().split()
        for word in words:
            sent = [random.choice(words)
                for word in range(int(num))]
            return ' '.join(sent)

def passw(filename):
    try:
        with open(filename, 'r') as f:
            words = f.read().split()
            for word in words:
                sent = [random.choice(words)
                        for word in range(int(1))]
                return ' '.join(sent)
    except FileNotFoundError:
        pass
    except TypeError:
        pass


def hmac512(mnemonic, passphrase):
    d = mnemonic+' '+ passphrase
    return d
    
def master(hmacsha512):
    return hashlib.sha256(hmacsha512.encode("utf-8")).hexdigest().upper()


def pubkey(masterkey):
    privatekey = binascii.unhexlify(masterkey)
    s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
    return '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')

def addr(public_key):
    output = []; alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
    var = '00' + var.hexdigest() + hashlib.sha256(hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()[0:8]
    count = [char != '0' for char in var].index(True) // 2
    n = int(var, 16)
    while n > 0:
        n, remainder = divmod(n, 58)
        output.append(alphabet[remainder])
    for i in range(count): output.append(alphabet[0])
    return ''.join(output[::-1])

def wif(masterkey):
    var80 = "80"+masterkey
    var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
    return str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))), 'utf-8')

def database(address):
    with open("data-base", "r") as m:
        add = m.read().split()
        for ad in add:
            continue
        if address in add:
            data = open("Win.txt","a")
            data.write("Bingo " + str(sect)+"\n" +str(address)+"\n"+str(WIF)+"\n"+"\n")
            data.close()
            return 'Bingo'
        else:
            i = 'No luck'
            return i


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu', ['&Settings', 'E&xit']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Text('Number of mnemonic words', size=(30,1), font=('Comic sans ms', 10)),
               sg.Spin(values=('3', '6', '9', '12', '15', '18', '21', '24'),size=(3,1), key='num'), sg.Text('', size=(17,1))],
              [sg.Text('This program has been running for... ', size=(30,1), font=('Comic sans ms', 10)),
               sg.Text('', size=(30,1), font=('Comic sans ms', 10), key='_DATE_')],
              [sg.Text('')],
              [sg.Output(size=(87, 20), font=('Comic sans ms', 8), key='out')],
              [sg.Text('Passwords file', size=(12,1), font=('Comic sans ms', 10)),sg.In(size=(65, 1),key='-in-'), sg.FileBrowse()],
              [sg.Button('Start/Stop',  font=('Comic sans ms', 10))]]

    return sg.Window('Bitcoin wallet cracker',
                     layout=layout,
                     default_element_size=(9,1))



def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    generator = False
    while True:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read(timeout=10)
        window.Element('_DATE_').Update(str(datetime.datetime.now()-start_time))
        if event in (None, 'Exit'):
            break
        elif event == 'Start/Stop':
            generator = not generator
        if generator:
            filename = values['-in-'].rstrip()
            num = values['num']
            mnemonic = bip(num)
            passphrase = passw(filename)
            hmacsha512 = hmac512(mnemonic, passphrase)
            masterkey = master(hmacsha512)
            public_key = pubkey(masterkey)
            address = addr(public_key)
            WIF = wif(masterkey)
            data_base = database(address)
            print('mnemonic and passphrase:   '+str(mnemonic)+ ' ' +str(passphrase)+'\n'+
                  'private key:                           '+str(masterkey)+'\n'+
                  'address:                                 '+str(address)+'\n'+
                  'wif:                                        '+str(WIF)+"\n"+
                  'address with balance:           '+str(data_base)+'\n\n')
            
        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)


    
    window.Close()
    
main()
from warnings import warn as _warn
from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil
from math import sqrt as _sqrt, acos as _acos, cos as _cos, sin as _sin
from math import tau as TWOPI, floor as _floor, isfinite as _isfinite
from math import lgamma as _lgamma, fabs as _fabs, log2 as _log2
from os import urandom as _urandom
from _collections_abc import Sequence as _Sequence
from operator import index as _index
from itertools import accumulate as _accumulate, repeat as _repeat
from bisect import bisect as _bisect
import os as _os
import _random

try:
    # hashlib is pretty heavy to load, try lean internal module first
    from _sha512 import sha512 as _sha512
except ImportError:
    # fallback to official implementation
    from hashlib import sha512 as _sha512

__all__ = [
    "Random",
    "SystemRandom",
    "betavariate",
    "binomialvariate",
    "choice",
    "choices",
    "expovariate",
    "gammavariate",
    "gauss",
    "getrandbits",
    "getstate",
    "lognormvariate",
    "normalvariate",
    "paretovariate",
    "randbytes",
    "randint",
    "random",
    "randrange",
    "sample",
    "seed",
    "setstate",
    "shuffle",
    "triangular",
    "uniform",
    "vonmisesvariate",
    "weibullvariate",
]

NV_MAGICCONST = 4 * _exp(-0.5) / _sqrt(2.0)
LOG4 = _log(4.0)
SG_MAGICCONST = 1.0 + _log(4.5)
BPF = 53        # Number of bits in a float
RECIP_BPF = 2 ** -BPF
_ONE = 1


class Random(_random.Random):
    """Random number generator base class used by bound module functions.

    Used to instantiate instances of Random to get generators that don't
    share state.

    Class Random can also be subclassed if you want to use a different basic
    generator of your own devising: in that case, override the following
    methods:  random(), seed(), getstate(), and setstate().
    Optionally, implement a getrandbits() method so that randrange()
    can cover arbitrarily large ranges.

    """

    VERSION = 3     # used by getstate/setstate

    def __init__(self, x=None):
        """Initialize an instance.

        Optional argument x controls seeding, as for Random.seed().
        """

        self.seed(x)
        self.gauss_next = None

    def seed(self, a=None, version=2):
        """Initialize internal state from a seed.

        The only supported seed types are None, int, float,
        str, bytes, and bytearray.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If *a* is an int, all bits are used.

        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.

        """

        if version == 1 and isinstance(a, (str, bytes)):
            a = a.decode('latin-1') if isinstance(a, bytes) else a
            x = ord(a[0]) << 7 if a else 0
            for c in map(ord, a):
                x = ((1000003 * x) ^ c) & 0xFFFFFFFFFFFFFFFF
            x ^= len(a)
            a = -2 if x == -1 else x

        elif version == 2 and isinstance(a, (str, bytes, bytearray)):
            if isinstance(a, str):
                a = a.encode()
            a = int.from_bytes(a + _sha512(a).digest())

        elif not isinstance(a, (type(None), int, float, str, bytes, bytearray)):
            raise TypeError('The only supported seed types are: None,\n'
                            'int, float, str, bytes, and bytearray.')

        super().seed(a)
        self.gauss_next = None

    def getstate(self):
        """Return internal state; can be passed to setstate() later."""
        return self.VERSION, super().getstate(), self.gauss_next

    def setstate(self, state):
        """Restore internal state from object returned by getstate()."""
        version = state[0]
        if version == 3:
            version, internalstate, self.gauss_next = state
            super().setstate(internalstate)
        elif version == 2:
            version, internalstate, self.gauss_next = state
            # In version 2, the state was saved as signed ints, which causes
            #   inconsistencies between 32/64-bit systems. The state is
            #   really unsigned 32-bit ints, so we convert negative ints from
            #   version 2 to positive longs for version 3.
            try:
                internalstate = tuple(x % (2 ** 32) for x in internalstate)
            except ValueError as e:
                raise TypeError from e
            super().setstate(internalstate)
        else:
            raise ValueError("state with version s passed to "
                             "Random.setstate() of version s" %
                             (version, self.VERSION))


    ## -------------------------------------------------------
    ## ---- Methods below this point do not need to be overridden or extended
    ## ---- when subclassing for the purpose of using a different core generator.


    ## -------------------- pickle support  -------------------

    # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
    # longer called; we leave it here because it has been here since random was
    # rewritten back in 2001 and why risk breaking something.
    def __getstate__(self):  # for pickle
        return self.getstate()

    def __setstate__(self, state):  # for pickle
        self.setstate(state)

    def __reduce__(self):
        return self.__class__, (), self.getstate()


    ## ---- internal support method for evenly distributed integers ----

    def __init_subclass__(cls, /, **kwargs):
        """Control how subclasses generate random integers.

        The algorithm a subclass can use depends on the random() and/or
        getrandbits() implementation available to it and determines
        whether it can generate random integers from arbitrarily large
        ranges.
        """

        for c in cls.__mro__:
            if '_randbelow' in c.__dict__:
                # just inherit it
                break
            if 'getrandbits' in c.__dict__:
                cls._randbelow = cls._randbelow_with_getrandbits
                break
            if 'random' in c.__dict__:
                cls._randbelow = cls._randbelow_without_getrandbits
                break

    def _randbelow_with_getrandbits(self, n):
        "Return a random int in the range [0,n).  Defined for n > 0."

        getrandbits = self.getrandbits
        k = n.bit_length()
        r = getrandbits(k)  # 0 <= r < 2**k
        while r >= n:
            r = getrandbits(k)
        return r

    def _randbelow_without_getrandbits(self, n, maxsize=1<<BPF):
        """Return a random int in the range [0,n).  Defined for n > 0.

        The implementation does not use getrandbits, but only random.
        """

        random = self.random
        if n >= maxsize:
            _warn("Underlying random() generator does not supply \n"
                "enough bits to choose from a population range this large.\n"
                "To remove the range limitation, add a getrandbits() method.")
            return _floor(random() * n)
        rem = maxsize % n
        limit = (maxsize - rem) / maxsize   # int(limit * maxsize) % n == 0
        r = random()
        while r >= limit:
            r = random()
        return _floor(r * maxsize) % n

    _randbelow = _randbelow_with_getrandbits


    ## --------------------------------------------------------
    ## ---- Methods below this point generate custom distributions
    ## ---- based on the methods defined above.  They do not
    ## ---- directly touch the underlying generator and only
    ## ---- access randomness through the methods:  random(),
    ## ---- getrandbits(), or _randbelow().


    ## -------------------- bytes methods ---------------------

    def randbytes(self, n):
        """Generate n random bytes."""
        return self.getrandbits(n * 8).to_bytes(n, 'little')

        

    ## -------------------- integer methods  -------------------

    def randrange(self, start, stop=None, step=_ONE):
        """Choose a random item from range(stop) or range(start, stop[, step]).

        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.

        """

        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
        istart = _index(start)
        if stop is None:
            # We don't check for "step != 1" because it hasn't been
            # type checked and converted to an integer yet.
            if step is not _ONE:
                raise TypeError("Missing a non-None stop argument")
            if istart > 0:
                return self._randbelow(istart)
            raise ValueError("empty range for randrange()")

        # Stop argument supplied.
        istop = _index(stop)
        width = istop - istart
        istep = _index(step)
        # Fast path.
        if istep == 1:
            if width > 0:
                return istart + self._randbelow(width)
            raise ValueError(f"empty range in randrange({start{stop})")

        # Non-unit step argument supplied.
        if istep > 0:
            n = (width + istep - 1) // istep
        elif istep < 0:
            n = (width + istep + 1) // istep
        else:
            raise ValueError("zero step for randrange()")
        if n <= 0:
            raise ValueError(f"empty range in randrange({start}, {stop}, {step})")
        return istart + istep * self._randbelow(n)

    def randint(self, a, b):
        """Return random integer in range [a, b], including both end points.
        """

        return self.randrange(a, b+1)


    ## -------------------- sequence methods  -------------------

    def choice(self, seq):
        """Choose a random element from a non-empty sequence."""

        # As an accommodation for NumPy, we don't use "if not seq"
        # because bool(numpy.array()) raises a ValueError.
        if not len(seq):
            raise IndexError('Cannot choose from an empty sequence')
        return seq[self._randbelow(len(seq))]

    def shuffle(self, x):
        """Shuffle list x in place, and return None."""

        randbelow = self._randbelow
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = randbelow(i + 1)
            x[i], x[j] = x[j], x[i]

    def sample(self, population, k, *, counts=None):
        """Chooses k unique random elements from a population sequence.

        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        Repeated elements can be specified one at a time or with the optional
        counts parameter.  For example:

            sample(['red', 'blue'], counts=[4, 2], k=5)

        is equivalent to:

            sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)

        To choose a sample from a range of integers, use range() for the
        population argument.  This is especially fast and space efficient
        for sampling from a large population:

            sample(range(10000000), 60)

        """

        # Sampling without replacement entails tracking either potential
        # selections (the pool) in a list or previous selections in a set.

        # When the number of selections is small compared to the
        # population, then tracking selections is efficient, requiring
        # only a small set and an occasional reselection.  For
        # a larger number of selections, the pool tracking method is
        # preferred since the list takes less space than the
        # set and it doesn't suffer from frequent reselections.

        # The number of calls to _randbelow() is kept at or near k, the
        # theoretical minimum.  This is important because running time
        # is dominated by _randbelow() and because it extracts the
        # least entropy from the underlying random number generators.

        # Memory requirements are kept to the smaller of a k-length
        # set or an n-length list.

        # There are other sampling algorithms that do not require
        # auxiliary memory, but they were rejected because they made
        # too many calls to _randbelow(), making them slower and
        # causing them to eat more entropy than necessary.

        if not isinstance(population, _Sequence):
            raise TypeError("Population must be a sequence.  "
                            "For dicts or sets, use sorted(d).")
        n = len(population)
        if counts is not None:
            cum_counts = list(_accumulate(counts))
            if len(cum_counts) != n:
                raise ValueError('The number of counts does not match the population')
            total = cum_counts.pop()
            if not isinstance(total, int):
                raise TypeError('Counts must be integers')
            if total <= 0:
                raise ValueError('Total of counts must be greater than zero')
            selections = self.sample(range(total), k=k)
            bisect = _bisect
            return [population[bisect(cum_counts, s)] for s in selections]
        randbelow = self._randbelow
        if not 0 <= k <= n:
            raise ValueError("Sample larger than population or is negative")
        result = [None] * k
        setsize = 21        # size of a small set minus size of an empty list
        if k > 5:
            setsize += 4 ** _ceil(_log(k * 3, 4))  # table size for big sets
        if n <= setsize:
            # An n-length list is smaller than a k-length set.
            # Invariant:  non-selected at pool[0 : n-i]
            pool = list(population)
            for i in range(k):
                j = randbelow(n - i)
                result[i] = pool[j]
                pool[j] = pool[n - i - 1]  # move non-selected item into vacancy
        else:
            selected = set()
            selected_add = selected.add
            for i in range(k):
                j = randbelow(n)
                while j in selected:
                    j = randbelow(n)
                selected_add(j)
                result[i] = population[j]
        return result

    def choices(self, population, weights=None, *, cum_weights=None, k=1):
        """Return a k sized list of population elements chosen with replacement.

        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.

        """
        random = self.random
        n = len(population)
        if cum_weights is None:
            if weights is None:
                floor = _floor
                n += 0.0    # convert to float for a small speed improvement
                return [population[floor(random() * n)] for i in _repeat(None, k)]
            try:
                cum_weights = list(_accumulate(weights))
            except TypeError:
                if not isinstance(weights, int):
                    raise
                k = weights
                raise TypeError(
                    f'The number of choices must be a keyword argument: {k=}'
                ) from None
        elif weights is not None:
            raise TypeError('Cannot specify both weights and cumulative weights')
        if len(cum_weights) != n:
            raise ValueError('The number of weights does not match the population')
        total = cum_weights[-1] + 0.0   # convert to float
        if total <= 0.0:
            raise ValueError('Total of weights must be greater than zero')
        if not _isfinite(total):
            raise ValueError('Total of weights must be finite')
        bisect = _bisect
        hi = n - 1
        return [population[bisect(cum_weights, random() * total, 0, hi)]
                for i in _repeat(None, k)]


    ## -------------------- real-valued distributions  -------------------

    def uniform(self, a, b):
        "Get a random number in the range [a, b) or [a, b] depending on rounding."
        return a + (b - a) * self.random()

    def triangular(self, low=0.0, high=1.0, mode=None):
        """Triangular distribution.

        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.

        http://en.wikipedia.org/wiki/Triangular_distribution

        """
        u = self.random()
        try:
            c = 0.5 if mode is None else (mode - low) / (high - low)
        except ZeroDivisionError:
            return low
        if u > c:
            u = 1.0 - u
            c = 1.0 - c
            low, high = high, low
        return low + (high - low) * _sqrt(u * c)

    def normalvariate(self, mu=0.0, sigma=1.0):
        """Normal distribution.

        mu is the mean, and sigma is the standard deviation.

        """
        # Uses Kinderman and Monahan method. Reference: Kinderman,
        # A.J. and Monahan, J.F., "Computer generation of random
        # variables using the ratio of uniform deviates", ACM Trans
        # Math Software, 3, (1977), pp257-260.

        random = self.random
        while True:
            u1 = random()
            u2 = 1.0 - random()
            z = NV_MAGICCONST * (u1 - 0.5) / u2
            zz = z * z / 4.0
            if zz <= -_log(u2):
                break
        return mu + z * sigma

    def gauss(self, mu=0.0, sigma=1.0):
        """Gaussian distribution.

        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.

        Not thread-safe without a lock around calls.

        """
        # When x and y are two variables from [0, 1), uniformly
        # distributed, then
        #
        #    cos(2*pi*x)*sqrt(-2*log(1-y))
        #    sin(2*pi*x)*sqrt(-2*log(1-y))
        #
        # are two *independent* variables with normal distribution
        # (mu = 0, sigma = 1).
        # (Lambert Meertens)
        # (corrected version; bug discovered by Mike Miller, fixed by LM)

        # Multithreading note: When two threads call this function
        # simultaneously, it is possible that they will receive the
        # same return value.  The window is very small though.  To
        # avoid this, you have to use a lock around all calls.  (I
        # didn't want to slow this down in the serial case by using a
        # lock here.)

        random = self.random
        z = self.gauss_next
        self.gauss_next = None
        if z is None:
            x2pi = random() * TWOPI
            g2rad = _sqrt(-2.0 * _log(1.0 - random()))
            z = _cos(x2pi) * g2rad
            self.gauss_next = _sin(x2pi) * g2rad

        return mu + z * sigma

    def lognormvariate(self, mu, sigma):
        """Log normal distribution.

        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.

        """
        return _exp(self.normalvariate(mu, sigma))

    def expovariate(self, lambd=1.0):
        """Exponential distribution.

        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.

        """
        # lambd: rate lambd = 1/mean
        # ('lambda' is a Python reserved word)

        # we use 1-random() instead of random() to preclude the
        # possibility of taking the log of zero.
        return -_log(1.0 - self.random()) / lambd

    def vonmisesvariate(self, mu, kappa):
        """Circular data distribution.

        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.

        """
        # Based upon an algorithm published in: Fisher, N.I.,
        # "Statistical Analysis of Circular Data", Cambridge
        # University Press, 1993.

        # Thanks to Magnus Kessler for a correction to the
        # implementation of step 4.

        random = self.random
        if kappa <= 1e-6:
            return TWOPI * random()

        s = 0.5 / kappa
        r = s + _sqrt(1.0 + s * s)

        while True:
            u1 = random()
            z = _cos(_pi * u1)

            d = z / (r + z)
            u2 = random()
            if u2 < 1.0 - d * d or u2 <= (1.0 - d) * _exp(d):
                break

        q = 1.0 / r
        f = (q + z) / (1.0 + q * z)
        u3 = random()
        if u3 > 0.5:
            theta = (mu + _acos(f)) % TWOPI
        else:
            theta = (mu - _acos(f)) % TWOPI

        return theta

    def gammavariate(self, alpha, beta):
        """Gamma distribution.  Not the gamma function!

        Conditions on the parameters are alpha > 0 and beta > 0.

        The probability distribution function is:

                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha

        """
        # alpha > 0, beta > 0, mean is alpha*beta, variance is alpha*beta**2

        # Warning: a few older sources define the gamma distribution in terms
        # of alpha > -1.0
        if alpha <= 0.0 or beta <= 0.0:
            raise ValueError('gammavariate: alpha and beta must be > 0.0')

        random = self.random
        if alpha > 1.0:

            # Uses R.C.H. Cheng, "The generation of Gamma
            # variables with non-integral shape parameters",
            # Applied Statistics, (1977), 26, No. 1, p71-74

            ainv = _sqrt(2.0 * alpha - 1.0)
            bbb = alpha - LOG4
            ccc = alpha + ainv

            while True:
                u1 = random()
                if not 1e-7 < u1 < 0.9999999:
                    continue
                u2 = 1.0 - random()
                v = _log(u1 / (1.0 - u1)) / ainv
                x = alpha * _exp(v)
                z = u1 * u1 * u2
                r = bbb + ccc * v - x
                if r + SG_MAGICCONST - 4.5 * z >= 0.0 or r >= _log(z):
                    return x * beta

        elif alpha == 1.0:
            # expovariate(1/beta)
            return -_log(1.0 - random()) * beta

        else:
            # alpha is between 0 and 1 (exclusive)
            # Uses ALGORITHM GS of Statistical Computing - Kennedy & Gentle
            while True:
                u = random()
                b = (_e + alpha) / _e
                p = b * u
                if p <= 1.0:
                    x = p ** (1.0 / alpha)
                else:
                    x = -_log((b - p) / alpha)
                u1 = random()
                if p > 1.0:
                    if u1 <= x ** (alpha - 1.0):
                        break
                elif u1 <= _exp(-x):
                    break
            return x * beta

    def betavariate(self, alpha, beta):
        """Beta distribution.

        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.

        """
        ## See
        ## http://mail.python.org/pipermail/python-bugs-list/2001-January/003752.html
        ## for Ivan Frohne's insightful analysis of why the original implementation:
        ##
        ##    def betavariate(self, alpha, beta):
        ##        # Discrete Event Simulation in C, pp 87-88.
        ##
        ##        y = self.expovariate(alpha)
        ##        z = self.expovariate(1.0/beta)
        ##        return z/(y+z)
        ##
        ## was dead wrong, and how it probably got that way.

        # This version due to Janne Sinkkonen, and matches all the std
        # texts (e.g., Knuth Vol 2 Ed 3 pg 134 "the beta distribution").
        y = self.gammavariate(alpha, 1.0)
        if y:
            return y / (y + self.gammavariate(beta, 1.0))
        return 0.0

    def paretovariate(self, alpha):
        """Pareto distribution.  alpha is the shape parameter."""
        # Jain, pg. 495

        u = 1.0 - self.random()
        return u ** (-1.0 / alpha)

    def weibullvariate(self, alpha, beta):
        """Weibull distribution.

        alpha is the scale parameter and beta is the shape parameter.

        """
        # Jain, pg. 499; bug fix courtesy Bill Arms

        u = 1.0 - self.random()
        return alpha * (-_log(u)) ** (1.0 / beta)


    ## -------------------- discrete  distributions  ---------------------

    def binomialvariate(self, n=1, p=0.5):
        """Binomial random variable.

        Gives the number of successes for *n* independent trials
        with the probability of success in each trial being *p*:

            sum(random() < p for i in range(n))

        Returns an integer in the range:   0 <= X <= n

        """
        # Error check inputs and handle edge cases
        if n < 0:
            raise ValueError("n must be non-negative")
        if p <= 0.0 or p >= 1.0:
            if p == 0.0:
                return 0
            if p == 1.0:
                return n
            raise ValueError("p must be in the range 0.0 <= p <= 1.0")

        random = self.random

        # Fast path for a common case
        if n == 1:
            return _index(random() < p)

        # Exploit symmetry to establish:  p <= 0.5
        if p > 0.5:
            return n - self.binomialvariate(n, 1.0 - p)

        if n * p < 10.0:
            # BG: Geometric method by Devroye with running time of O(np).
            # https://dl.acm.org/doi/pdf/10.1145/42372.42381
            x = y = 0
            c = _log2(1.0 - p)
            if not c:
                return x
            while True:
                y += _floor(_log2(random()) / c) + 1
                if y > n:
                    return x
                x += 1

        # BTRS: Transformed rejection with squeeze method by Wolfgang Hörmann
        # https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.47.8407&rep=rep1&type=pdf
        assert n*p >= 10.0 and p <= 0.5
        setup_complete = False

        spq = _sqrt(n * p * (1.0 - p))  # Standard deviation of the distribution
        b = 1.15 + 2.53 * spq
        a = -0.0873 + 0.0248 * b + 0.01 * p
        c = n * p + 0.5
        vr = 0.92 - 4.2 / b

        while True:

            u = random()
            u -= 0.5
            us = 0.5 - _fabs(u)
            k = _floor((2.0 * a / us + b) * u + c)
            if k < 0 or k > n:
                continue

            # The early-out "squeeze" test substantially reduces
            # the number of acceptance condition evaluations.
            v = random()
            if us >= 0.07 and v <= vr:
                return k

            # Acceptance-rejection test.
            # Note, the original paper errorneously omits the call to log(v)
            # when comparing to the log of the rescaled binomial distribution.
            if not setup_complete:
                alpha = (2.83 + 5.1 / b) * spq
                lpq = _log(p / (1.0 - p))
                m = _floor((n + 1) * p)         # Mode of the distribution
                h = _lgamma(m + 1) + _lgamma(n - m + 1)
                setup_complete = True           # Only needs to be done once
            v *= alpha / (a / (us * us) + b)
            if _log(v) <= h - _lgamma(k + 1) - _lgamma(n - k + 1) + (k - m) * lpq:
                return k


## ------------------------------------------------------------------
## --------------- Operating System Random Source  ------------------


class SystemRandom(Random):
    """Alternate random number generator using sources provided
    by the operating system (such as /dev/urandom on Unix or
    CryptGenRandom on Windows).

     Not available on all systems (see os.urandom() for details).

    """

    def random(self):
        """Get the next random number in the range 0.0 <= X < 1.0."""
        return (int.from_bytes(_urandom(7)) >> 3) * RECIP_BPF

    def getrandbits(self, k):
        """getrandbits(k) -> x.  Generates an int with k random bits."""
        if k < 0:
            raise ValueError('number of bits must be non-negative')
        numbytes = (k + 7) // 8                       # bits / 8 and rounded up
        x = int.from_bytes(_urandom(numbytes))
        return x >> (numbytes * 8 - k)                # trim excess bits

    def randbytes(self, n):
        """Generate n random bytes."""
        # os.urandom(n) fails with ValueError for n < 0
        # and returns an empty bytes string for n == 0.
        return _urandom(n)

    def seed(self, *args, **kwds):
        "Stub method.  Not used for a system random number generator."
        return None

    def _notimplemented(self, *args, **kwds):
        "Method should not be called for a system random number generator."
        raise NotImplementedError('System entropy source does not have state.')
    getstate = setstate = _notimplemented


# ----------------------------------------------------------------------
# Create one instance, seeded from current time, and export its methods
# as module-level functions.  The functions share state across all uses
# (both in the user's code and in the Python libraries), but that's fine
# for most programs and is easier for the casual user than making them
# instantiate their own Random() instance.

_inst = Random()
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
triangular = _inst.triangular
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
sample = _inst.sample
shuffle = _inst.shuffle
choices = _inst.choices
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
gauss = _inst.gauss
betavariate = _inst.betavariate
binomialvariate = _inst.binomialvariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
getrandbits = _inst.getrandbits
randbytes = _inst.randbytes


## ------------------------------------------------------
## ----------------- test program -----------------------

def _test_generator(n, func, args):
    from statistics import stdev, fmean as mean
    from time import perf_counter

    t0 = perf_counter()
    data = [func(*args) for i in _repeat(None, n)]
    t1 = perf_counter()

    xbar = mean(data)
    sigma = stdev(data, xbar)
    low = min(data)
    high = max(data)

    print(f'{t1 - t0:.3f} sec, {n} times {func.__name__}{args!r}')
    print('avg g, stddev %, min % max %n' % (xbar, sigma, low, high))


def _test(N=10_000):
    _test_generator(N, random, ())
    _test_generator(N, normalvariate, (0.0, 1.0))
    _test_generator(N, lognormvariate, (0.0, 1.0))
    _test_generator(N, vonmisesvariate, (0.0, 1.0))
    _test_generator(N, binomialvariate, (15, 0.60))
    _test_generator(N, binomialvariate, (100, 0.75))
    _test_generator(N, gammavariate, (0.01, 1.0))
    _test_generator(N, gammavariate, (0.1, 1.0))
    _test_generator(N, gammavariate, (0.1, 2.0))
    _test_generator(N, gammavariate, (0.5, 1.0))
    _test_generator(N, gammavariate, (0.9, 1.0))
    _test_generator(N, gammavariate, (1.0, 1.0))
    _test_generator(N, gammavariate, (2.0, 1.0))
    _test_generator(N, gammavariate, (20.0, 1.0))
    _test_generator(N, gammavariate, (200.0, 1.0))
    _test_generator(N, gauss, (0.0, 1.0))
    _test_generator(N, betavariate, (3.0, 3.0))
    _test_generator(N, triangular, (0.0, 1.0, 1.0 / 3.0))


## ------------------------------------------------------
## ------------------ fork support  ---------------------

if hasattr(_os, "fork"):
    _os.register_at_fork(after_in_child=_inst.seed)


if __name__ == '__main__':
    _test()
   #for chemistry webassign

#for atm
def function_atm(input_choice, input_number, input_final):
    #turns atm to torr/mmHG
    if input_final == "torr":
        print(input_number * 760)
        
    #turns atm to kpa
    elif input_final ==  "kpa":
        print(input_number * 101.3)
            

def function_torr(input_choice, input_number, input_final):
    #turns torr to atm
    if input_final == "atm":
        print(input_number / 760)
    #turns torr to kpa
    elif input_final == "kpa":
        print(input_number * 0.13328947)
       
        
def function_kpa(input_choice, input_number, input_final):
    #turns kpa to atm
    if input_final == "atm":
        print(input_number / 101.3)
    #turns kpa to torr
    elif input_final == "torr":
        print(input_number * 7.50246792)
        
def function_
        
#driver
if __name__ == "__main__":   
    while (1 != 0):
        print("type everything in lowercase \n")

        input_choice = str(input("what is your unit "))
        input_number = float(input("number of the unit "))
        input_final = str(input("what is the unit you want to convert to "))
                
        if input_choice == "atm":
            function_atm(input_choice, input_number, input_final)
            
        if input_choice == "torr":
            function_torr(input_choice, input_number, input_final)

        if input_choice == "kpa":
            function_kpa(input_choice, input_number, input_final)
        
        print('\n')
        
     import random
from uuid import uuid4

from flask import Flask, make_response, request
from google.cloud import firestore


app = Flask(__name__)
db = firestore.Client()
sessions = db.collection('sessions')
greetings = [
    'Hello World',
    'Hallo Welt',
    'Ciao Mondo',
    'Salut le Monde',
    'Hola Mundo',
]


@firestore.transactional
def get_session_data(transaction, session_id):
Looks up (or creates) the session with the given session_id.
        Creates a random session_id if none is provided. Increments
        the number of views in this session. Updates are done in a
        transaction to make sure no saved increments are overwritten.

    if session_id is None:
        session_id = str(uuid4())   # Random, unique identifier

    doc_ref = sessions.document(document_id=session_id)
    doc = doc_ref.get(transaction=transaction)
    if doc.exists:
        session = doc.to_dict()
    else:
        session = {
            'greeting': random.choice(greetings),
            'views': 0
        }

    session['views'] += 1   # This counts as a view
    transaction.set(doc_ref, session)

    session['session_id'] = session_id
    return session


@app.route('/', methods=['GET'])
def home():
    template = '<body>{} views for "{}"</body>'

    transaction = db.transaction()
    session = get_session_data(transaction, request.cookies.get('session_id'))

    resp = make_response(template.format(
        session['views'],
        session['greeting']
        )
    )
    resp.set_cookie('session_id', session['session_id'], httponly=True)
    return resp


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)






def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()



def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
from time import strftime
from tkinter import Label, Tk

# ======= Configuring window =========
window = Tk()
window.title("")
window.geometry("200x80")
window.configure(bg="green")  # =======Background of the clock=====
window.resizable(False, False)  # =====setting a fixed window size =======

clock_label = Label(
    window, bg="black", fg="cyan", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)


def update_label():
    """
    This function will update the clock

    every 80 milliseconds
    """
    current_time = strftime("%H: %M: %S\n -%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()
        from collections.abc import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
    
        from collections.abc import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
            from collections.abc import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)
# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
'''

def findDist(input, map):
    fingerMap = convertMapToFinger(map)
    distances = findKeyDistances(map)
    finger_location = fingerStartPos(map)
    return(findDistance(input, fingerMap, distances, finger_location))


def generate_random_keyboard():
    keys = list("qwertyuiopasdfghjkl;zxcvbnm,./")
    random.shuffle(keys)
    keyboard_layout = [''.join(keys[:10]), ''.join(keys[10:20]), ''.join(keys[20:])]
    return keyboard_layout



def findBestRandom(generations):
    start_time = time.time()  # Start time of the loop
    best = 100000000000000000000000
    bestLayout = []
    for i in range(0, generations):
        current_iteration = i + 1
        progress_percentage = (current_iteration / generations) * 100  # Calculate progress percentage
        current_time = time.time()
        elapsed_time = current_time - start_time
        estimated_time_remaining = (generations - current_iteration) * elapsed_time / current_iteration

        # Display progress and estimated time remaining
        print(f"Progress: {progress_percentage:.2f}%, Estimated Time Remaining: {int(estimated_time_remaining):.2f} seconds, ", int(estimated_time_remaining/6), " minutes", end="\r")

        randomkeys = generate_random_keyboard()
        distance = findDist(input, randomkeys)
        if distance < best:
            best = distance
            bestLayout = randomkeys
    print(best)
    return([best, bestLayout])

print(findDist(input, ['itb.,jdgr;', 'owenylmaus', 'kqxf/chvzp']))
'''bestList = []
for i in range(0, 10):
    board = generate_random_keyboard()
    returned = findBestRandom(10000)
    bestList.append(returned)

for best in bestList:
    print("score: ", best[0], " for the keyboard layout: ", best[1])'''



def roulette_wheel_selection(p):
   c = np.cumsum(p)
   r = sum(p) * np.random.rand()
   ind = np.argwhere(r <= c)
   return ind[0][0]

#takes population 1 and 2 to split them in half
#then compares the the halves from p1 and p2 to find the best one
#we take the best half and then 
def crossover(p1, p2):
    print(p2)
    p2List = p2['board'][0] + p2['board'][1] + p2['board'][0]
    #gets the halves
    if 'board' in p1 and isinstance(p1['board'], list):
        p1_lists = p1['board']
        for i in range(len(p1_lists)):
            p1_half_length = len(p1_lists[i]) // 2
            p1_lists[i] = p1_lists[i][:p1_half_length]
        for char in p2List:
            if char not in p1['board'][0] or char not in p1['board'][1] or char not in p1['board'][2]:
                if len(p1['board'][0]) < 10:
                    p1['board'][0] += char
                elif len(p1['board'][1]) < 10:
                    p1['board'][1] += char
                elif len(p1['board'][2]) < 10:
                    p1['board'][2] += char



    
def geneticAlgorithm(amount):
    population = {}
    distances = []

    # Generate initial population
    for i in range(amount):
        board = generate_random_keyboard()
        population[i] = {'board': board, 'score': findDist(input, board)}

    # Calculating probability for roulette wheel selection
    beta = 1
    for j in range(1000):
        distances = []
        for i in range(len(population)):
            distances.append(population[i]['score'])
        avg_cost = np.mean(distances)

        if avg_cost != 0:
            distances = np.array(distances) / avg_cost
            probs = np.exp(-beta * distances)

        # Roulette wheel selection
        p1 = population[roulette_wheel_selection(probs)]
        p2 = population[roulette_wheel_selection(probs)]
        crossover(p1, p2)
    print(p1)

    
        
 

geneticAlgorithm(1000)

