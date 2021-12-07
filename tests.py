from io import BytesIO
from PIL import Image, ImageDraw
import PySimpleGUI as sg


def icon(check):
    box = (20, 20)
    background = (255, 255, 255, 0)
    rectangle = (3, 3, 29, 29)
    line = ((4, 12), (10, 18), (18, 4))
    im = Image.new('RGBA', box, background)
    draw = ImageDraw.Draw(im, 'RGBA')
    draw.rectangle(rectangle, outline='black', width=3)
    if check == 1:
        draw.line(line, fill='black', width=3, joint='curve')
    elif check == 2:
        draw.line(line, fill='grey', width=3, joint='curve')
    with BytesIO() as output:
        im.save(output, format="PNG")
        png = output.getvalue()
    return png


check = [icon(0), icon(1), icon(2)]

headings = ['President', 'Date of Birth', '1', '2', '3']
data = [
    ['Ronald Reagan', 'February 6'],
    ['Abraham Lincoln', 'February 12'],
    ['George Washington', 'February 22'],
    ['Andrew Jackson', 'March 15'],
    ['Thomas Jefferson', 'April 13'],
    ['Harry Truman', 'May 8'],
    ['John F. Kennedy', 'May 29'],
    ['George H. W. Bush', 'June 12'],
    ['George W. Bush', 'July 6'],
    ['John Quincy Adams', 'July 11'],
    ['Garrett Walker', 'July 18'],
    ['Bill Clinton', 'August 19'],
    ['Jimmy Carter', 'October 1'],
    ['John Adams', 'October 30'],
    ['Theodore Roosevelt', 'October 27'],
    ['Frank Underwood', 'November 5'],
    ['Woodrow Wilson', 'December 28'],
]

treedata = sg.TreeData()
for president, birthday in data:
    treedata.Insert('', president, president, values=[birthday]+[1, 2, 3],
                    icon=check[0])

sg.theme('LightPurple')
sg.set_options(font=('Helvetica', 16))
layout = [
    [sg.Input("hello")],
    [sg.Tree(data=treedata, headings=headings[1:], auto_size_columns=True,
             num_rows=10, col0_width=20, key='-TREE-', row_height=48, metadata=[],
             show_expanded=False, enable_events=True,
             select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
    [sg.Button('Quit')]
]
window = sg.Window('Tree as Table', layout, finalize=True)
tree = window['-TREE-']
tree.Widget.heading("#0", text=headings[0])  # Set heading for column #0

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    elif event == '-TREE-':
        president = values['-TREE-'][0]
        print(president)
        if president in tree.metadata:
            tree.metadata.remove(president)
            tree.update(key=president, icon=check[0])
        else:
            tree.metadata.append(president)
            tree.update(key=president, icon=check[1])

window.close()
