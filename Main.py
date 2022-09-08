# source https://www.youtube.com/watch?v=S41RPtdWe78 + google
from cProfile import label
import kivy
import kivy.uix.button as button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json

DATA_FILE='my_contacts.json'

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        # add columns
        self.cols = 2
        # add widgets
        self.add_widget(Label(text="Name: ", font_size=40))
        # add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Cell: ", font_size=40))
        # add input box
        self.cell = TextInput(multiline=False)
        self.add_widget(self.cell)

        # Create a submit button
        self.submit = Button(text="Add Contact", font_size=40)
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

# -------------------------------------------------------------------------------------
        self.btn1 = Button(text='Print all countacts', font_size=40)
        self.btn1.bind(on_press=self.print)
        self.add_widget(self.btn1)
# -------------------------------------------------------------------------------------

        self.btn2 = Button(text='Search countacts', font_size=40)                                   
        self.btn2.bind(on_press=self.searchfunc)                                           
        self.add_widget(self.btn2)
# -------------------------------------------------------------------------------------
        self.btn3 = Button(text='Delete countacts', font_size=40)                                   
        self.btn3.bind(on_press=self.dell)                                           
        self.add_widget(self.btn3)


        
    # print in terminal what button was pressed



    def press(self, instance):
        contacts=load(DATA_FILE)
        name = self.name.text
        cell = self.cell.text
        contacts.append({"name": name ,"cell":cell})
        # print output inside the program!
        self.add_widget(Label(
            text=f"Added contact under the name {name} and his cell is:  {cell}"))
        # print the output in terminal
        print(f"Added {name} and telephone: {cell} ")
        save(DATA_FILE,contacts)
         # clear the input boxes
        self.name.text = ""
        self.cell.text = ""


    def print(self, instance):
        contacts=load(DATA_FILE)
        # print output inside the program!
        self.add_widget(Label(text=(str(contacts))))
        # print the output in terminal


    def searchfunc(self, instance):
        contacts=load(DATA_FILE)
        self.add_widget(Button(text=" "))
        self.add_widget(Button(text=" "))
        self.add_widget(Label(text=(str(contacts)))) # prints all contacts
        self.add_widget(Button(text=" "))
        self.add_widget(Label(text="Who to search for? ", font_size=40))
        self.seachName = TextInput(multiline=False) # text to in
        self.add_widget(self.seachName)
        self.add_widget(Button(text="Search",on_press=self.search, font_size=40))
        



    def search(self, instance):
        contacts=load(DATA_FILE)
        name = self.seachName.text
        cell = self.cell.text
        contact_2_search=name
        for contact in contacts:
         if contact['name'] == contact_2_search:
            self.add_widget(Label(text=f"Found contact under the name: {name} and his phone is {contact['cell']}", font_size=40))
            return
        else:
            self.add_widget(Label(text=f"Contact not found", font_size=40))
            return
    

    def dell(self, instance):
        contacts=load(DATA_FILE)
        self.add_widget(Button(text="-------"))
        self.add_widget(Button(text="-------"))
        self.add_widget(Label(text=(str(contacts)))) # prints all contacts
        self.add_widget(Label(text="name of delete contact?  ", font_size=40))
        self.killc = TextInput(multiline=False) # text to in
        self.add_widget(self.killc)
        self.add_widget(Button(text="Delete",on_press=self.kill, font_size=40))



    def kill(self, instance):
        contacts=load(DATA_FILE)
        name = self.killc.text
        contact_2_del=name
        for contact in contacts:
           if contact["name"] == contact_2_del:
            self.add_widget(Label(text=f"deleted a contact under the name: {name}", font_size=40))
            contacts.remove(contact)
            save(DATA_FILE,contacts)
            return
        else:
            self.add_widget(Label(text=f"Contact not found", font_size=40))
            return

   


def load(DATA_FILE):
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        save(DATA_FILE,[])
        return []        
    
def save(DATA_FILE,contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f)

    

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()



# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&&&&&@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&
# &&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&&@@&
# &&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&@&&&&&&&&
# &&&&@@@@@@@@@@@@@@@@@@@@@&&&&&&%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&&&&&&&&
# &@&@@@@@@@@&@&&&@@@@&&&%%######%##%%#####%%%%&&&@@@@@@@@@@@@@@@@@@@@&@&&&&&&&&&&
# &&@@@@@@@&&&%&&&@@@&%&%#(*********************/(#&&@@@@@%&@@@@@@@@@@@@@@&&@@@@&@
# @&@@@@@@@@&%&&&@%%&%%#(/**,,,,,,,,,,,,,,,**********/((###%#%&@@@@@@@@@@@@@@@@@&%
# &@@@@@@@@&%&%%%%&%%%#(/*,,,,,,,,,,,,,,,,,,,,***********///(((#&@@@@@@@@@@@@@@@(/
# @@@@@@@@&&&&&&%%%###(//*,,,,,,,,,,,,,,,,,,,,****,*******////((#@@@@@@@@@@@@@@@&(
# @@@@&@@@&&%&%&###((((/****,,,,,,,,,,,,,,,,,,,,,,*******/***//((%@@@@@@@@@@@@@@@#
# &&&&&@@@@&%%%%###((((/****,,,,,,,,,,,,,,,,,,,,,,*************//#@@@@@@@@@@@@@@@%
# &&&&#%@@&&%%#(##(((((/*******,,,,,,,,,,,,,,,,*,,**************/(%@@@@@@@@@@@@@@@
# //**/(@&&%%#(##((#(/*********,*,,,,,,,,,,,,,,,,,,*,****,,,***//#&@@@@@@@@@@@@@@@
# *****/%&%%%%####((/************,,,,,/*****,,,*,,***********/(#@@@@@@@@@@@@@@@@@@
# *******%#(%%#####(/**********,,,,*/((#&&&&&@&@@&%/((/**//(#&@@&&&@@@@@@@@@@@@@@@
# ***/##*,,**(%%##((*************(%###(((((#%%%%%%%%%#((((%@@@@&@@@@@@@@@@@@@@@@@@
# ****/%///*,*/%#((/**********////////((#%%&&@&%%%%###((#@@@@@&&&&&@@@@@@@@@@@@@@@
# ****//*//((/*/((//*********/*/((#&&&@@@@#(#&&@&%%#*,,,,(@&&&&%%##%@@@@@@@@@@@@@@
# **////**/(///*(//**************/**/(//((/((##((*,,,,,,.,*((((((((#@@@@@@@@@@@@@@
# ///((((,,****,*(//******,*,,,,*,,,**/(((((///*,,,,,,,,,,,*(/////(#@@@@@@@@@@@@@@
# (###%%%#/*,*/**/((///*****,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,*////(#@@@@@@@@@@@@@@
# &&&&&@@@&//(*/(((##((//****,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,**//(#@@@@@@@@@@@@@@
# @@@@@@@@@@@(***/(####((//****,,,,,,,,,,,,,,,,,,****,,,,,,,,,,*/((#@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@&&%##(((///****,,,,,,,,,,,,,,*****,,,,,,,,***(#((%@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@%%#%(((((///*********,**,,****,*/((#%%%%%%&@&%##@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@#####(((((/////*/************,,,,,,*/((%%%%&%%&&@@@@@@@@@@@@@@@
# &@@@@@@@@@@@@@@@@###((##(((//////////******//***************(&&%@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@###(((##((////////***//#%%#(//***//###%%&&&%%@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@%###((((##((//////////(((//**//((//////(/(#%&@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@%(##((((((#(((////((////*********///(####%&@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@&(((((((((((##(((////////*****///(((#((##@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@((((((((((((((##((////////********///(&@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@&(((((((((((((((#%#(#((////*/**//((#@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((####%%#######%&@#@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@&(((((((((((###########%@@@@@#@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(((((((((####(((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(//((((((((/((((#@@@@@@@/@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(/(((((////((@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((////////(@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((((/((%@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(((&@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@

#             @@@@@@@      @@@@  @@@@
#           @@        @@   @@@@  @@@@                                
#          @@   #@@@   @@        @@@@                                              
#          @@ #@#       @  @@@@  @@@@       @@@@   @@@  @@@@@@@@@@                      
#          @@ &@*       @  @@@@  @@@@        @@@# @@@     .@@@@@@@                      
#           @@  #@@@  %@   @@@@  @@@@@@@      @@@@@@   (@@@   *@@@                      
#             @@     @@    @@@@  @@@@@@@       @@@@*    @@@@@@ @@@#                     
#              ,@@@@@                      @@@@@@*                   