#!/usr/bin/python3
#
#  [Program]
#
#  PEH
#  PyEmailHanu
#
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.

'''imports'''
import smtplib as system
import sys
from time import sleep


class hcolors:
    RED = "\033[31m"
    GREEN = '\033[92m'
    YELLOW = '\033[93m'


def banner():
    print(hcolors.YELLOW + '''
   ___               ____           _ __        __ __              
  / _ \__ __  ____  / __/_ _  ___ _(_) / ____  / // /__ ____  __ __
 / ___/ // / /___/ / _//  ' \/ _ `/ / / /___/ / _  / _ `/ _ \/ // /
/_/   \_, /       /___/_/_/_/\_,_/_/_/       /_//_/\_,_/_//_/\_,_/ 
     /___/                                                         
  
    					     [ AUTHOR : HORRID HANU ]
                                                                    .--.--.
*.______________________________________________________________,' (For you)
                                                                    `-___-' \n''')
    print(hcolors.RED + '[-] Email Sending script v1.1')

def loading(Message, intialTime, endtime):  #endtime = intialTime - 1 
    for x in range(1,intialTime):
        for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
            sleep(0.1)
            if x == endtime:
                print(hcolors.RED + '', end="[-] ")
                break
            else:
                print( Message +i, end = '\r')




def Start():

    object = system.SMTP("smtp.gmail.com", 587)
    object.starttls()

    '''loading for initailizing the code..'''
    loading(hcolors.GREEN + " Initializing the script, Please Wait ", 10, 9)

    '''print note statement'''
    print(hcolors.RED + "Note : Use an App Password if you have 2-factor authentication enabled")
    
    
    '''User Info for authentication'''
    print('[+] For logging process provide your information, Good luck!')
    userEmail = input(hcolors.GREEN + "\n[+] Enter your email (i.e anyone123@gmail.com) <: ")
    while userEmail == "" or userEmail == " ":
        userEmail = input(hcolors.RED + "[+] Enter valid email (i.e anyone123@gmail.com)<: ")
    
    userPassword = input(hcolors.GREEN + "[+] Enter your password (i.e meva gmxz swie psbv) <:")
    if userPassword == "":
        print(hcolors.RED + '\n\nSomething went wrong, You skipped to enter password, Thanks for your patience')
        sys.exit()
    
    '''Login progess'''
    loading(hcolors.GREEN + " Logging... : ", 6, 5)
    object.login(userEmail, userPassword)
    print(hcolors.GREEN + "login successfully.....")


    #Email Subject and body
    subject = input("\n[+] Enter subject of your mail (By Default - Sending mails using python) <: ")
    if subject == "":
        subject = "Sending mails using python"


    '''Body Context'''
    body = open("body.txt", 'rt')
    bodyConent = body.read()
    
    print(hcolors.GREEN + '[+] Body message will be sent from file "directory/body.txt" !!')
    
    '''list of targets to send mails'''
    targets = open("target_list.txt", 'rt')
    target_context = targets.read()
    print('[+] Target lists taken from the file "directory/target_list.txt" !!')
    
    # listOfTargets = input(hcolors.GREEN + "\n[+] Enter the targets emails (i.e example@gmail.com, pythonusers@gmail.com <: ")
    
    # while listOfTargets == " " or listOfTargets =="":
    #     listOfTargets = input(hcolors.RED + "[+] Enter the targets emails (i.e example@gmail.com, pythonusers@gmail.com <: ")

    address = input(hcolors.GREEN + '[+] Enter your address (i.e in case your email is anyone123@gmail.com, your address is anyone123) <: ')
    while address == "":
        address = input(hcolors.RED + '[+] Enter your address (i.e in case your email is anyone123@gmail.com, your address is anyone123) <: ')

    message = "Subject:{}\n\n{}".format(subject, bodyConent)    
    object.sendmail(address, target_context, message)

    loading(hcolors.GREEN + " Final moment, Please wait...", 16, 15)
    print(hcolors.GREEN + "\nSend successfully, Thanks for using!! Goodbye")
    object.quit

    



if __name__ == '__main__':
    banner()
    Start()
    