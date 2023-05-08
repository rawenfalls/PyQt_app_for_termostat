from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
	app = QApplication(sys.argv)
	window = QMainWindow()

	window.setWindowTitle("test program")
	#window.setGeometry(0,0,1920,1080)
	window.setGeometry(0,0,2048,1152)

	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	application()