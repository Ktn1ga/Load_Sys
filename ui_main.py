import warnings
import os


# 忽略警告
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings(action='ignore')
from func.mainwindow import Ui_MainWindow
from sys import argv, exit
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QFile


if __name__ == '__main__':
    app = QApplication(argv)


    window = QMainWindow()
    ui = Ui_MainWindow(window)
    # #
    # with open('mystyle.qss') as f:
    #     qss = f.read()
    # window.setStyleSheet(qss)

    window.show()

    exit(app.exec_())