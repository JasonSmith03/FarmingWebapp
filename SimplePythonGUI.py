import PySimpleGUI as sg

# Demo of how columns work
# window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to window layouts, they are a list of lists of elements.

#window = sg.Window('Plant Health')                                   # blank window

# Column layout
box1 = [
    [sg.Text('Cedar Box 1', key='-CEDAR1TEXT-', expand_x=True, justification='center')],
    [sg.Image(r'H:\FarmingApp\FarmingWebapp\assets\tomatoplantpng.png', expand_x=True, expand_y=True, key='-TOMATO-', pad=(0, 60))]
]

box2 = [
    [sg.Text('Cedar Box 2', key='-CEDAR2TEXT-', expand_x=True, justification='center')],
    [sg.Image(r'H:\FarmingApp\FarmingWebapp\assets\pepperplantpng.png', expand_x=True, expand_y=True, key='-PEPPER-', pad=(0, 60))]
]

layout = [
    [
        sg.Column(box1, expand_x=True, expand_y=True), 
        sg.VSeparator(pad=(60, 0)),
        sg.Column(box2, expand_x=True, expand_y=True)
    ]
]

window = sg.Window('Plant Health', layout, resizable=True)

# Display the window and get values
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()

#sg.Popup(event, values, line_width=200)