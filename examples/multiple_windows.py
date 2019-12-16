"""
This example demonstrates how to create and manage multiple windows
"""

import webview


def add_third_window(mainwin):
    # Create a new window after the loop started
    if not mainwin.shown.wait(10):
        print("Main window failed to start.")
    else:
        third_window = webview.create_window('Window #3', html='<h1>Third Window</h1>')


if __name__ == '__main__':
    # Master window
    master_window = webview.create_window('Window #1', html='<h1>First window</h1>')
    second_window = webview.create_window('Window #2', html='<h1>Second window</h1>')
    webview.start(add_third_window, args=master_window)
