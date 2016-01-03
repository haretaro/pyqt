from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class CountDownWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.interval = 10
        self.timer = QTimer(parent=self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_countdown)
        self.timer.start()

    def do_countdown(self):
        print('hoge')

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = CountDownWidget()
    screen.show()

    sys.exit(app.exec_())
