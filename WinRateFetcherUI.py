import PySimpleGUI as sg

# Some global constants and variables...
AppFont = 'Any 16'
sg.theme('DarkBlue3')
_VARS = {'clickCount': 0}

# The function that is going to be called, note how
# it selects the text field via a key...


def myFunction():
    _VARS['clickCount'] += 1
    window['-keyforText-'].update('Clicked: ' +
                                  str(_VARS['clickCount']) + ' times')
    print('called my Function')

# Here's where you set a layout and add UI widgets, note both
# the button function call and the text display key that matches the
# one on the previous function


layout = [[sg.Button('Summoner Name Search', key=lambda: myFunction(), font=AppFont),
           sg.Exit(font=AppFont)],
          [sg.Text('Not clicked yet', key='-keyforText-',
                   font=AppFont, size=(20, 4))]]

# Add everything under a window...

window = sg.Window('Window Title', layout)

# And finally add an event loop to catch events
# and behavior, pretty standard pattern


while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if callable(event):
        event()

window.close()