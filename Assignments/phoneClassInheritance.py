# parent phone class
# universal attributes to be inherited by child classes
class Phone:
    make = 'Make Here'
    model = 'Model Here'
    number = '555-555-5555'

# child cell phone class
# cell phones uniquely have cameras, a company who provides service (carrier)
# and a network that it connects to in order to receive voice, text, data
class Cell_Phone(Phone):
    carrier = 'Carrier Here'
    hasCamera = True
    network = '4G'

# child land line phone class
# land line phones uniquely have optional voicemail (depending on age)
# land lines can also make use of multiple lines as they may or may not have call-handling
class Land_Line_Phone(Phone):
    hasVoicemail = False
    numberOfLines = 2
    
