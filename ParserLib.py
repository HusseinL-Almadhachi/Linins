#/usr/bin/env python3

import os


settings = {}


""" in SettingFile class"""
class SettingFile:
    def __init__( self ):
        # this file stores the number that referes to the users distro and stores programs that needs root permissions
        self.SettingFile = "SettingFile"

    #   load settings from SettingFile    
    def load( self ):
        file_descriptor = open( self.SettingFile , "r" )
        for line in file_descriptor:
            feature , value = [   line[ : line.index( ":" ) ]   ,   line[ line.index( ":" ) + 1  :  -1  ]   ]
            settings[ feature ] = value
        file_descriptor.close()

    #   write changes to SettingFile
    def save( self ):
        file_descriptor = open( self.SettingFile , "w" )
        for key in settings:
            file_descriptor.write(  key   +  ":"  +  settings[ key ]  +  "\n"  )
        file_descriptor.close()



#   InstallFile
class InstallFile:
#   inintialisation
    def __init__( self ):
        file_descriptor = open( "HardwareInfo" , "r" )
        self.info = file_descriptor.read()
        file_descriptor.close()


#   check wether a particular software available
    def chack_hardware_device_availibility( self, device ):
        return  device in self.info


#   check wether a particular software available
    def check_software_availibility( self , path ):
        return  os.path.exists( path )


#   parse a line of script and 
    def parse( self , line_of_script ):
        self.line_of_script = line_of_script
        #     remove all charaters that exist in an index
        def remove_a_char_at( char , index ):
            while char == self.line_of_script[ index ]:
                self.line_of_script = self.line_of_script[ : index ] + self.line_of_script[  index + 1  :  ]
        
        # remove spaces from the beginning of the line
        remove_a_char_at( " " , 0 )
        
        
        #  don't parse emty lines
        if len(  self.line_of_script.replace(" ","").replace("\t","").replace("\n","")  ) == 0:
            print("[!] emty line !!!!!!")
            exit(0)
        
        #  distribution specific script
        elif self.line_of_script[ 0 ] == settings[ "Distribution" ]:
            # remove spaces at index [1]
            remove_a_char_at ( " " , 1 )
            self.script = self.line_of_script[ 1 : ]
            return self.script

        #  hardware specific script
        elif    "#" == self.line_of_script[ 0 ]:
            if    ":" in self.line_of_script    and    self.chack_hardware_device_availibility(   self.line_of_script[  1  :  self.line_of_script.index(":")  ]   ):
                remove_a_char_at(  " "  ,  self.line_of_script.index( ":" ) + 1  )
                self.script = self.line_of_script[  line_of_script.index( ":" ) + 1  :  ]
                return self.script
            else:
                return "#"
        

    #  software specific script
        elif    "@"  ==  self.line_of_script[ 0 ]:
            if    ":"  in  self.line_of_script[ 1 : ]    and    self.check_software_availibility(   self.line_of_script[  1  :  self.line_of_script.index(":")  ]   ):
                remove_a_char_at(  " "  ,  self.line_of_script.index( ":" ) + 1  )
                self.script = self.line_of_script[  self.line_of_script.index( ":" ) + 1  :  ]
                return  self.script
            else:
                return "#"
        
        
        #  general purpose script
        elif not self.line_of_script[ 0 ].isnumeric():
            remove_a_char_at ( " " , 0 )
            self.script = self.line_of_script
            return self.script
        else:
            return "#"
    

    def debug( self , installfile ):
        for  line  in  open( installfile ):
            os.system("clear")
            parsed = self.parse( line.replace( "\n" , "" ) )
            print( "\n\n================================================================" )
            print( ">>>>>>>>>>>>>>>>>>>> Installation process <<<<<<<<<<<<<<<<<<<<<<" )
            print( "----------------------------------------------------------------" )
            print(  "\nline of script = \""  +  line.replace( "\n" , "" )  +  "\""  )
            print(  "parsed line of script = \""  +  parsed  +  "\"\n\n"  )
            input( "           --- press enter to run the above script ---" )
            print( "result:\n" )
            os.system( parsed )
            print( "\n----------------------------------------------------------------" )
            print( ">>>>>>>>>>>>>>>>>> command has been executed <<<<<<<<<<<<<<<<<<" )
            print( "================================================================" )
            input( "\n\n             --- press enter to go to the next ---\n\n" )

    def execute( self , installfile ):
        for  line  in  open( installfile ):
            os.system(  self.parse( line )  )


