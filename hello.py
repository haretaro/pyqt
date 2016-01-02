import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def on_click():
    print('hello hello hello')

def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    hello_button = QPushButton("hellohellohello")
    hello_button.clicked.connect(on_click)
    main_window.setCentralWidget(hello_button)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()

