#!/usr/bin/python3
import random, os
from .colors import color
from time import sleep

banners = []

banner_1 = \
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 _____                            _              ______                           _             
|  ___|                          | |             |  _  \                         | |            
| |__ _ __   ___ _ __ _   _ _ __ | |_ ___  _ __  | | | |___  ___ _ __ _   _ _ __ | |_ ___  _ __ 
|  __| '_ \ / __| '__| | | | '_ \| __/ _ \| '__| | | | / _ \/ __| '__| | | | '_ \| __/ _ \| '__|
| |__| | | | (__| |  | |_| | |_) | || (_) | |    | |/ /  __/ (__| |  | |_| | |_) | || (_) | |   
\____/_| |_|\___|_|   \__, | .__/ \__\___/|_|    |___/ \___|\___|_|   \__, | .__/ \__\___/|_|   
                       __/ | |                                         __/ | |                  
                      |___/|_|                                        |___/|_|                  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

banners.append(banner_1)

banner_2 = \
"""

________________________________________________________________________________
|   __|___ ___ ___ _ _ ___| |_ ___ ___   |    \ ___ ___ ___ _ _ ___| |_ ___ ___ 
|   __|   |  _|  _| | | . |  _| . |  _|  |  |  | -_|  _|  _| | | . |  _| . |  _|
|_____|_|_|___|_| |_  |  _|_| |___|_|    |____/|___|___|_| |_  |  _|_| |___|_|  
__________________|___|_|__________________________________|___|_|______________

"""

banners.append(banner_2)

banner_3 = \
"""
________________________________________________________
╔═╗┌┐┌┌─┐┬─┐┬ ┬┌─┐┌┬┐┌─┐┬─┐  ╔╦╗┌─┐┌─┐┬─┐┬ ┬┌─┐┌┬┐┌─┐┬─┐
║╣ ││││  ├┬┘└┬┘├─┘ │ │ │├┬┘   ║║├┤ │  ├┬┘└┬┘├─┘ │ │ │├┬┘
╚═╝┘└┘└─┘┴└─ ┴ ┴   ┴ └─┘┴└─  ═╩╝└─┘└─┘┴└─ ┴ ┴   ┴ └─┘┴└─
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

banners.append(banner_3)

banner_4 = \
"""

▄▄▄ . ▐ ▄  ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄      ▄▄▄      ·▄▄▄▄  ▄▄▄ . ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄      ▄▄▄  
▀▄.▀·•█▌▐█▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ▪     ▀▄ █·    ██▪ ██ ▀▄.▀·▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ▪     ▀▄ █·
▐▀▀▪▄▐█▐▐▌██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪ ▄█▀▄ ▐▀▀▄     ▐█· ▐█▌▐▀▀▪▄██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█▄▄▌██▐█▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▌.▐▌▐█•█▌    ██. ██ ▐█▄▄▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▌.▐▌▐█•█▌
 ▀▀▀ ▀▀ █▪·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀  ▀█▄▀▪.▀  ▀    ▀▀▀▀▀•  ▀▀▀ ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀  ▀█▄▀▪.▀  ▀

"""

banners.append(banner_4)

banner_5 = \
"""
__________________________________________________________
 __             _              _              _          
|_ __  _  __ \/|_)_|_ _  __   | \ _  _  __ \/|_)_|_ _  __
|__| |(_  |  / |   |_(_) |    |_/(/_(_  |  / |   |_(_) | 
__________________________________________________________
"""

banners.append(banner_5)

##########################################################################################################################

help_banner = \
"""
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  |                                                                      |
  |  A simple script to implement various encryption and decryption      |
  |  algorithms in a simplistic manner. The list will increase over time.|
  |                                                                      |
  |  Select the type of encryption or decryption algorithm to use and    |
  |  and follow the on-screen instructions. (Choose 'E' / 'D' and so on) |
  |  For the algorithms that are feasibly susceptible to brute force,    |
  |  {}providing no decryption key will trigger a brute force decryption{}   |
  |  (this feature will be mentioned for the specific algorithms)        |
  |                                                                      |
  |  {}Note:- {}Please ensure that the PyGame module is installed{}            |
  |         {}for the Morse Code Audio to work (provided in requirements){}  |
  |                                                                      |
  |                                             created by ~ {}Ricky-001{}   |
  |                   {}{}https://github.com/Ricky-001/custompass_generator{}  |
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""".format(color.ORANGE,color.END, color.RED,color.YELLOW,color.END,color.YELLOW,color.END ,color.GREEN,color.END, color.BLUE,color.UNDERLINE,color.END)


def show():
  show = random.randint(0, 4)

  if show==0:
    for line in banners[show].split('\n'):
      print(color.BLUE + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==1:
    for line in banners[show].split('\n'):
      print(color.YELLOW + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==2:
    for line in banners[show].split('\n'):
      print(color.GREEN + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==3:
    for line in banners[show].split('\n'):
      print(color.RED + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==4:
    for line in banners[show].split('\n'):
      print(color.CYAN + color.BOLD + line + color.END)
      sleep(0.05)

  for line in help_banner.split('\n'):
    print(line)
    sleep(0.03)
  sleep(1)