from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class CountDownWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.interval = 10
        self.count = 0
        self.timer = QTimer(parent=self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_count)
        self.lcd_number = QLCDNumber(parent=self)
        layout = QVBoxLayout()
        layout.addWidget(self.lcd_number)
        self.setLayout(layout)
        self.timer.start()

    def do_count(self):
        self.count += 1
        self.lcd_number.display(self.count)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = CountDownWidget()
    screen.show()

    sys.exit(app.exec_())
