from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtSql
from PyQt5 import QtChart

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from collections import Counter




import sklearn

from sklearn.metrics import mean_absolute_percentage_error as MAPE
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.preprocessing import MinMaxScaler


#资源文件
import func.res_rc

from func.dialog import Ui_Dialog_data

from func.save_result import *


import re
import time

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN



from func.fore import *



mycolor = [[255, 0, 0], [0, 255, 0], [0, 0, 255],
           [255, 255, 0], [255, 0, 255], [0, 255, 255],
           [  0,  0,128], [  0,128, 0], [128, 00, 0],
           [128, 128, 0], [128,  0,128], [0, 128, 128],
           [  0, 0, 64], [0, 64, 0], [64, 0,0],
           [64, 64, 192], [64, 192, 64], [192, 64, 64],
           [ 0, 0, 32], [0, 32, 0]]

class Ui_MainWindow(object):

    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.setEnabled(True)
        Mainwindow.resize(1280, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/auto_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mainwindow.setWindowIcon(icon)
        Mainwindow.setWindowOpacity(1.0)
        Mainwindow.setStyleSheet("")
        Mainwindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Mainwindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         " border-image: url(:/images/resources/bj.png);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_1check = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1check.sizePolicy().hasHeightForWidth())
        self.btn_1check.setSizePolicy(sizePolicy)
        self.btn_1check.setStyleSheet("QPushButton{\n"
                                      " image-position: left;                   \n"
                                      "    padding-right: 15px;    \n"
                                      "    image: url(:/images/resources/数据查看.svg);\n"
                                      "background-color: rgba(18, 107, 214,100);\n"
                                      "  \n"
                                      "                   font:bold 18px;                       \n"
                                      "                   color:rgba(255,255,255,100);                \n"
                                      "                   padding:20px; \n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      " QPushButton:hover{\n"
                                      "                   background-color:rgb(200,225,255);\n"
                                      "                   border-color:rgba(255,255,255,200);\n"
                                      "                   color:rgba(0,0,0,200);\n"
                                      "                font:bold 24px;\n"
                                      "                   }")
        self.btn_1check.setObjectName("btn_1check")
        self.verticalLayout.addWidget(self.btn_1check)
        self.btn_2show = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2show.sizePolicy().hasHeightForWidth())
        self.btn_2show.setSizePolicy(sizePolicy)
        self.btn_2show.setStyleSheet("QPushButton{\n"
                                     " image-position: left;\n"
                                     "                       padding-right: 15px;\n"
                                     "    image: url(:/images/resources/负荷监控.svg);\n"
                                     "\n"
                                     "background-color: rgba(18, 107, 214,100);\n"
                                     "  \n"
                                     "                   font:bold 18px;                       \n"
                                     "                   color:rgba(255,255,255,100);                \n"
                                     "                   padding:20px; \n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     " QPushButton:hover{\n"
                                     "                   background-color:rgb(200,225,255);\n"
                                     "                   border-color:rgba(255,255,255,200);\n"
                                     "                   color:rgba(0,0,0,200);\n"
                                     "                font:bold 24px;\n"
                                     "                   }")
        self.btn_2show.setObjectName("btn_2show")
        self.verticalLayout.addWidget(self.btn_2show)
        self.btn_3clus = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3clus.sizePolicy().hasHeightForWidth())
        self.btn_3clus.setSizePolicy(sizePolicy)
        self.btn_3clus.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_3clus.setStyleSheet("QPushButton{\n"
                                     " image-position: left;\n"
                                     "\n"
                                     "padding-right: 15px;\n"
                                     "    image: url(:/images/resources/负荷聚类.svg);\n"
                                     "\n"
                                     "background-color: rgba(18, 107, 214,100);\n"
                                     "  \n"
                                     "                   font:bold 18px;                       \n"
                                     "                   color:rgba(255,255,255,100);                \n"
                                     "                   padding:20px; \n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     " QPushButton:hover{\n"
                                     "                   background-color:rgb(200,225,255);\n"
                                     "                   border-color:rgba(255,255,255,200);\n"
                                     "                   color:rgba(0,0,0,200);\n"
                                     "                font:bold 22px;\n"
                                     "                   }")
        self.btn_3clus.setObjectName("btn_3clus")
        self.verticalLayout.addWidget(self.btn_3clus)
        self.btn_4fore = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4fore.sizePolicy().hasHeightForWidth())
        self.btn_4fore.setSizePolicy(sizePolicy)
        self.btn_4fore.setStyleSheet("QPushButton{\n"
                                     " image-position: left;\n"
                                     "                       padding-right: 15px;\n"
                                     "    image: url(:/images/resources/负荷预测.svg);\n"
                                     "\n"
                                     "background-color: rgba(18, 107, 214,100);\n"
                                     "  \n"
                                     "                   font:bold 18px;                       \n"
                                     "                   color:rgba(255,255,255,100);                \n"
                                     "                   padding:20px; \n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     " QPushButton:hover{\n"
                                     "                   background-color:rgb(200,225,255);\n"
                                     "                   border-color:rgba(255,255,255,200);\n"
                                     "                   color:rgba(0,0,0,200);\n"
                                     "                font:bold 24px;\n"
                                     "                   }")
        self.btn_4fore.setObjectName("btn_4fore")
        self.verticalLayout.addWidget(self.btn_4fore)
        self.text_message = QtWidgets.QTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text_message.setFont(font)
        self.text_message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_message.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
                                        "font:15px;                       \n"
                                        "color:rgba(255,255,255,200);   ")
        self.text_message.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.text_message.setObjectName("text_message")
        self.verticalLayout.addWidget(self.text_message)
        self.btn_help = QtWidgets.QPushButton(self.groupBox)
        self.btn_help.setStyleSheet("QPushButton{\n"
                                    "image-position: center;                   \n"
                                    "padding-right: 1px;\n"
                                    "image: url(:/images/resources/帮助中心.png);\n"
                                    "background-color: rgba(255, 255, 255,0);\n"
                                    "font:18px;\n"
                                    "color:rgba(255,255,255,100)\n"
                                    "}\n"
                                    "\n"
                                    " QPushButton:hover{\n"
                                    "color:rgba(0,0,0,200);\n"
                                    "font:18px;                   \n"
                                    "}\n"
                                    "")
        self.btn_help.setObjectName("btn_help")
        self.verticalLayout.addWidget(self.btn_help)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 5)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.page0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem1, 0, 2, 1, 1)
        self.p0_textBrowser = QtWidgets.QTextBrowser(self.page0)
        self.p0_textBrowser.setStyleSheet("background-color: rgba(0, 0, 0,100);\n"
                                          "border-style:inset;                  \n"
                                          "border-width:3px;                    \n"
                                          "border-radius:5px;                   \n"
                                          "border-color:rgba(200,200,255,200);   \n"
                                          "")
        self.p0_textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.p0_textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.p0_textBrowser.setLineWidth(0)
        self.p0_textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.p0_textBrowser.setCursorWidth(4)
        self.p0_textBrowser.setObjectName("p0_textBrowser")
        self.gridLayout_26.addWidget(self.p0_textBrowser, 0, 1, 1, 1)
        self.gridLayout_26.setColumnStretch(0, 1)
        self.gridLayout_26.setColumnStretch(1, 5)
        self.gridLayout_26.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setStyleSheet("")
        self.page1.setObjectName("page1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.p1_groupBox = QtWidgets.QGroupBox(self.page1)
        self.p1_groupBox.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:5px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font:bold 18px;                       \n"
                                       "                   color:rgb(255,255,255);                \n"
                                       "                   padding:6px; \n"
                                       "}")
        self.p1_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_groupBox.setFlat(True)
        self.p1_groupBox.setObjectName("p1_groupBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.p1_groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_10 = QtWidgets.QGroupBox(self.p1_groupBox)
        self.groupBox_10.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:1px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font: 18px;                       \n"
                                       "                   color:rgb(2,2,2);                \n"
                                       "                   padding:6px; \n"
                                       "}\n"
                                       "\n"
                                       "QRadioButton{\n"
                                       "font: 18px;                       \n"
                                       "color:rgb(2,2,2);                \n"
                                       "padding:6px; \n"
                                       "}\n"
                                       "\n"
                                       " \n"
                                       "QComboBox{\n"
                                       "background-color: rgba(255, 255, 255,10);\n"
                                       "border:1px solid rgba(228,228,228,100);\n"
                                       "border-radius:5px 5px 0px 0px;\n"
                                       "font-size:18px;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QComboBox QAbstractItemView {\n"
                                       "    outline: 0px solid gray;   /* 选定项的虚框 */\n"
                                       "    border: 1px solid raga(228,228,228,100);   /* 整个下拉窗体的边框 */\n"
                                       "    color: blue;\n"
                                       "    background-color: white;   /* 整个下拉窗体的背景色 */\n"
                                       "    selection-background-color: lightblue;   /* 整个下拉窗体被选中项的背景色 */\n"
                                       "}")
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.p1_cb_paixu = QtWidgets.QComboBox(self.groupBox_10)
        self.p1_cb_paixu.setStyleSheet("")
        self.p1_cb_paixu.setObjectName("p1_cb_paixu")
        self.p1_cb_paixu.addItem("")
        self.p1_cb_paixu.addItem("")
        self.p1_cb_paixu.addItem("")
        self.p1_cb_paixu.addItem("")
        self.gridLayout_24.addWidget(self.p1_cb_paixu, 0, 0, 2, 1)
        self.p1_rb_paixu_zheng = QtWidgets.QRadioButton(self.groupBox_10)
        self.p1_rb_paixu_zheng.setStyleSheet("")
        self.p1_rb_paixu_zheng.setChecked(True)
        self.p1_rb_paixu_zheng.setObjectName("p1_rb_paixu_zheng")
        self.gridLayout_24.addWidget(self.p1_rb_paixu_zheng, 0, 1, 1, 1)
        self.p1_rb_paixu_fan = QtWidgets.QRadioButton(self.groupBox_10)
        self.p1_rb_paixu_fan.setStyleSheet("")
        self.p1_rb_paixu_fan.setObjectName("p1_rb_paixu_fan")
        self.gridLayout_24.addWidget(self.p1_rb_paixu_fan, 1, 1, 1, 1)
        self.gridLayout_24.setColumnStretch(0, 2)
        self.gridLayout_24.setColumnStretch(1, 1)
        self.gridLayout_10.addWidget(self.groupBox_10, 0, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem4, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem6, 3, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem8, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.p1_groupBox)
        self.label_8.setStyleSheet("QLabel{\n"
                                   "font:13px;                       \n"
                                   "color:rgba(0,0,0,100);                \n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 2, 0, 1, 4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.p1_groupBox)
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:5px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "QLabel{\n"
                                      "font:18px;                       \n"
                                      "color:rgb(2,2,2);                \n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox{\n"
                                      "padding-right: 15px; /* make room for the arrows */\n"
                                      "border:1px solid rgba(228,228,228,100);\n"
                                      "border-radius:5px;       \n"
                                      "  \n"
                                      "background-color: rgba(255, 255, 255,10);\n"
                                      "font:18px;      \n"
                                      "color:rgb(2,2,2);\n"
                                      "} \n"
                                      "\n"
                                      "QSpinBox::up-button {\n"
                                      "border-image: url(:/images/resources/spinbox-up.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button {\n"
                                      "border-image: url(:/images/resources/spinbox-down.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::up-button:pressed {\n"
                                      "margin-top:3px;\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button:pressed {\n"
                                      "margin-bottom:3px;\n"
                                      "}\n"
                                      "")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.p1_sb_month = QtWidgets.QSpinBox(self.groupBox_6)
        self.p1_sb_month.setMaximum(12)
        self.p1_sb_month.setObjectName("p1_sb_month")
        self.gridLayout_20.addWidget(self.p1_sb_month, 0, 7, 1, 1)
        self.p1_sb_day = QtWidgets.QSpinBox(self.groupBox_6)
        self.p1_sb_day.setMaximum(31)
        self.p1_sb_day.setObjectName("p1_sb_day")
        self.gridLayout_20.addWidget(self.p1_sb_day, 0, 10, 1, 1)
        self.label_0 = QtWidgets.QLabel(self.groupBox_6)
        self.label_0.setStyleSheet("")
        self.label_0.setObjectName("label_0")
        self.gridLayout_20.addWidget(self.label_0, 0, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox_6)
        self.label_1.setStyleSheet("font:16px;                       \n"
                                   "color:rgb(2,2,2);                ")
        self.label_1.setObjectName("label_1")
        self.gridLayout_20.addWidget(self.label_1, 0, 4, 1, 1)
        self.p1_sb_year = QtWidgets.QSpinBox(self.groupBox_6)
        self.p1_sb_year.setMaximum(3000)
        self.p1_sb_year.setSingleStep(1)
        self.p1_sb_year.setProperty("value", 0)
        self.p1_sb_year.setObjectName("p1_sb_year")
        self.gridLayout_20.addWidget(self.p1_sb_year, 0, 3, 1, 1)
        self.p1_sb_zoneid = QtWidgets.QSpinBox(self.groupBox_6)
        self.p1_sb_zoneid.setStyleSheet("")
        self.p1_sb_zoneid.setMaximum(21)
        self.p1_sb_zoneid.setObjectName("p1_sb_zoneid")
        self.gridLayout_20.addWidget(self.p1_sb_zoneid, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setStyleSheet("font:16px;                       \n"
                                   "color:rgb(2,2,2);                ")
        self.label_2.setObjectName("label_2")
        self.gridLayout_20.addWidget(self.label_2, 0, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setStyleSheet("font:16px;                       \n"
                                   "color:rgb(2,2,2);                ")
        self.label_3.setObjectName("label_3")
        self.gridLayout_20.addWidget(self.label_3, 0, 11, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_6, 0, 0, 1, 2)
        self.groupBox_9 = QtWidgets.QGroupBox(self.p1_groupBox)
        self.groupBox_9.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      " image-position: left;\n"
                                      "\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:2px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgba(255,255,255,100);   \n"
                                      "                   font:18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "\n"
                                      "}\n"
                                      " QPushButton:hover{\n"
                                      "                   background-color:rgb(200,225,255);\n"
                                      "                   border-color:rgba(255,255,255,200);\n"
                                      "                   color:rgba(0,0,0,200);\n"
                                      "font:bold 20px;\n"
                                      "                   }\n"
                                      "\n"
                                      "QLineEdit{\n"
                                      "border:1px solid rgba(228,228,228,100);\n"
                                      "font:18px;                       \n"
                                      "color:rgba(5,5,50,1);     \n"
                                      "} ")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.p1_lineEdit_sql = QtWidgets.QLineEdit(self.groupBox_9)
        self.p1_lineEdit_sql.setStyleSheet("")
        self.p1_lineEdit_sql.setText("")
        self.p1_lineEdit_sql.setObjectName("p1_lineEdit_sql")
        self.gridLayout_23.addWidget(self.p1_lineEdit_sql, 0, 0, 1, 1)
        self.p1_pushButton_search = QtWidgets.QPushButton(self.groupBox_9)
        self.p1_pushButton_search.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.p1_pushButton_search.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/查询.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p1_pushButton_search.setIcon(icon1)
        self.p1_pushButton_search.setIconSize(QtCore.QSize(20, 20))
        self.p1_pushButton_search.setAutoRepeat(False)
        self.p1_pushButton_search.setObjectName("p1_pushButton_search")
        self.gridLayout_23.addWidget(self.p1_pushButton_search, 0, 1, 1, 1)
        self.gridLayout_23.setColumnStretch(0, 5)
        self.gridLayout_23.setColumnStretch(1, 1)
        self.gridLayout_10.addWidget(self.groupBox_9, 1, 0, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.p1_groupBox)
        self.groupBox_8.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      " image-position: left;\n"
                                      "\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:2px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgba(255,255,255,100);   \n"
                                      "                   font:18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "\n"
                                      "}\n"
                                      " QPushButton:hover{\n"
                                      "                   background-color:rgb(200,225,255);\n"
                                      "                   border-color:rgba(255,255,255,200);\n"
                                      "                   color:rgba(0,0,0,200);\n"
                                      "font:bold 20px;\n"
                                      "                   }")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.p1_btn_add = QtWidgets.QPushButton(self.groupBox_8)
        self.p1_btn_add.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/增加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p1_btn_add.setIcon(icon2)
        self.p1_btn_add.setObjectName("p1_btn_add")
        self.gridLayout_22.addWidget(self.p1_btn_add, 0, 0, 1, 1)
        self.p1_btn_save = QtWidgets.QPushButton(self.groupBox_8)
        self.p1_btn_save.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/resources/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p1_btn_save.setIcon(icon3)
        self.p1_btn_save.setObjectName("p1_btn_save")
        self.gridLayout_22.addWidget(self.p1_btn_save, 0, 2, 1, 1)
        self.p1_btn_del = QtWidgets.QPushButton(self.groupBox_8)
        self.p1_btn_del.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/resources/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p1_btn_del.setIcon(icon4)
        self.p1_btn_del.setObjectName("p1_btn_del")
        self.gridLayout_22.addWidget(self.p1_btn_del, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_8, 1, 2, 1, 2)
        self.gridLayout_10.setColumnStretch(0, 2)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_10.setColumnStretch(2, 1)
        self.gridLayout_10.setColumnStretch(3, 1)
        self.gridLayout_10.setRowStretch(0, 1)
        self.gridLayout_10.setRowStretch(1, 1)
        self.gridLayout_4.addWidget(self.p1_groupBox, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 1, 2, 1, 1)
        self.p1_tableView = QtWidgets.QTableView(self.page1)
        self.p1_tableView.setStyleSheet("")
        self.p1_tableView.setObjectName("p1_tableView")
        self.gridLayout_4.addWidget(self.p1_tableView, 0, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 2)
        self.gridLayout_4.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem10, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem11, 1, 2, 1, 1)
        self.p2_groupBox = QtWidgets.QGroupBox(self.page2)
        self.p2_groupBox.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:5px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font:bold 18px;                       \n"
                                       "                   color:rgba(255,255,255,255);                \n"
                                       "                   padding:6px; \n"
                                       "}")
        self.p2_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_groupBox.setFlat(True)
        self.p2_groupBox.setObjectName("p2_groupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.p2_groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem12, 2, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem13, 2, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem14, 2, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem15, 2, 2, 1, 1)
        self.p2_groupBox_zoonid = QtWidgets.QGroupBox(self.p2_groupBox)
        self.p2_groupBox_zoonid.setStyleSheet("QGroupBox{\n"
                                              "                  padding-right: 15px;\n"
                                              "                   border-style:inset;                  \n"
                                              "                   border-width:1px;                    \n"
                                              "                   border-radius:5px;                   \n"
                                              "                   border-color:rgb(255,255,255);   \n"
                                              "                   font: 18px;                       \n"
                                              "                   color:rgb(2,2,2);                \n"
                                              "                   padding:6px; \n"
                                              "}\n"
                                              "QCheckBox::indicator::unchecked {\n"
                                              "    image: url(:/images/resources/checkbox_unchecked.png);\n"
                                              "width:25px;\n"
                                              "height:25px;\n"
                                              "\n"
                                              "}\n"
                                              "QCheckBox::indicator::checked {\n"
                                              "    image: url(:/images/resources/checkbox_checked.png);\n"
                                              "width:25px;\n"
                                              "height:25px\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "")
        self.p2_groupBox_zoonid.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.p2_groupBox_zoonid.setFlat(False)
        self.p2_groupBox_zoonid.setCheckable(False)
        self.p2_groupBox_zoonid.setObjectName("p2_groupBox_zoonid")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.p2_groupBox_zoonid)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.p2_cb_6 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_6.setObjectName("p2_cb_6")
        self.gridLayout_7.addWidget(self.p2_cb_6, 1, 0, 1, 1)
        self.p2_cb_14 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_14.setObjectName("p2_cb_14")
        self.gridLayout_7.addWidget(self.p2_cb_14, 2, 3, 1, 1)
        self.p2_cb_17 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_17.setObjectName("p2_cb_17")
        self.gridLayout_7.addWidget(self.p2_cb_17, 3, 1, 1, 1)
        self.p2_cb_5 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_5.setObjectName("p2_cb_5")
        self.gridLayout_7.addWidget(self.p2_cb_5, 0, 4, 1, 1)
        self.p2_cb_15 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_15.setObjectName("p2_cb_15")
        self.gridLayout_7.addWidget(self.p2_cb_15, 2, 4, 1, 1)
        self.p2_cb_20 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_20.setObjectName("p2_cb_20")
        self.gridLayout_7.addWidget(self.p2_cb_20, 3, 4, 1, 1)
        self.p2_cb_13 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_13.setObjectName("p2_cb_13")
        self.gridLayout_7.addWidget(self.p2_cb_13, 2, 2, 1, 1)
        self.p2_cb_4 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_4.setObjectName("p2_cb_4")
        self.gridLayout_7.addWidget(self.p2_cb_4, 0, 3, 1, 1)
        self.p2_cb_19 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_19.setObjectName("p2_cb_19")
        self.gridLayout_7.addWidget(self.p2_cb_19, 3, 3, 1, 1)
        self.p2_cb_18 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_18.setObjectName("p2_cb_18")
        self.gridLayout_7.addWidget(self.p2_cb_18, 3, 2, 1, 1)
        self.p2_cb_1 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_1.setObjectName("p2_cb_1")
        self.gridLayout_7.addWidget(self.p2_cb_1, 0, 0, 1, 1)
        self.p2_cb_11 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_11.setObjectName("p2_cb_11")
        self.gridLayout_7.addWidget(self.p2_cb_11, 2, 0, 1, 1)
        self.p2_cb_2 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_2.setObjectName("p2_cb_2")
        self.gridLayout_7.addWidget(self.p2_cb_2, 0, 1, 1, 1)
        self.p2_cb_16 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_16.setObjectName("p2_cb_16")
        self.gridLayout_7.addWidget(self.p2_cb_16, 3, 0, 1, 1)
        self.p2_cb_8 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_8.setObjectName("p2_cb_8")
        self.gridLayout_7.addWidget(self.p2_cb_8, 1, 2, 1, 1)
        self.p2_cb_12 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_12.setObjectName("p2_cb_12")
        self.gridLayout_7.addWidget(self.p2_cb_12, 2, 1, 1, 1)
        self.p2_cb_9 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_9.setObjectName("p2_cb_9")
        self.gridLayout_7.addWidget(self.p2_cb_9, 1, 3, 1, 1)
        self.p2_cb_10 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_10.setObjectName("p2_cb_10")
        self.gridLayout_7.addWidget(self.p2_cb_10, 1, 4, 1, 1)
        self.p2_cb_3 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_3.setStyleSheet("")
        self.p2_cb_3.setIconSize(QtCore.QSize(5, 5))
        self.p2_cb_3.setObjectName("p2_cb_3")
        self.gridLayout_7.addWidget(self.p2_cb_3, 0, 2, 1, 1)
        self.p2_cb_7 = QtWidgets.QCheckBox(self.p2_groupBox_zoonid)
        self.p2_cb_7.setObjectName("p2_cb_7")
        self.gridLayout_7.addWidget(self.p2_cb_7, 1, 1, 1, 1)
        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(3, 5)
        self.gridLayout_11.addWidget(self.p2_groupBox_zoonid, 1, 0, 1, 7)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem16, 2, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem17, 2, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem18, 0, 7, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem19, 1, 7, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem20, 2, 7, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.p2_groupBox)
        self.groupBox_7.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:5px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "QLabel{\n"
                                      "font:18px;                       \n"
                                      "color:rgb(2,2,2);                \n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox{\n"
                                      "padding-right: 15px; /* make room for the arrows */\n"
                                      "border:1px solid rgba(228,228,228,100);\n"
                                      "border-radius:5px;       \n"
                                      "  \n"
                                      "background-color: rgba(255, 255, 255,10);\n"
                                      "font:18px;      \n"
                                      "color:rgb(2,2,2);\n"
                                      "} \n"
                                      "\n"
                                      "QSpinBox::up-button {\n"
                                      "border-image: url(:/images/resources/spinbox-up.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button {\n"
                                      "border-image: url(:/images/resources/spinbox-down.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::up-button:pressed {\n"
                                      "margin-top:3px;\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button:pressed {\n"
                                      "margin-bottom:3px;\n"
                                      "}\n"
                                      "")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.p2_sb_day = QtWidgets.QSpinBox(self.groupBox_7)
        self.p2_sb_day.setMaximum(31)
        self.p2_sb_day.setProperty("value", 1)
        self.p2_sb_day.setObjectName("p2_sb_day")
        self.gridLayout_21.addWidget(self.p2_sb_day, 1, 6, 1, 1)
        self.p2_sb_month = QtWidgets.QSpinBox(self.groupBox_7)
        self.p2_sb_month.setMaximum(12)
        self.p2_sb_month.setProperty("value", 1)
        self.p2_sb_month.setObjectName("p2_sb_month")
        self.gridLayout_21.addWidget(self.p2_sb_month, 1, 4, 1, 1)
        self.p2_sb_year = QtWidgets.QSpinBox(self.groupBox_7)
        self.p2_sb_year.setMaximum(3000)
        self.p2_sb_year.setProperty("value", 2004)
        self.p2_sb_year.setObjectName("p2_sb_year")
        self.gridLayout_21.addWidget(self.p2_sb_year, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_21.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_21.addWidget(self.label_5, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_21.addWidget(self.label_6, 1, 7, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_7, 0, 0, 1, 5)
        self.groupBox_11 = QtWidgets.QGroupBox(self.p2_groupBox)
        self.groupBox_11.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:1px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font: 18px;                       \n"
                                       "                   color:rgb(2,2,2);                \n"
                                       "                   padding:10px; \n"
                                       "}\n"
                                       "QLabel{\n"
                                       "font:12px;                       \n"
                                       "color:rgb(2,2,2);                \n"
                                       "}\n"
                                       "\n"
                                       "QCheckBox{\n"
                                       "font:15px;                       \n"
                                       "color:rgb(2,2,2); \n"
                                       "}\n"
                                       "\n"
                                       "QCheckBox::indicator::unchecked {\n"
                                       "image: url(:/images/resources/btn_unchecked.png);\n"
                                       "width:15px;\n"
                                       "height:15px;\n"
                                       "\n"
                                       "\n"
                                       "}\n"
                                       "QCheckBox::indicator::checked {\n"
                                       "    image: url(:/images/resources/btn_checked.png);\n"
                                       "width:15px;\n"
                                       "height:15px\n"
                                       "}\n"
                                       "")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.p2_checkBox_data = QtWidgets.QCheckBox(self.groupBox_11)
        self.p2_checkBox_data.setObjectName("p2_checkBox_data")
        self.gridLayout_25.addWidget(self.p2_checkBox_data, 0, 0, 1, 1)
        self.p2_checkBox_dhua = QtWidgets.QCheckBox(self.groupBox_11)
        self.p2_checkBox_dhua.setObjectName("p2_checkBox_dhua")
        self.gridLayout_25.addWidget(self.p2_checkBox_dhua, 1, 0, 1, 1)
        self.gridLayout_25.setRowStretch(0, 1)
        self.gridLayout_25.setRowStretch(1, 1)
        self.gridLayout_11.addWidget(self.groupBox_11, 0, 5, 1, 1)
        self.gridLayout_11.setRowStretch(0, 1)
        self.gridLayout_11.setRowStretch(1, 1)
        self.gridLayout_5.addWidget(self.p2_groupBox, 1, 0, 1, 1)
        self.p2_widget = QtWidgets.QWidget(self.page2)
        self.p2_widget.setObjectName("p2_widget")
        self.p2_verticalLayout = QtWidgets.QVBoxLayout(self.p2_widget)
        self.p2_verticalLayout.setObjectName("p2_verticalLayout")
        self.gridLayout_5.addWidget(self.p2_widget, 0, 0, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setRowStretch(0, 2)
        self.gridLayout_5.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem21, 1, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem22, 0, 1, 1, 1)
        self.p3_groupBox = QtWidgets.QGroupBox(self.page3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3_groupBox.sizePolicy().hasHeightForWidth())
        self.p3_groupBox.setSizePolicy(sizePolicy)
        self.p3_groupBox.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:5px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font:bold 18px;                       \n"
                                       "                   color:rgba(255,255,255,255);                \n"
                                       "                   padding:6px; \n"
                                       "}")
        self.p3_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p3_groupBox.setFlat(True)
        self.p3_groupBox.setObjectName("p3_groupBox")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.p3_groupBox)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.p3_btn_saveResult = QtWidgets.QPushButton(self.p3_groupBox)
        self.p3_btn_saveResult.setStyleSheet("QPushButton{\n"
                                             " image-position: left;\n"
                                             "\n"
                                             "                  padding-right: 15px;\n"
                                             "                   border-style:inset;                  \n"
                                             "                   border-width:2px;                    \n"
                                             "                   border-radius:1px;                   \n"
                                             "                   border-color:rgba(255,255,255,100);   \n"
                                             "                   font:18px;                       \n"
                                             "                   color:rgb(2,2,2);                \n"
                                             "                   padding:6px; \n"
                                             "\n"
                                             "}\n"
                                             " QPushButton:hover{\n"
                                             "                   background-color:rgb(200,225,255);\n"
                                             "                   border-color:rgba(255,255,255,200);\n"
                                             "                   color:rgba(0,0,0,200);\n"
                                             "font:bold 20px;\n"
                                             "                   }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/resources/导出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p3_btn_saveResult.setIcon(icon5)
        self.p3_btn_saveResult.setObjectName("p3_btn_saveResult")
        self.gridLayout_18.addWidget(self.p3_btn_saveResult, 2, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem23, 3, 2, 1, 1)
        self.p3_result = QtWidgets.QTextEdit(self.p3_groupBox)
        self.p3_result.setStyleSheet("font:15px;                       \n"
                                     "color:rgba(255,255,255,200);                ")
        self.p3_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.p3_result.setObjectName("p3_result")
        self.gridLayout_18.addWidget(self.p3_result, 0, 2, 2, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem24, 3, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem25, 3, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.p3_groupBox)
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      " image-position: left;\n"
                                      "\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:2px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgba(255,255,255,100);   \n"
                                      "                   font:18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "\n"
                                      "}\n"
                                      " QPushButton:hover{\n"
                                      "                   background-color:rgb(200,225,255);\n"
                                      "                   border-color:rgba(255,255,255,200);\n"
                                      "                   color:rgba(0,0,0,200);\n"
                                      "font:bold 18px;\n"
                                      "                   }")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.p3_btn1_choose = QtWidgets.QPushButton(self.groupBox_4)
        self.p3_btn1_choose.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/resources/数据选择器.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p3_btn1_choose.setIcon(icon6)
        self.p3_btn1_choose.setObjectName("p3_btn1_choose")
        self.gridLayout_12.addWidget(self.p3_btn1_choose, 0, 0, 1, 1)
        self.p3_listWidget = QtWidgets.QListWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3_listWidget.sizePolicy().hasHeightForWidth())
        self.p3_listWidget.setSizePolicy(sizePolicy)
        self.p3_listWidget.setProperty("isWrapping", False)
        self.p3_listWidget.setObjectName("p3_listWidget")
        self.gridLayout_12.addWidget(self.p3_listWidget, 0, 1, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.p3_groupBox)
        self.groupBox_12.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:1px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font: 18px;                       \n"
                                       "                   color:rgb(2,2,2);                \n"
                                       "                   padding:6px; \n"
                                       "}\n"
                                       "QLabel{\n"
                                       "font:18px;                       \n"
                                       "color:rgb(2,2,2);                \n"
                                       "}\n"
                                       "\n"
                                       "QCheckBox{\n"
                                       "font:18px;                       \n"
                                       "color:rgb(2,2,2); \n"
                                       "}\n"
                                       "\n"
                                       "QCheckBox::indicator::unchecked {\n"
                                       "image: url(:/images/resources/btn_unchecked.png);\n"
                                       "width:15px;\n"
                                       "height:15px;\n"
                                       "\n"
                                       "\n"
                                       "}\n"
                                       "QCheckBox::indicator::checked {\n"
                                       "    image: url(:/images/resources/btn_checked.png);\n"
                                       "width:15px;\n"
                                       "height:15px\n"
                                       "}\n"
                                       "")
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.p3_checkBox_showAve = QtWidgets.QCheckBox(self.groupBox_12)
        self.p3_checkBox_showAve.setStyleSheet("")
        self.p3_checkBox_showAve.setObjectName("p3_checkBox_showAve")
        self.gridLayout_27.addWidget(self.p3_checkBox_showAve, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.p3_groupBox)
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:5px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "QLabel{\n"
                                      "font:18px;                       \n"
                                      "color:rgb(2,2,2);                \n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:horizontal {\n"
                                      "background-color: rgba(200,200,200,200);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox{\n"
                                      "background-color: rgba(255, 255, 255,10);\n"
                                      "border:1px solid rgba(228,228,228,100);\n"
                                      "border-radius:5px 5px 0px 0px;\n"
                                      "font-size:18px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    outline: 0px solid gray;   /* 选定项的虚框 */\n"
                                      "    border: 1px solid raga(228,228,228,100);   /* 整个下拉窗体的边框 */\n"
                                      "    color: blue;\n"
                                      "    background-color: white;   /* 整个下拉窗体的背景色 */\n"
                                      "    selection-background-color: lightblue;   /* 整个下拉窗体被选中项的背景色 */\n"
                                      "}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.p3_sw_method = QtWidgets.QStackedWidget(self.groupBox_5)
        self.p3_sw_method.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3_sw_method.sizePolicy().hasHeightForWidth())
        self.p3_sw_method.setSizePolicy(sizePolicy)
        self.p3_sw_method.setObjectName("p3_sw_method")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setObjectName("label_13")
        self.gridLayout_19.addWidget(self.label_13, 0, 0, 1, 1)
        self.p3_sw_method.addWidget(self.page)
        self.pg1_cnum = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pg1_cnum.sizePolicy().hasHeightForWidth())
        self.pg1_cnum.setSizePolicy(sizePolicy)
        self.pg1_cnum.setObjectName("pg1_cnum")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.pg1_cnum)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.p3_slider_cnum = QtWidgets.QSlider(self.pg1_cnum)
        self.p3_slider_cnum.setMinimum(2)
        self.p3_slider_cnum.setMaximum(20)
        self.p3_slider_cnum.setProperty("value", 3)
        self.p3_slider_cnum.setTracking(True)
        self.p3_slider_cnum.setOrientation(QtCore.Qt.Horizontal)
        self.p3_slider_cnum.setInvertedControls(False)
        self.p3_slider_cnum.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.p3_slider_cnum.setTickInterval(2)
        self.p3_slider_cnum.setObjectName("p3_slider_cnum")
        self.gridLayout_8.addWidget(self.p3_slider_cnum, 0, 1, 1, 1)
        self.p3_label_cnum = QtWidgets.QLabel(self.pg1_cnum)
        self.p3_label_cnum.setObjectName("p3_label_cnum")
        self.gridLayout_8.addWidget(self.p3_label_cnum, 0, 0, 1, 1)
        self.p3_sw_method.addWidget(self.pg1_cnum)
        self.pg2_db = QtWidgets.QWidget()
        self.pg2_db.setObjectName("pg2_db")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.pg2_db)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.p3_slider_minpts = QtWidgets.QSlider(self.pg2_db)
        self.p3_slider_minpts.setMaximum(100)
        self.p3_slider_minpts.setProperty("value", 10)
        self.p3_slider_minpts.setOrientation(QtCore.Qt.Horizontal)
        self.p3_slider_minpts.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.p3_slider_minpts.setObjectName("p3_slider_minpts")
        self.gridLayout_9.addWidget(self.p3_slider_minpts, 3, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem26, 1, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem27, 2, 3, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem28, 3, 3, 1, 1)
        self.p3_slider_eps = QtWidgets.QSlider(self.pg2_db)
        self.p3_slider_eps.setMaximum(100)
        self.p3_slider_eps.setSingleStep(1)
        self.p3_slider_eps.setPageStep(10)
        self.p3_slider_eps.setProperty("value", 10)
        self.p3_slider_eps.setSliderPosition(10)
        self.p3_slider_eps.setOrientation(QtCore.Qt.Horizontal)
        self.p3_slider_eps.setInvertedAppearance(False)
        self.p3_slider_eps.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.p3_slider_eps.setTickInterval(0)
        self.p3_slider_eps.setObjectName("p3_slider_eps")
        self.gridLayout_9.addWidget(self.p3_slider_eps, 1, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem29, 0, 3, 1, 1)
        self.p3_label_eps = QtWidgets.QLabel(self.pg2_db)
        self.p3_label_eps.setObjectName("p3_label_eps")
        self.gridLayout_9.addWidget(self.p3_label_eps, 1, 0, 1, 1)
        self.p3_label_minpts = QtWidgets.QLabel(self.pg2_db)
        self.p3_label_minpts.setObjectName("p3_label_minpts")
        self.gridLayout_9.addWidget(self.p3_label_minpts, 3, 0, 1, 1)
        self.p3_sw_method.addWidget(self.pg2_db)
        self.gridLayout_17.addWidget(self.p3_sw_method, 0, 1, 1, 1)
        self.p3_cb_method = QtWidgets.QComboBox(self.groupBox_5)
        self.p3_cb_method.setStyleSheet("")
        self.p3_cb_method.setObjectName("p3_cb_method")
        self.p3_cb_method.addItem("")
        self.p3_cb_method.addItem("")
        self.p3_cb_method.addItem("")
        self.p3_cb_method.addItem("")
        self.p3_cb_method.addItem("")
        self.p3_cb_method.addItem("")
        self.gridLayout_17.addWidget(self.p3_cb_method, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_5, 1, 0, 2, 2)
        self.gridLayout_18.setColumnStretch(0, 2)
        self.gridLayout_18.setColumnStretch(1, 1)
        self.gridLayout_18.setColumnStretch(2, 3)
        self.gridLayout_18.setRowStretch(0, 1)
        self.gridLayout_18.setRowStretch(1, 1)
        self.gridLayout_18.setRowStretch(2, 1)
        self.gridLayout_6.addWidget(self.p3_groupBox, 1, 0, 1, 1)
        self.p3_widget = QtWidgets.QWidget(self.page3)
        self.p3_widget.setStyleSheet("")
        self.p3_widget.setObjectName("p3_widget")
        self.p3_verticalLayout = QtWidgets.QVBoxLayout(self.p3_widget)
        self.p3_verticalLayout.setObjectName("p3_verticalLayout")
        self.gridLayout_6.addWidget(self.p3_widget, 0, 0, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setRowStretch(0, 2)
        self.gridLayout_6.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem30, 1, 1, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem31, 0, 1, 1, 1)
        self.p4_widget = QtWidgets.QWidget(self.page4)
        self.p4_widget.setStyleSheet("")
        self.p4_widget.setObjectName("p4_widget")
        self.p4_verticalLayout = QtWidgets.QVBoxLayout(self.p4_widget)
        self.p4_verticalLayout.setObjectName("p4_verticalLayout")
        self.gridLayout_13.addWidget(self.p4_widget, 0, 0, 1, 1)
        self.p4_groupBox = QtWidgets.QGroupBox(self.page4)
        self.p4_groupBox.setStyleSheet("QGroupBox{\n"
                                       "                  padding-right: 15px;\n"
                                       "                   border-style:inset;                  \n"
                                       "                   border-width:5px;                    \n"
                                       "                   border-radius:5px;                   \n"
                                       "                   border-color:rgb(255,255,255);   \n"
                                       "                   font:bold 18px;                       \n"
                                       "                   color:rgba(255,255,255,255);                \n"
                                       "                   padding:6px; \n"
                                       "}")
        self.p4_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p4_groupBox.setObjectName("p4_groupBox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.p4_groupBox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.p4_btn_saveResult = QtWidgets.QPushButton(self.p4_groupBox)
        self.p4_btn_saveResult.setStyleSheet("\n"
                                             "QPushButton{\n"
                                             " image-position: left;\n"
                                             "\n"
                                             "                  padding-right: 15px;\n"
                                             "                   border-style:inset;                  \n"
                                             "                   border-width:2px;                    \n"
                                             "                   border-radius:1px;                   \n"
                                             "                   border-color:rgba(255,255,255,100);   \n"
                                             "                   font:18px;                       \n"
                                             "                   color:rgb(2,2,2);                \n"
                                             "                   padding:6px; \n"
                                             "\n"
                                             "}\n"
                                             " QPushButton:hover{\n"
                                             "                   background-color:rgb(200,225,255);\n"
                                             "                   border-color:rgba(255,255,255,200);\n"
                                             "                   color:rgba(0,0,0,200);\n"
                                             "font:bold 20px;\n"
                                             "                   }")
        self.p4_btn_saveResult.setIcon(icon5)
        self.p4_btn_saveResult.setObjectName("p4_btn_saveResult")
        self.gridLayout_14.addWidget(self.p4_btn_saveResult, 2, 1, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem32, 3, 1, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem33, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.p4_groupBox)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      " image-position: left;\n"
                                      "\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:2px;                    \n"
                                      "                   border-radius:1px;                   \n"
                                      "                   border-color:rgba(255,255,255,100);   \n"
                                      "                   font:18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "\n"
                                      "}\n"
                                      " QPushButton:hover{\n"
                                      "                   background-color:rgb(200,225,255);\n"
                                      "                   border-color:rgba(255,255,255,200);\n"
                                      "                   color:rgba(0,0,0,200);\n"
                                      "font:bold 20px;\n"
                                      "                   }\n"
                                      "QLabel{\n"
                                      "font:16px;                       \n"
                                      "color:rgb(2,2,2);                \n"
                                      "}\n"
                                      "QComboBox{\n"
                                      "background-color: rgba(255, 255, 255,10);\n"
                                      "border:1px solid rgba(228,228,228,100);\n"
                                      "border-radius:5px 5px 0px 0px;\n"
                                      "font-size:18px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "    outline: 0px solid gray;   /* 选定项的虚框 */\n"
                                      "    border: 1px solid raga(228,228,228,100);   /* 整个下拉窗体的边框 */\n"
                                      "    color: blue;\n"
                                      "    background-color: white;   /* 整个下拉窗体的背景色 */\n"
                                      "    selection-background-color: lightblue;   /* 整个下拉窗体被选中项的背景色 */\n"
                                      "}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.p4_btn_predict = QtWidgets.QPushButton(self.groupBox_3)
        self.p4_btn_predict.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/resources/预测.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p4_btn_predict.setIcon(icon7)
        self.p4_btn_predict.setIconSize(QtCore.QSize(20, 20))
        self.p4_btn_predict.setObjectName("p4_btn_predict")
        self.gridLayout_15.addWidget(self.p4_btn_predict, 1, 0, 1, 1)
        self.p4_checkBox_showReal = QtWidgets.QCheckBox(self.groupBox_3)
        self.p4_checkBox_showReal.setStyleSheet("QCheckBox{\n"
                                                "  color:#666666;\n"
                                                "  font-size:18px;\n"
                                                "  padding: 1px 15px 1px 3px;\n"
                                                "} ")
        self.p4_checkBox_showReal.setChecked(True)
        self.p4_checkBox_showReal.setObjectName("p4_checkBox_showReal")
        self.gridLayout_15.addWidget(self.p4_checkBox_showReal, 1, 1, 1, 1)
        self.p4_cb_modelchoose = QtWidgets.QComboBox(self.groupBox_3)
        self.p4_cb_modelchoose.setStyleSheet("")
        self.p4_cb_modelchoose.setObjectName("p4_cb_modelchoose")
        self.p4_cb_modelchoose.addItem("")
        self.p4_cb_modelchoose.addItem("")
        self.p4_cb_modelchoose.addItem("")
        self.p4_cb_modelchoose.addItem("")
        self.p4_cb_modelchoose.addItem("")
        self.p4_cb_modelchoose.addItem("")
        self.gridLayout_15.addWidget(self.p4_cb_modelchoose, 0, 0, 1, 2)
        self.gridLayout_14.addWidget(self.groupBox_3, 1, 0, 2, 1)
        self.p4_result = QtWidgets.QTextEdit(self.p4_groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.p4_result.setFont(font)
        self.p4_result.setStyleSheet("font:15px;                       \n"
                                     "color:rgba(255,255,255,200);                ")
        self.p4_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.p4_result.setObjectName("p4_result")
        self.gridLayout_14.addWidget(self.p4_result, 0, 1, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.p4_groupBox)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
                                      "                  padding-right: 15px;\n"
                                      "                   border-style:inset;                  \n"
                                      "                   border-width:1px;                    \n"
                                      "                   border-radius:5px;                   \n"
                                      "                   border-color:rgb(255,255,255);   \n"
                                      "                   font: 18px;                       \n"
                                      "                   color:rgb(2,2,2);                \n"
                                      "                   padding:6px; \n"
                                      "}\n"
                                      "QLabel{\n"
                                      "font:18px;                       \n"
                                      "color:rgb(2,2,2);                \n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox{\n"
                                      "padding-right: 15px; /* make room for the arrows */\n"
                                      "border:1px solid rgba(228,228,228,100);\n"
                                      "border-radius:5px;       \n"
                                      "  \n"
                                      "background-color: rgba(255, 255, 255,10);\n"
                                      "font:18px;      \n"
                                      "color:rgb(2,2,2);\n"
                                      "} \n"
                                      "\n"
                                      "QSpinBox::up-button {\n"
                                      "border-image: url(:/images/resources/spinbox-up.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button {\n"
                                      "border-image: url(:/images/resources/spinbox-down.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::up-button:pressed {\n"
                                      "margin-top:3px;\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button:pressed {\n"
                                      "margin-bottom:3px;\n"
                                      "}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_16.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_16.addWidget(self.label_12, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_16.addWidget(self.label_10, 0, 8, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_16.addWidget(self.label_9, 0, 6, 1, 1)
        self.p4_sb_year = QtWidgets.QSpinBox(self.groupBox_2)
        self.p4_sb_year.setMinimum(2004)
        self.p4_sb_year.setMaximum(2008)
        self.p4_sb_year.setSingleStep(1)
        self.p4_sb_year.setProperty("value", 2004)
        self.p4_sb_year.setObjectName("p4_sb_year")
        self.gridLayout_16.addWidget(self.p4_sb_year, 0, 2, 1, 1)
        self.p4_sb_month = QtWidgets.QSpinBox(self.groupBox_2)
        self.p4_sb_month.setMinimum(1)
        self.p4_sb_month.setMaximum(12)
        self.p4_sb_month.setObjectName("p4_sb_month")
        self.gridLayout_16.addWidget(self.p4_sb_month, 0, 4, 1, 1)
        self.p4_sb_zoneid = QtWidgets.QSpinBox(self.groupBox_2)
        self.p4_sb_zoneid.setMinimum(1)
        self.p4_sb_zoneid.setMaximum(21)
        self.p4_sb_zoneid.setObjectName("p4_sb_zoneid")
        self.gridLayout_16.addWidget(self.p4_sb_zoneid, 0, 0, 1, 1)
        self.p4_sb_day = QtWidgets.QSpinBox(self.groupBox_2)
        self.p4_sb_day.setMinimum(1)
        self.p4_sb_day.setMaximum(31)
        self.p4_sb_day.setProperty("value", 8)
        self.p4_sb_day.setObjectName("p4_sb_day")
        self.gridLayout_16.addWidget(self.p4_sb_day, 0, 7, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_14.setRowStretch(0, 1)
        self.gridLayout_14.setRowStretch(1, 1)
        self.gridLayout_14.setRowStretch(2, 1)
        self.gridLayout_13.addWidget(self.p4_groupBox, 1, 0, 1, 1)
        self.gridLayout_13.setColumnStretch(0, 1)
        self.gridLayout_13.setRowStretch(0, 2)
        self.gridLayout_13.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.page4)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 1)
        self.gridLayout_3.setColumnStretch(0, 4)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        Mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainwindow)
        self.stackedWidget.setCurrentIndex(3)
        self.p3_sw_method.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "电力负荷分析软件"))
        self.btn_1check.setText(_translate("Mainwindow", "数据查看"))
        self.btn_2show.setText(_translate("Mainwindow", "负荷监控"))
        self.btn_3clus.setText(_translate("Mainwindow", "负荷聚类"))
        self.btn_4fore.setText(_translate("Mainwindow", "负荷预测"))
        self.btn_help.setText(_translate("Mainwindow", "帮助    中心"))
        self.p0_textBrowser.setHtml(_translate("Mainwindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline; color:#b8d5ff;\">电力负荷分析软件</span></p>\n"
                                               "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d5ff;\">柯思雄毕业设计作品</span></p>\n"
                                               "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d5ff;\">指导老师：方支剑</span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d4ff;\">本软件包含以下功能</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d4ff;\">1、数据查看</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">负荷数据的增加；</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">负荷数据的删除；</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">负荷数据的修改；</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">负荷数据的插叙；</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">    （按地区、日期查询、SQL查询、排序）</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d4ff;\">2、负荷监控</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">历史数据的按日负荷曲线可视化</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; color:#b8d4ff;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d4ff;\">3、负荷聚类</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">数据选择</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">聚类模型选择</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">聚类分析结果显示</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">    （可视化曲线、数学解释）</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">导出聚类分析结果为PDF</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; color:#b8d4ff;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8d4ff;\">4、负荷预测</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •待</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">预测日的选择</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">预测模型选择</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">预测结果显示</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">    （可视化曲线、预测误差）</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#b8d4ff;\">    •</span><span style=\" font-family:\'等线\'; font-size:16pt; color:#b8d4ff;\">导出预测结果为PDF</span><span style=\" font-size:16pt; color:#b8d4ff;\"> </span></p>\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; color:#b8d4ff;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#b8d4ff;\">如有问题 请联系作者：柯思雄（kktenega@gmail.com）</span></p></body></html>"))
        self.p1_groupBox.setTitle(_translate("Mainwindow", "数据查看"))
        self.groupBox_10.setTitle(_translate("Mainwindow", "排序方式"))
        self.p1_cb_paixu.setItemText(0, _translate("Mainwindow", "默认排序"))
        self.p1_cb_paixu.setItemText(1, _translate("Mainwindow", "以地区排序"))
        self.p1_cb_paixu.setItemText(2, _translate("Mainwindow", "以日期排序"))
        self.p1_cb_paixu.setItemText(3, _translate("Mainwindow", "以负荷排序"))
        self.p1_rb_paixu_zheng.setText(_translate("Mainwindow", "正序"))
        self.p1_rb_paixu_fan.setText(_translate("Mainwindow", "逆序"))
        self.label_8.setText(
            _translate("Mainwindow", "提示：SQL查询格式如：select * from where (zone_id = 0 and year = 2004 and h1>2000)"))
        self.groupBox_6.setTitle(_translate("Mainwindow", "日期查询"))
        self.label_0.setText(_translate("Mainwindow", "地区"))
        self.label_1.setText(_translate("Mainwindow", "年"))
        self.label_2.setText(_translate("Mainwindow", "月"))
        self.label_3.setText(_translate("Mainwindow", "日"))
        self.groupBox_9.setTitle(_translate("Mainwindow", "数据库SQL查询"))
        self.p1_lineEdit_sql.setPlaceholderText(_translate("Mainwindow", "zone_id = 0 and year =2004 and h1>2000"))
        self.p1_pushButton_search.setText(_translate("Mainwindow", "查询"))
        self.groupBox_8.setTitle(_translate("Mainwindow", "数据操作"))
        self.p1_btn_add.setText(_translate("Mainwindow", "增加"))
        self.p1_btn_save.setText(_translate("Mainwindow", "保存"))
        self.p1_btn_del.setText(_translate("Mainwindow", "删除"))
        self.p2_groupBox.setTitle(_translate("Mainwindow", "负荷监控"))
        self.p2_groupBox_zoonid.setTitle(_translate("Mainwindow", "区域"))
        self.p2_cb_6.setText(_translate("Mainwindow", "6"))
        self.p2_cb_14.setText(_translate("Mainwindow", "14"))
        self.p2_cb_17.setText(_translate("Mainwindow", "17"))
        self.p2_cb_5.setText(_translate("Mainwindow", "5"))
        self.p2_cb_15.setText(_translate("Mainwindow", "15"))
        self.p2_cb_20.setText(_translate("Mainwindow", "20"))
        self.p2_cb_13.setText(_translate("Mainwindow", "13"))
        self.p2_cb_4.setText(_translate("Mainwindow", "4"))
        self.p2_cb_19.setText(_translate("Mainwindow", "19"))
        self.p2_cb_18.setText(_translate("Mainwindow", "18"))
        self.p2_cb_1.setText(_translate("Mainwindow", "1"))
        self.p2_cb_11.setText(_translate("Mainwindow", "11"))
        self.p2_cb_2.setText(_translate("Mainwindow", "2"))
        self.p2_cb_16.setText(_translate("Mainwindow", "16"))
        self.p2_cb_8.setText(_translate("Mainwindow", "8"))
        self.p2_cb_12.setText(_translate("Mainwindow", "12"))
        self.p2_cb_9.setText(_translate("Mainwindow", "9"))
        self.p2_cb_10.setText(_translate("Mainwindow", "10"))
        self.p2_cb_3.setText(_translate("Mainwindow", "3"))
        self.p2_cb_7.setText(_translate("Mainwindow", "7"))
        self.groupBox_7.setTitle(_translate("Mainwindow", "查询日期"))
        self.label_4.setText(_translate("Mainwindow", "年"))
        self.label_5.setText(_translate("Mainwindow", "月"))
        self.label_6.setText(_translate("Mainwindow", "日"))
        self.groupBox_11.setTitle(_translate("Mainwindow", "功能选项"))
        self.p2_checkBox_data.setText(_translate("Mainwindow", "是否显示数据"))
        self.p2_checkBox_dhua.setText(_translate("Mainwindow", "有无动画"))
        self.p3_groupBox.setTitle(_translate("Mainwindow", "负荷聚类"))
        self.p3_btn_saveResult.setText(_translate("Mainwindow", "导出报告"))
        self.groupBox_4.setTitle(_translate("Mainwindow", "数据选择"))
        self.p3_btn1_choose.setText(_translate("Mainwindow", "请选择"))
        self.p3_listWidget.setSortingEnabled(False)
        self.groupBox_12.setTitle(_translate("Mainwindow", "功能选项"))
        self.p3_checkBox_showAve.setText(_translate("Mainwindow", "显示平均曲线"))
        self.groupBox_5.setTitle(_translate("Mainwindow", "聚类方法选择"))
        self.label_13.setText(_translate("Mainwindow", "......"))
        self.p3_label_cnum.setText(_translate("Mainwindow", "聚类数"))
        self.p3_label_eps.setText(_translate("Mainwindow", "eps"))
        self.p3_label_minpts.setText(_translate("Mainwindow", "minpts"))
        self.p3_cb_method.setItemText(0, _translate("Mainwindow", "请选择"))
        self.p3_cb_method.setItemText(1, _translate("Mainwindow", "K-均值"))
        self.p3_cb_method.setItemText(2, _translate("Mainwindow", "层次聚类"))
        self.p3_cb_method.setItemText(3, _translate("Mainwindow", "高斯模型"))
        self.p3_cb_method.setItemText(4, _translate("Mainwindow", "谱聚类"))
        self.p3_cb_method.setItemText(5, _translate("Mainwindow", "DBSCAN"))
        self.p4_groupBox.setTitle(_translate("Mainwindow", "负荷预测"))
        self.p4_btn_saveResult.setText(_translate("Mainwindow", "导出报告"))
        self.groupBox_3.setTitle(_translate("Mainwindow", "模型选择"))
        self.p4_btn_predict.setText(_translate("Mainwindow", "预测"))
        self.p4_checkBox_showReal.setText(_translate("Mainwindow", "显示真实值"))
        self.p4_cb_modelchoose.setItemText(0, _translate("Mainwindow", "请选择"))
        self.p4_cb_modelchoose.setItemText(1, _translate("Mainwindow", "ANN"))
        self.p4_cb_modelchoose.setItemText(2, _translate("Mainwindow", "LSTM"))
        self.p4_cb_modelchoose.setItemText(3, _translate("Mainwindow", "GRU"))
        self.p4_cb_modelchoose.setItemText(4, _translate("Mainwindow", "Kmeans-ANN"))
        self.p4_cb_modelchoose.setItemText(5, _translate("Mainwindow", "Kmeans-TCN-GRU"))
        self.groupBox_2.setTitle(_translate("Mainwindow", "预测日选择"))
        self.label_11.setText(_translate("Mainwindow", "地区"))
        self.label_12.setText(_translate("Mainwindow", "年"))
        self.label_10.setText(_translate("Mainwindow", "日"))
        self.label_9.setText(_translate("Mainwindow", "月"))

    '''运行状态信息显示'''
    def send_message(self,message):
        now_time = datetime.datetime.now().strftime('%F %T')
        self.text_message.append(now_time + ':\n'+message+'\n')

    def __init__(self,Mainwindow):
        self.setupUi(Mainwindow)
        self.stackedWidget.setCurrentIndex(0)




        '''连接数据库'''
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('func/load.db')

        if db.open():
            self.send_message('数据库连接成功')
        else:
            self.send_message('数据库连接失败')
            self.send_message(db.lastError().text())


        '''页面0'''
        self.p0_textBrowser.hide()

        '''页面1'''
        self.sqlmodel = QtSql.QSqlTableModel(db=db)
        self.sqlmodel.setTable('load_history')
        #设置提交才能生效修改
        self.sqlmodel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        #self.sqlmodel.select()
        self.sql_str = str("select * from Load_history")
        sql = QtSql.QSqlQuery(self.sql_str)
        self.sqlmodel.setQuery(sql)


        self.p1_tableView.setModel(self.sqlmodel)
        self.p1_tableView.setStyleSheet("background-color: rgba(255, 255, 255,200);")
        self.p1_tableView.setAlternatingRowColors(True)


        '''页面2'''


        self.p2_chart_view = QtChart.QChartView()
        #ChartThemeDark   ChartThemeBlueCerulean  ChartThemeBlueNcs ChartThemeHighContrast
        self.p2_chart_view.chart().setTheme(QtChart.QChart.ChartThemeBlueNcs)
        self.p2_chart_view.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.p2_verticalLayout.addWidget(self.p2_chart_view)


        '''页面3'''
        self.dialog = Ui_Dialog_data()
        # self.p3_data  读取到的数据
        self.p3_data = np.zeros(1)
        # self.p3_data_xy  聚类后的数据
        self.p3_data_xy = np.zeros(1)
        self.p3_sw_method.setCurrentIndex(0)
        self.p3_chart_view = QtChart.QChartView()
        self.p3_chart_view.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.p3_verticalLayout.addWidget(self.p3_chart_view)

        '''页面4'''
        self.p4_chart_view = QtChart.QChartView()
        self.p4_chart_view.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.p4_verticalLayout.addWidget(self.p4_chart_view)
        self.p4_pre_y = np.zeros(1)
        self.p4_real_y = np.zeros(1)




        '''槽函数'''
        self.slot_init()  # 槽函数设置



    def slot_init(self):
        '''切换页面按钮'''
        self.btn_help.clicked.connect(self.btn_0click)
        self.btn_1check.clicked.connect(self.btn_1click)
        self.btn_2show.clicked.connect(self.btn_2click)
        self.btn_3clus.clicked.connect(self.btn_3click)
        self.btn_4fore.clicked.connect(self.btn_4click)




        '''页面1：槽函数'''
        self.p1_sb_zoneid.textChanged.connect(self.p1_auto_search)
        self.p1_sb_year.textChanged.connect(self.p1_auto_search)
        self.p1_sb_month.textChanged.connect(self.p1_auto_search)
        self.p1_sb_day.textChanged.connect(self.p1_auto_search)
        self.p1_pushButton_search.clicked.connect(self.p1_btn_search_clicked)

        self.p1_cb_paixu.currentTextChanged.connect(self.p1_paixu)
        self.p1_rb_paixu_zheng.clicked.connect(self.p1_paixu)
        self.p1_rb_paixu_fan.clicked.connect(self.p1_paixu)
        self.p1_btn_add.clicked.connect(self.p1_add)
        self.p1_btn_del.clicked.connect(self.p1_del)
        self.p1_btn_save.clicked.connect(self.p1_save)


        '''页面2：槽函数'''
        self.p2_sb_year.textChanged.connect(self.p2_btn_search_click)
        self.p2_sb_month.textChanged.connect(self.p2_btn_search_click)
        self.p2_sb_day.textChanged.connect(self.p2_btn_search_click)

        self.p2_checkBox_data.stateChanged.connect(self.p2_btn_search_click)
        self.p2_checkBox_dhua.stateChanged.connect(self.p2_btn_search_click)

        self.p2_cb_1.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_2.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_3.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_4.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_5.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_6.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_7.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_8.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_9.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_10.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_11.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_12.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_13.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_14.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_15.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_16.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_17.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_18.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_19.clicked.connect(self.p2_btn_search_click)
        self.p2_cb_20.clicked.connect(self.p2_btn_search_click)

        '''页面3：槽函数'''
        self.p3_btn1_choose.clicked.connect(self.p3_btn1_choose_click)

        self.dialog.btn_yes.clicked.connect(self.p3_dialog_get_data)

        self.p3_cb_method.activated.connect(self.p3_method_changed)
        self.p3_slider_cnum.valueChanged.connect(self.p3_method_changed)
        self.p3_slider_eps.valueChanged.connect(self.p3_method_changed)
        self.p3_slider_minpts.valueChanged.connect(self.p3_method_changed)

        self.p3_checkBox_showAve.stateChanged.connect(self.p3_draw)

        self.p3_btn_saveResult.clicked.connect(self.p3_save)

        '''页面4：槽函数'''

        self.p4_btn_predict.clicked.connect(self.p4_predict)
        self.p4_checkBox_showReal.stateChanged.connect(self.p4_draw)
        self.p4_btn_saveResult.clicked.connect(self.p4_save)


    '''功能栏四个按键'''

    def btn_0click(self):
        '''第一次点击至帮助界面 or 上一时刻隐藏着，则显示'''
        if self.stackedWidget.currentIndex()!=0 or self.p0_textBrowser.isHidden()==1:
            self.p0_textBrowser.show()
            self.send_message('帮助中心——显示')
        else:
            self.p0_textBrowser.hide()
            self.send_message('帮助中心——不显示')

        self.stackedWidget.setCurrentIndex(0)

    def btn_1click(self):
        self.stackedWidget.setCurrentIndex(1)
        self.send_message('数据查看')

    def btn_2click(self):
        self.stackedWidget.setCurrentIndex(2)
        self.send_message('负荷监控')


    def btn_3click(self):
        self.stackedWidget.setCurrentIndex(3)
        self.send_message('负荷聚类')

    def btn_4click(self):
        self.stackedWidget.setCurrentIndex(4)
        self.send_message('负荷预测')


    '''页面1'''
    def p1_auto_search(self):
        zone_id=self.p1_sb_zoneid.text()
        year=self.p1_sb_year.text()
        month=self.p1_sb_month.text()
        day=self.p1_sb_day.text()

        if zone_id == '0':
            zone_id = "%%"
        if year == '0':
            year = "%%"
        if month == '0':
            month = "%%"
        if day == '0' :
            day = "%%"
        #
        # fil=str('zone_id LIKE \'{0}\' AND year LIKE \'{1}\' AND month LIKE \'{2}\' AND day LIKE \'{3}\'')\
        #     .format(zone_id,year,month,day)
        # self.sqlmodel.setFilter(fil)

        self.sql_str=str("select * from Load_history where zone_id LIKE \'{0}\' AND year LIKE \'{1}\' AND month LIKE \'{2}\' AND day LIKE \'{3}\'".format(zone_id,year,month,day))
        sql=QtSql.QSqlQuery(self.sql_str)
        self.sqlmodel.setQuery(sql)
        self.p1_paixu()

    def p1_btn_search_clicked(self):
        self.sql_str = str("select * from Load_history where ")+self.p1_lineEdit_sql.text()
        sql=QtSql.QSqlQuery(self.sql_str)
        self.sqlmodel.setQuery(sql)

    def p1_paixu(self):
        if self.p1_rb_paixu_zheng.isChecked():
            if self.p1_cb_paixu.currentIndex() == 1:
                order_str=" order by 1 ASC"
                new_sql_str = self.sql_str +order_str
            elif self.p1_cb_paixu.currentIndex() == 2:
                order_str = " order by 2 ASC,3 ASC,4 ASC "
                new_sql_str = self.sql_str + order_str
            elif self.p1_cb_paixu.currentIndex() == 3:
                order_str = " order by 29 ASC"
                new_sql_str = self.sql_str + order_str
            else:
                new_sql_str = self.sql_str
        else:
            if self.p1_cb_paixu.currentIndex() == 1:
                order_str=" order by 1 DESC"
                new_sql_str = self.sql_str +order_str
            elif self.p1_cb_paixu.currentIndex() == 2:
                order_str = " order by 2 DESC,3 DESC,4 DESC "
                new_sql_str = self.sql_str + order_str
            elif self.p1_cb_paixu.currentIndex() == 3:
                order_str = " order by 29 DESC"
                new_sql_str = self.sql_str + order_str
            else:
                new_sql_str = self.sql_str
        sql=QtSql.QSqlQuery(new_sql_str)
        self.sqlmodel.setQuery(sql)



    def p1_add(self):
        rowNum = self.sqlmodel.rowCount()
        curRow = self.p1_tableView.currentIndex().row()
        if curRow == -1:
            box = QMessageBox()
            box.setWindowTitle("提示")
            box.setText("请选择要添加的行")
            box.setStandardButtons(QMessageBox.Yes)
            box.exec()
            return
        else:
            print(curRow)
            row=curRow+1
            self.sqlmodel.insertRow(row)
        self.sqlmodel.setData(self.sqlmodel.index(row,0),1)
        #self.sqlmodel.submitAll()


    def p1_del(self):
        curRow = self.p1_tableView.currentIndex().row()
        self.sqlmodel.removeRow(curRow)
        box = QMessageBox()
        box.setWindowTitle("提示")
        box.setText("你确定要删除改行吗？")
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply = box.exec()
        if reply == QMessageBox.Yes:
            self.sqlmodel.submitAll()
        else:
            self.sqlmodel.revertAll()

    def p1_save(self):
        self.sqlmodel.database().transaction()
        if self.sqlmodel.submitAll():
            if self.sqlmodel.database().commit():
                QMessageBox.about(self.centralwidget, "提示", "保存成功")
            else:
                self.sqlmodel.database().rollback()
                QMessageBox.about(self.centralwidget, "提示", "保存失败")




    '''页面2'''
    def p2_btn_search_click(self):

        year=self.p2_sb_year.text()
        month=self.p2_sb_month.text()
        day=self.p2_sb_day.text()

        if year == '0':
            year = "%%"
        if month == '0':
            month = "%%"
        if day == '0' :
            day = "%%"

        zone_id_list=[]

        if self.p2_cb_1.isChecked():
            zone_id_list.append(1)
        if self.p2_cb_2.isChecked():
            zone_id_list.append(2)
        if self.p2_cb_3.isChecked():
            zone_id_list.append(3)
        if self.p2_cb_4.isChecked():
            zone_id_list.append(4)
        if self.p2_cb_5.isChecked():
            zone_id_list.append(5)
        if self.p2_cb_6.isChecked():
            zone_id_list.append(6)
        if self.p2_cb_7.isChecked():
            zone_id_list.append(7)
        if self.p2_cb_8.isChecked():
            zone_id_list.append(8)
        if self.p2_cb_9.isChecked():
            zone_id_list.append(9)
        if self.p2_cb_10.isChecked():
            zone_id_list.append(10)
        if self.p2_cb_11.isChecked():
            zone_id_list.append(11)
        if self.p2_cb_12.isChecked():
            zone_id_list.append(12)
        if self.p2_cb_13.isChecked():
            zone_id_list.append(13)
        if self.p2_cb_14.isChecked():
            zone_id_list.append(14)
        if self.p2_cb_15.isChecked():
            zone_id_list.append(15)
        if self.p2_cb_16.isChecked():
            zone_id_list.append(16)
        if self.p2_cb_17.isChecked():
            zone_id_list.append(17)
        if self.p2_cb_18.isChecked():
            zone_id_list.append(18)
        if self.p2_cb_19.isChecked():
            zone_id_list.append(19)
        if self.p2_cb_20.isChecked():
            zone_id_list.append(20)



        self.p2_chart_view.chart().removeAllSeries()

        if len(zone_id_list) == 0:
            return

        up_line = 0
        for zone_id in zone_id_list:
            sql = 'select * from load_history where zone_id = {0} AND year like \'{1}\' AND month like \'{2}\' AND day like \'{3}\''\
                .format(zone_id,year, month, day)

            query = QtSql.QSqlQuery()
            query.exec(sql)
            while query.next():
                line_series = QtChart.QLineSeries()
                for i in range(4,28):
                    line_series.append(i-4,query.value(i))
                    up_line = max(up_line,query.value(i))
                line_series.setPen(QtGui.QPen(QtGui.QColor(mycolor[zone_id-1][0],mycolor[zone_id-1][1],mycolor[zone_id-1][2]),2))
                line_series.setName('zone_'+str(zone_id))

                if self.p2_checkBox_data.isChecked():
                    line_series.setPointLabelsFormat("@yPoint")
                    line_series.setPointLabelsClipping(False)
                    line_series.setPointLabelsFont(QFont("Roman times",8))
                    line_series.setPointLabelsVisible(True)

                self.p2_chart_view.chart().addSeries(line_series)

        self.p2_chart_view.chart().setTitle("{}年{}月{}日历史负荷曲线".format(year,month,day))
        self.p2_chart_view.chart().createDefaultAxes()
        self.p2_chart_view.chart().axisX().setRange(0,24)
        self.p2_chart_view.chart().axisX().setMinorTickCount(5)
        self.p2_chart_view.chart().axisX().setLabelFormat("%d")

        self.p2_chart_view.chart().axisY().setMax(up_line*1.1)
        self.p2_chart_view.chart().axisY().setMin(0)
        if self.p2_checkBox_dhua.isChecked():
            self.p2_chart_view.chart().setAnimationOptions(QtChart.QChart.AllAnimations)
        else:
            self.p2_chart_view.chart().setAnimationOptions(QtChart.QChart.NoAnimation)

    '''页面3'''
    def p3_btn1_choose_click(self):
        self.dialog.show()

    def p3_dialog_get_data(self):
        self.p3_listWidget.clear()
        list_que=[]
        count = self.dialog.listWidget.count()
        for i in range(count):
            item=self.dialog.listWidget.item(i).text()
            self.p3_listWidget.addItem(item)
            list_one=re.findall(r'[\d+N]+', item)
            for j in range(len(list_one)):
                if list_one[j] =='N':
                    list_one[j] = '%%'
            list_que.append(list_one)
        data=[]
        for (zone,year,month,day) in list_que:
            sql = 'select * from load_history where zone_id like \'{0}\' AND year like \'{1}\' AND month like \'{2}\' AND day like \'{3}\'' \
                .format(zone, year, month, day)

            query = QtSql.QSqlQuery()
            query.exec(sql)
            while query.next():
                line=[]
                for i in range(0, 28):
                    line.append(query.value(i))
                data.append(line)
        self.p3_data=np.array(data)
        self.p3_data_xy = np.zeros(1)

        '''绘图'''
        self.p3_chart_view.chart().removeAllSeries()
        for i in range(self.p3_data.shape[0]):
            line_series = QtChart.QLineSeries()
            for j in range(4, 28):
                line_series.append(j-4, self.p3_data[i][j])
            line_series.setPen(QtGui.QPen(QtGui.QColor(mycolor[i%20][0],mycolor[i%20][1],mycolor[i%20][2]),2))
            #line_series.setName('zone_'+str(zone_id))
            self.p3_chart_view.chart().addSeries(line_series)
        self.p3_chart_view.chart().legend().hide()
        self.p3_chart_view.chart().createDefaultAxes()
        #chart_view.chart().setTitle("Load-"+str(year)+'-'+str(month)+'-'+str(day))


    def p3_method_changed(self):

        if self.p3_cb_method.currentIndex()==0:
            self.p3_sw_method.setCurrentIndex(0)
            self.p3_result.clear()
            self.p3_chart_view.chart().removeAllSeries()
            self.p3_dialog_get_data()
            return

        cnum=self.p3_slider_cnum.value()
        eps=self.p3_slider_eps.value()/100
        minpts=self.p3_slider_minpts.value()
        self.p3_label_cnum.setText("聚类数:{}".format(cnum))
        self.p3_label_eps.setText("eps:{}".format(eps))
        self.p3_label_minpts.setText("minpts:{}".format(minpts))



        if self.p3_data.shape[0] < cnum:

            QMessageBox.warning(self.centralwidget, "警告", "数据过少，无法分析")
            return

        dataset_x = self.p3_data[:, 4:28]
        dataset_x = sklearn.preprocessing.MaxAbsScaler().fit_transform(dataset_x)

        if self.p3_cb_method.currentIndex() == 1:
            self.p3_sw_method.setCurrentIndex(1)
            begin=time.time()
            y = KMeans(n_clusters=cnum).fit_predict(dataset_x)
            end=time.time()
            time_cost=end-begin
        elif self.p3_cb_method.currentIndex() == 2:
            self.p3_sw_method.setCurrentIndex(1)
            begin = time.time()
            y = AgglomerativeClustering(n_clusters=cnum).fit_predict(dataset_x)
            end = time.time()
            time_cost=end-begin
        elif self.p3_cb_method.currentIndex() == 3:
            self.p3_sw_method.setCurrentIndex(1)
            begin = time.time()
            y = GaussianMixture(n_components=cnum).fit_predict(dataset_x)
            end = time.time()
            time_cost=end-begin
        elif self.p3_cb_method.currentIndex() == 4:
            self.p3_sw_method.setCurrentIndex(1)
            begin = time.time()
            y = SpectralClustering(n_clusters=cnum, random_state=0).fit_predict(dataset_x)
            end = time.time()
            time_cost=end-begin
        elif self.p3_cb_method.currentIndex() == 5:
            self.p3_sw_method.setCurrentIndex(2)
            begin = time.time()
            y = DBSCAN(eps=eps, min_samples=minpts).fit_predict(dataset_x)
            end = time.time()
            time_cost=end-begin
        y = y[:, np.newaxis]
        self.p3_data_xy = np.hstack((self.p3_data, y))


        '''显示'''
        self.p3_result.clear()
        Color = QColor(255, 255, 255)
        self.p3_result.setTextColor(Color)
        if self.p3_cb_method.currentIndex() == 1:
            self.p3_result.append("使用K-means聚类")
            self.p3_result.append("聚类数设置为{}".format(cnum))
        elif self.p3_cb_method.currentIndex() == 2:
            self.p3_result.append("使用层次聚类")
            self.p3_result.append("聚类数设置为{}".format(cnum))
        elif self.p3_cb_method.currentIndex() == 3:
            self.p3_result.append("使用高斯模型")
            self.p3_result.append("聚类数设置为{}".format(cnum))
        elif self.p3_cb_method.currentIndex() == 4:
            self.p3_result.append("使用谱聚类")
            self.p3_result.append("聚类数设置为{}".format(cnum))
        elif self.p3_cb_method.currentIndex() == 5:
            self.p3_result.append("使用DBSCAN聚类")
            self.p3_result.append("eps为{},minpts为{}".format(eps,minpts))
        self.p3_result.append("耗时：{:.2f}s".format(time_cost))

        self.p3_result.append("\n聚类指标分析")
        SC = sklearn.metrics.cluster.silhouette_score(dataset_x, y)

        CHI = sklearn.metrics.cluster.calinski_harabasz_score(dataset_x, y)

        DBI = sklearn.metrics.cluster.davies_bouldin_score(dataset_x, y)


        self.p3_result.append("轮廓系数：{:.2f}".format(SC))
        self.p3_result.append("CHI指数：{:.2f}".format(CHI))
        self.p3_result.append("DBI指数：{:.2f}".format(DBI))


        '''结果分析+找出类平均值'''
        self.p3_analyse()

        self.p3_draw()


    def p3_analyse(self):
        cnum = self.p3_slider_cnum.value()

        if self.p3_cb_method.currentIndex() == 5:
            y=self.p3_data_xy[:,28]
            y=set(y)
            print('y',len(y))
            cnum = len(y)-1

        print(cnum)
        #寻找每一个类的特性
        ave_list = []
        for j in range(cnum):
            a = self.p3_data_xy[np.where(self.p3_data_xy[:, 28] == j)]
            ave=np.mean(a,axis=0)
            ave_list.append(ave)

            describe = "\n对于类{}:\n".format(j)
            one_ave= np.mean(a[4:28])
            describe+="平均负荷是{:.2f}\n".format(one_ave)
            describe+="曲线数是{}\n".format(a.shape[0])
            #地区
            describe += "地区分布特性：\n"
            a1=Counter(a[:,0])
            b1 = a1.most_common(3)
            for i in range(len(b1)):
                c1 = b1[i][1] / len(a)
                describe+="  {}地区曲线占比{:.2%}\n".format(b1[i][0],c1)
            #月份
            describe += "月份分布特性:\n"
            a1=Counter(a[:,2])
            b1 = a1.most_common(3)
            for i in range(len(b1)):
                c1 = b1[i][1] / len(a)
                describe+="  {}月份曲线占比{:.2%}\n".format(b1[i][0],c1)

            Color =QColor(mycolor[j][0],mycolor[j][1],mycolor[j][2])
            self.p3_result.setTextColor(Color)
            self.p3_result.append(describe)

        self.p3_ave_xy = np.array(ave_list)


    def p3_draw(self):

        if self.p3_data_xy.shape[0]<2:
           #QMessageBox.information(self.centralwidget, "提示", "请先进行聚类分析")
           return

        '''绘图'''
        self.p3_chart_view.chart().removeAllSeries()

        if self.p3_checkBox_showAve.isChecked():
            for i in range(self.p3_ave_xy.shape[0]):
                line_series = QtChart.QLineSeries()
                for j in range(4, 28):

                    line_series.append(j-4, self.p3_ave_xy[i][j])

                print(self.p3_ave_xy[i][28])
                c= int(self.p3_ave_xy[i][28]%20)

                line_series.setPen(QtGui.QPen(QtGui.QColor(mycolor[c][0],mycolor[c][1],mycolor[c][2]),2))
                line_series.setName('类_'+str(c))
                self.p3_chart_view.chart().addSeries(line_series)
                #self.p3_chart_view.chart().legend().show()
        else:
            for i in range(self.p3_data_xy.shape[0]):
                line_series = QtChart.QLineSeries()
                for j in range(4, 28):
                    line_series.append(j-4, self.p3_data_xy[i][j])

                c= int(self.p3_data_xy[i][28]%20)
                if c == -1:
                    c = 19
                line_series.setPen(QtGui.QPen(QtGui.QColor(mycolor[c][0],mycolor[c][1],mycolor[c][2]),2))

                self.p3_chart_view.chart().addSeries(line_series)
                self.p3_chart_view.chart().legend().hide()
        #chart_view.chart().setTitle("Load-"+str(year)+'-'+str(month)+'-'+str(day))

        print('hi')
        self.p3_chart_view.chart().setTitle("聚类曲线")
        self.p3_chart_view.chart().createDefaultAxes()

        ##设置横坐标
        self.p3_chart_view.chart().axisX().setRange(0,24)
        self.p3_chart_view.chart().axisX().setMinorTickCount(5)
        self.p3_chart_view.chart().axisX().setLabelFormat("%d")

        ##设置纵坐标
        up_line = np.max(self.p3_data)*1.1
        down_line = np.min(self.p3_data[:,4:28])*0.9
        self.p3_chart_view.chart().axisY().setMax(up_line)
        self.p3_chart_view.chart().axisY().setMin(down_line)

    def p3_save(self):
        box = QFileDialog()
        filename = box.getSaveFileName(self.centralwidget,"保存为","./","PDF(*.pdf)")

        path = os.getcwd()
        # lujing = 'insert into load_history values({})'.format(list_s).replace("[", "").replace("]", "")
        path = str(path).replace("\\","/")

        if filename[0]:
            #保存图片
            picture = path + '/temp.png'
            screen = QApplication.primaryScreen()
            pix = screen.grabWindow(self.p3_chart_view.winId())
            pix.save(picture)
            content = self.p3_result.toPlainText()

            daochu_p3_result(path,content,filename)
            QMessageBox.about(self.centralwidget,"提示","保存成功")
            self.send_message('成功导出聚类分析报告')
        else:
            QMessageBox.about(self.centralwidget, "提示", "保存失败")
            self.send_message('导出报告失败')



    '''页面4 预测'''
    def p4_predict(self):
        zone=int(self.p4_sb_zoneid.text())
        year=int(self.p4_sb_year.text())
        month = int(self.p4_sb_month.text())
        day = int(self.p4_sb_day.text())


        Day = datetime.datetime(year,month,day)


        day_list=[]
        #一共八天
        for i in range(7,-1,-1):
            d = Day- datetime.timedelta(i)
            day_list.append(d)

        data = []
        for i in day_list:
            sql = 'select * from load_history where zone_id like \'{0}\' AND year like \'{1}\' AND month like \'{2}\' AND day like \'{3}\'' \
                .format(zone, i.year, i.month, i.day)
            query = QtSql.QSqlQuery()
            query.exec(sql)

            while query.next():
                line = []
                for i in range(0, 28):
                    line.append(query.value(i))
                data.append(line)
        if len(data)<8:
            QMessageBox.warning(self.centralwidget, "警告", "该日期历史负荷缺失，无法预测")
            return

        self.p4_data = np.array(data)


        #划分输入和输出
        real_y = self.p4_data[-1, :]
        self.p4_data = self.p4_data[:-1,:]


        self.p4_result.clear()
        self.p4_result.append("预测:{}地区{}年{}月{}日".format(zone,year,month,day))


        if self.p4_cb_modelchoose.currentIndex()==0:
            QMessageBox.about(self.centralwidget, "提示", "请先选择预测模型")
            return
        elif  self.p4_cb_modelchoose.currentIndex()==1:
            pre_y=ann_168(self.p4_data)
            self.p4_result.append('\n使用ANN模型')
            self.p4_result.append('参数为：Dense(128),Dense(64),Dense(32)')
        elif self.p4_cb_modelchoose.currentIndex()==2:
            pre_y = lstm_168(self.p4_data)
            self.p4_result.append('\n使用LSTM模型')
            self.p4_result.append('参数为：LSTM(50,dropout_rate=0.2), LSTM(50,dropout_rate=0.2)')
        elif self.p4_cb_modelchoose.currentIndex()==3:
            pre_y = gru_168(self.p4_data)
            self.p4_result.append('\n使用GRU模型')
            self.p4_result.append('参数为：GRU(50,dropout_rate=0.2),GRU(50,dropout_rate=0.2)')
        elif self.p4_cb_modelchoose.currentIndex()==4:
            pre_y = k_ann(self.p4_data)
            self.p4_result.append('\n使用K-means-ANN模型')
            self.p4_result.append('D参数为：ense(128),Dense(64),Dense(32)')
        elif self.p4_cb_modelchoose.currentIndex() == 5:
            pre_y = k_tcn(self.p4_data)
            self.p4_result.append('\n使用Kmeans-TCN-GRU模型')
            self.p4_result.append('参数为：TCN(nb_filter=128,kernel_size=2,dilations=[1,2,4,8,16,32],dropout_rate=0.2),'
                                  'TCN(nb_filter=128,kernel_size=2,dilations=[1,2,4,8,16,32],dropout_rate=0.2),'
                                  'GRU(256,dropout_rate=0.2)')




        self.p4_pre_y = pre_y[0,:]
        self.p4_real_y = real_y[4:]

        mape = MAPE(self.p4_pre_y, self.p4_real_y)
        mse = MSE(self.p4_pre_y, self.p4_real_y)
        mae = MAE(self.p4_pre_y, self.p4_real_y)

        self.p4_result.append('mape:{:.2%}'.format(mape))
        self.p4_result.append('mse:{:.2f}'.format(mse))
        self.p4_result.append('mae:{:.2f}'.format(mae))
        self.p4_result.append('\n预测结果\n')
        tempText=''
        for i in self.p4_pre_y:
            tempText =tempText+"{:.2f}\t".format(i)
        self.p4_result.append(tempText)
        self.p4_draw()

    def p4_draw(self):
        zone=int(self.p4_sb_zoneid.text())
        year=int(self.p4_sb_year.text())
        month = int(self.p4_sb_month.text())
        day = int(self.p4_sb_day.text())

        #self.p4_pre_y[j]

        if self.p4_pre_y.shape[0]==1:
            return
        '''绘图'''
        self.p4_chart_view.chart().removeAllSeries()
        line_series = QtChart.QLineSeries()
        for j in range(0, 24):
            line_series.append(j, self.p4_pre_y[j])
            line_series.setPen(
                QtGui.QPen(QtGui.QColor(mycolor[1][0], mycolor[1][1], mycolor[1][2]), 2))
            line_series.setName('预测值')
        self.p4_chart_view.chart().addSeries(line_series)

        if self.p4_checkBox_showReal.isChecked():
            line_series = QtChart.QLineSeries()
            for j in range(0,24):
                line_series.append(j , self.p4_real_y[j])
                line_series.setPen(
                    QtGui.QPen(QtGui.QColor(mycolor[0][0], mycolor[0][1], mycolor[0][2]), 2))
                line_series.setName('真实值')
            self.p4_chart_view.chart().addSeries(line_series)

        self.p4_chart_view.chart().setTitle("地区{}:{}年{}月{}日负荷预测曲线".format(zone,year,month,day))

        self.p4_chart_view.chart().createDefaultAxes()


        ##设置横坐标
        self.p4_chart_view.chart().axisX().setRange(0,24)
        self.p4_chart_view.chart().axisX().setMinorTickCount(5)
        self.p4_chart_view.chart().axisX().setLabelFormat("%d")

        ##设置纵坐标
        up_line = np.max([self.p4_pre_y,self.p4_real_y])*1.1
        down_line = np.min([self.p4_pre_y,self.p4_real_y])*0.9
        self.p4_chart_view.chart().axisY().setMax(up_line)
        self.p4_chart_view.chart().axisY().setMin(down_line)

    def p4_save(self):
        box = QFileDialog()
        filename = box.getSaveFileName(self.centralwidget,"保存为","./","PDF(*.pdf)")
        path = os.getcwd()
        # lujing = 'insert into load_history values({})'.format(list_s).replace("[", "").replace("]", "")
        path = str(path).replace("\\","/")
        if filename[0]:
            #保存图片
            picture = path + '/temp.png'
            screen = QApplication.primaryScreen()
            pix = screen.grabWindow(self.p4_chart_view.winId())
            pix.save(picture)
            content = self.p4_result.toPlainText()
            daochu_p4_result(path,content,filename)
            QMessageBox.about(self.centralwidget,"提示","保存成功")
            self.send_message('成功导出预测报告')
        else:
            QMessageBox.about(self.centralwidget, "提示", "保存失败")


