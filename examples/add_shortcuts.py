"""
This example demonstrates how to add global keyboard shortcuts.
"""

import webview


def quit():
    for win in reversed(webview.windows):
        win.destroy()


def new_window():
    print("New window")
    idx = len(webview.windows) + 1
    win = webview.create_window('Window {}'.format(idx), html='<h1>Hello world!</h1>')
    #add_shortcuts(win)


def add_shortcuts(win):
    win.add_shortcut("Ctrl+Q", quit)
    win.add_shortcut("F11", win.toggle_fullscreen)
    win.add_shortcut("Ctrl+N", new_window)


if __name__ == '__main__':
    window = webview.create_window('Main Window', html='<h1>Hello world!</h1>')
    webview.start(add_shortcuts, args=window, gui='qt')
