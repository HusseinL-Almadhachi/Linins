# The Linux Installer 
###Linins 2021   version 0.1.0 

Linins is souce code installer for compiling and installing source code with the ability to write scripts that runs when a specified operating systems or distribution exist, or  when a particular hardware device or software exist on the users computers. this project aim to make an automated installation possible  primarly for Linux and also other open source operating systems
---
## Introduction
if you wanted to make an open source project one of the biggest challenges that you have to face, is that your users uses a wide range of hardware devices , operating systems and software. and if your users do not have the needed technical knowladge, they cannot compile the source code and install all the required dependencies to uses the program or otherwise the the author of the project has to compile the source code for each operating system and in some cases for hardware devices or some software. so this software aims to solve this problem by providing you with the followings options to add to your shell script:

* You can specify a line of shell script to run only the user is using a certain Linux distribution or a certain operating system
* You can specify a line of shell script to run when a certain hardware device exist (e.g GPU , network adaptors)
* You can specify a line of shell script to run when a certain software path exist (e.g GCC , Python , Nim , R )
* You can clone any other additionl repositories
* You can clone repositories that support Linins Installation file's format "InstallFile" and install additional software that specified in those repositories installtion files without worrying about how to install them when you writing your installtion files

