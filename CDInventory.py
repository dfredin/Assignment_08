#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Dfredin, 2022-Nov-28, added code to create classes and methods
#------------------------------------------#

# -- DATA -- #
lstOfCDObjects = []
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object
flag = bool() # boolean flag for file check
import pickle # allows storage to .dat files

class CD:
    """ Stores data about a CD:
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        add_cd: Function that takes new CD data and creates a new CD while appending to list
    """
    #--- Fields ---#
    numCDs = 0
    #--- Constructor ---#
    def __init__(self, ID, title, artist):
        #--- Attributes ---#
        self.__cd_id = ID
        self.__cd_title = title
        self.__cd_artist = artist
        CD.numCDs +=1
        
    #--- Properties ---#
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if not str(value).isnumeric():
            raise Exception('The CD ID must be a number!')
        else:
            self.__cd_id = value
        
    @property
    def cd_title(self):
        return self.__cd_title
        
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    #--- Methods ---#
    @staticmethod
    def add_cd(newCD):
        """ Adds new CD to list of CDs (lstOfCDObjects)
        Args:
            newCD (CD): Object CD consisting of CD data.            
        Returns:
            None.
        """
        lstOfCDObjects.append(newCD)          
        
# -- PROCESSING -- #
class FileIO:
    """ Processes data to and from file:
    properties:
        None.
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """
    #--- Methods ---#
    @staticmethod
    def load_inventory(file_name):
        """ Function to manage data ingestion from file to a list of CDs
            Reads the data from file identified by file_name into a 2D table
            (list of CDs) table one line in the file represents one CD row in table.
        Args:
            file_name (string): name of file used to read the data from
            table (list of CDs): 2D data structure (list of CDs) that holds the data during runtime
        Returns:
            table (list of CDs): 2D data structure that contains the file data.
        """    
        try:
            with open(file_name, 'rb') as objFile:
                if objFile == None:
                    table = []
                    return table
                else:
                    table = pickle.load(objFile)
                    return table

        except FileNotFoundError as e:
            with open(file_name, 'ab+') as objFile:
                table = []
                print('\nERROR! Data file not found! \nAn empty file has now been created.\n')
                print(e)
                print()
                return table
      
    @staticmethod
    def save_inventory(file_name, table):
        """ Function that overwrites the new data input by the user into the named dat file
        Args:
            file_name (string): name of file used to write the data to.
            table (list): data structure that holds the data during runtime.
        Returns:
            None.
        """        
        with open(file_name, 'wb') as objFile:
            pickle.dump(table, objFile)    

# -- PRESENTATION (Input/Output) -- #
class IO:
    """ Retrieves input from the user and displays output of menu and inventory:
    properties:
        None.
    methods:
        print_menu: Displays a menu of choices to the user
        menu_choice: Gets user input for menu selection
        show_inventory: Displays current inventory table
        get_CD: Retrieves input from user and returns an object CD 
    """
    #--- Methods ---#
    @staticmethod
    def print_menu():
        """ Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """
        print('------Menu------\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')
        
    @staticmethod
    def menu_choice():
        """ Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice    
    
    @staticmethod
    def show_inventory(table):
        """ Displays current inventory table
        Args:
            table (list of CDs): 2D data structure (list of CDs) that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print('{}\t{} (by: {})'.format(cd.cd_id, cd.cd_title, cd.cd_artist))

        print('======================================')
    
    @staticmethod
    def get_CD():
        """ Retrieves input from user and returns an object CD        
        Returns:
            CD: Object of CD that contains ID, CD title, and CD artist.
        """
        while True:
            try: 
                strID = int(input('Enter ID: ').strip())
                break
            except ValueError as e:
                print('\nERROR! Entered ID was not an integer. \nPlease enter an integer ID.\n')
                print(e)
                print()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return CD(strID, strTitle, strArtist)
            
# -- Main Body of Script -- #
lstOfCDObjects = FileIO.load_inventory(strFileName) # File not found error handling
while True:
    IO.print_menu()
    IO.show_inventory(lstOfCDObjects)
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        print('Ending program...')
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('Reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            continue
    elif strChoice == 'a':
        CD.add_cd(IO.get_CD())   
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)   
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')