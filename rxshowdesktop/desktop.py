import os
from subprocess import call, check_output


# show desktop
def show():
    return call('wmctrl -k on'.split())

# unshow / hide desktop
def hide():
    return call('wmctrl -k off'.split())

# toggle desktop
def toggle():
    return show() if hidden() else hide()

# returns true if showing desktop
def hidden():
    return 'off' in str(check_output('wmctrl -m | grep "showing the desktop"'.split())).lower()

# return true if desktop is hidden
def showing():
    return not hidden()

# show icon location
def locate():
    icons_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')
    icons = []
    for (dirpath, dirnames, filenames) in os.walk(icons_path):
        icons.extend(filenames)
    for icon in icons:
        print(os.path.join(icons_path, icon))
