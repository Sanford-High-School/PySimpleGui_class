# Write your code here :-)
import PySimpleGUI as sg


def create_cow():
    pass

def read_cow():
    pass

def update_cow():
    pass

def delete_cow():
    pass

def show_crud():
    sg.theme('DarkAmber')
    layout = [ [sg.Button('New Cow'),
                sg.Button('Show Cow'),
                sg.Button('Edit Cow'),
                sg.Button('Delete Cow'),
                sg.Button('Quit')] ]

    # Create the Window
    window = sg.Window('Cattle Herd', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
            break
        print('You entered ', event)

    window.close()
    return event

# main program

# show form to get CRUD
print(show_crud())








sg.theme('DarkAmber')   # Add some color
# All the stuff inside your window.
layout = [  [sg.Text('Enter the Information for a Cow')],
            [sg.Text('Cow ID '), sg.InputText()],
            [sg.Text('Cow Name '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Cattle Herd', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0],values[1])


window.close()
