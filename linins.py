#!/usr/bin/env python3


import os
from os import chdir as cd
from sys import argv as args


import ParserLib


# some setup before running the rest of the program
SettingObj = ParserLib.SettingFile()




# main functionalities

#   debug option
def debug():
    SettingObj.load()
    if os.path.isfile( "InstallFile" ):
        ParserLib.InstallFile().debug( "InstallFile" )
        os.system( "clear" )
    else:
        print("[!] No installation file")
        exit(0)

#   install option
def install():
    SettingObj.load()
    if os.path.isfile( "InstallFile" ):
        ParserLib.InstallFile().execute( "InstallFile" )
    else:
        print("[!] No installation file")
        exit(0)


#   clone option
def clone( url ):
    os.system(  "git clone " + url  )
    current_directory = os.getcwd()
    cd(   url[  url.rindex( "/" )  :  ]   ) # change directory
    install()


#   setup option
def setup():
    settingObj = ParserLib.SettingFile()
    print( "What is the Linux disribution that you are using?" )
    print( "\t1)  Arch" )
    print( "\t2)  Fedora" )
    print( "\t3)  OpenSUSE" )
    print( "\t4)  CentOS" )
    print( "\t5)  Apline Linux" )
    print( "\t6)  Gentoo" )
    print( "\t7)  FreeBSD\n" )
    print( "\t8)  Debian" )
    print( "\t9)  Ubuntu" )
        
    user_choice = input( "write the number of your choice: " )
    if user_choice in [ "0" , "1" , "3" , "4" , "5" , "6" ]:
        ParserLib.settings.update( { "Distribution" : user_choice } )
        settingObj.save()
        print( "[!] saved" )
    else:
        print( "invalid option" )


#   settings option
def start_settings_interface():
    options ="""
1) change distribution
2) Exit\n
"""
    print( options )
    user_choice = input( "choice >  " )
    
    if user_choice == "1":
        print( "What is the Linux disribution that you are using?" )
        print( "\t0)  Debian" )
        print( "\t1)  Arch" )
        print( "\t2)  Fedora" )
        print( "\t3)  OpenSUSE" )
        print( "\t4)  Apline Linux" )
        print( "\t5)  Gentoo" )
        print( "\t6)  FreeBSD\n" )
        
        user_choice = input("write the number of your choice: ")
        
        
        valid_choices = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 ]
        
        if user_choice in valid_choices:
            ParserLib.settings[ "Distribtuion" ] = user_choice
            settingObj.save()
            print( "[*] saved" )
            exit(0)
        else:
            print( "[!] invalid option")
            exit(0)
        
    elif user_choice == "2":
        print( "[*] exited" )
        exit(0)
    
    else:
        print( "[!] invalid option" )




# main program execution
print("The Linux Installer   Linins 2021     version 0.1.0")

if len( args )  >  1:
    # install
    if  args[1] == "install":
        install()
    # debug
    elif args[1] == "debug":
        debug()
    # clone
    elif  args[1] == "clone"  and  len(args) == 3:
        if  "/" in args[2]:
            clone( url )
        else:
            print( "[!] invalid URL" )
    # settings
    elif args[1] == "settings":
        start_settings_interface()
    # setup
    elif args[1] == "setup":
        setup()
    # invalid arguements
    else:
        print("\nUsage:")
        print("    linins install\t    run the installtion scripts")
        print("    linins debug\t    debug the installtion scripts (for developers)")
        print("    linins clone [url]\t    clone a repository and install it")
        print("    linins setup\t    setting up the program")
        print("    linins settings\t    to access program's settings")
        exit(0)

else:
    print("\nUsage:")
    print("    linins install\t    run the installtion scripts")
    print("    linins debug\t    debug an installtion file (for developers)")
    print("    linins clone [url]\t    clone a repository and install it")
    print("    linins setup\t    setting up the program")
    print("    linins settings\t    to access program's settings")
    exit(0)
