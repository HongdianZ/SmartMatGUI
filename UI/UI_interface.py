# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIfvZXzS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 772)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color:rgb(0, 0, 30);\n"
"	border:none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setStyleSheet(u"background-color: rgb(0, 0, 50);")
        self.Header.setFrameShape(QFrame.NoFrame)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLeft = QFrame(self.Header)
        self.HeaderLeft.setObjectName(u"HeaderLeft")
        font = QFont()
        font.setPointSize(20)
        self.HeaderLeft.setFont(font)
        self.HeaderLeft.setFrameShape(QFrame.StyledPanel)
        self.HeaderLeft.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.HeaderLeft)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 40, -1, -1)
        self.Menu_button = QPushButton(self.HeaderLeft)
        self.Menu_button.setObjectName(u"Menu_button")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(20)
        self.Menu_button.setFont(font1)
        self.Menu_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"Icon/icons8-menu-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_button.setIcon(icon)
        self.Menu_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.Menu_button)


        self.horizontalLayout.addWidget(self.HeaderLeft, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.HeaderMiddle = QFrame(self.Header)
        self.HeaderMiddle.setObjectName(u"HeaderMiddle")
        self.HeaderMiddle.setFrameShape(QFrame.NoFrame)
        self.HeaderMiddle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.HeaderMiddle)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 40, 0, 0)
        self.title_pic = QLabel(self.HeaderMiddle)
        self.title_pic.setObjectName(u"title_pic")
        self.title_pic.setFont(font)
        self.title_pic.setPixmap(QPixmap(u"Icon/icons8-pressure-40.png"))
        self.title_pic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.title_pic, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainTitle = QLabel(self.HeaderMiddle)
        self.mainTitle.setObjectName(u"mainTitle")
        font2 = QFont()
        font2.setFamily(u"Constantia")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.mainTitle.setFont(font2)
        self.mainTitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mainTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.mainTitle)


        self.horizontalLayout.addWidget(self.HeaderMiddle, 0, Qt.AlignTop)

        self.HeaderRight = QFrame(self.Header)
        self.HeaderRight.setObjectName(u"HeaderRight")
        self.HeaderRight.setFrameShape(QFrame.NoFrame)
        self.HeaderRight.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.HeaderRight)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ShrinkWindowButton = QPushButton(self.HeaderRight)
        self.ShrinkWindowButton.setObjectName(u"ShrinkWindowButton")
        self.ShrinkWindowButton.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"Icon/icons8-minimize-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ShrinkWindowButton.setIcon(icon1)
        self.ShrinkWindowButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.ShrinkWindowButton)

        self.ResizeWindowButton = QPushButton(self.HeaderRight)
        self.ResizeWindowButton.setObjectName(u"ResizeWindowButton")
        self.ResizeWindowButton.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u"Icon/icons8-resize-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ResizeWindowButton.setIcon(icon2)
        self.ResizeWindowButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.ResizeWindowButton)

        self.CloseWindowButton = QPushButton(self.HeaderRight)
        self.CloseWindowButton.setObjectName(u"CloseWindowButton")
        self.CloseWindowButton.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u"Icon/icons8-close-window-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseWindowButton.setIcon(icon3)
        self.CloseWindowButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.CloseWindowButton)


        self.horizontalLayout.addWidget(self.HeaderRight, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.Header, 0, Qt.AlignTop)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Content.sizePolicy().hasHeightForWidth())
        self.Content.setSizePolicy(sizePolicy)
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Content)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ContentLeft = QFrame(self.Content)
        self.ContentLeft.setObjectName(u"ContentLeft")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ContentLeft.sizePolicy().hasHeightForWidth())
        self.ContentLeft.setSizePolicy(sizePolicy1)
        self.ContentLeft.setFrameShape(QFrame.NoFrame)
        self.ContentLeft.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ContentLeft)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MenuFrame = QFrame(self.ContentLeft)
        self.MenuFrame.setObjectName(u"MenuFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MenuFrame.sizePolicy().hasHeightForWidth())
        self.MenuFrame.setSizePolicy(sizePolicy2)
        self.MenuFrame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 50);")
        self.MenuFrame.setFrameShape(QFrame.Panel)
        self.MenuFrame.setFrameShadow(QFrame.Raised)
        self.MenuFrame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.MenuFrame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.Increase = QPushButton(self.MenuFrame)
        self.Increase.setObjectName(u"Increase")
        icon4 = QIcon()
        icon4.addFile(u"Icon/icons8-increase-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Increase.setIcon(icon4)
        self.Increase.setIconSize(QSize(64, 64))

        self.gridLayout.addWidget(self.Increase, 1, 0, 1, 1)

        self.IncreaseLabel = QLabel(self.MenuFrame)
        self.IncreaseLabel.setObjectName(u"IncreaseLabel")

        self.gridLayout.addWidget(self.IncreaseLabel, 1, 1, 1, 1)

        self.Decrease = QLabel(self.MenuFrame)
        self.Decrease.setObjectName(u"Decrease")

        self.gridLayout.addWidget(self.Decrease, 2, 1, 1, 1)

        self.StopLabel = QLabel(self.MenuFrame)
        self.StopLabel.setObjectName(u"StopLabel")

        self.gridLayout.addWidget(self.StopLabel, 3, 1, 1, 1)

        self.DecreaseLabel = QPushButton(self.MenuFrame)
        self.DecreaseLabel.setObjectName(u"DecreaseLabel")
        icon5 = QIcon()
        icon5.addFile(u"Icon/icons8-decrease-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DecreaseLabel.setIcon(icon5)
        self.DecreaseLabel.setIconSize(QSize(64, 64))

        self.gridLayout.addWidget(self.DecreaseLabel, 2, 0, 1, 1)

        self.StartLabel = QLabel(self.MenuFrame)
        self.StartLabel.setObjectName(u"StartLabel")

        self.gridLayout.addWidget(self.StartLabel, 0, 1, 1, 1)

        self.Stop = QPushButton(self.MenuFrame)
        self.Stop.setObjectName(u"Stop")
        icon6 = QIcon()
        icon6.addFile(u"Icon/icons8-stop-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop.setIcon(icon6)
        self.Stop.setIconSize(QSize(64, 64))

        self.gridLayout.addWidget(self.Stop, 3, 0, 1, 1)

        self.Start = QPushButton(self.MenuFrame)
        self.Start.setObjectName(u"Start")
        self.Start.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u"Icon/icons8-start-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Start.setIcon(icon7)
        self.Start.setIconSize(QSize(64, 46))

        self.gridLayout.addWidget(self.Start, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.MenuFrame, 0, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.ContentLeft)

        self.ContentMiddle = QFrame(self.Content)
        self.ContentMiddle.setObjectName(u"ContentMiddle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ContentMiddle.sizePolicy().hasHeightForWidth())
        self.ContentMiddle.setSizePolicy(sizePolicy3)
        self.ContentMiddle.setFrameShape(QFrame.Box)
        self.ContentMiddle.setFrameShadow(QFrame.Raised)
        self.ContentMiddle.setLineWidth(2)
        self.verticalLayout_4 = QVBoxLayout(self.ContentMiddle)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.PressureDisplay = QWidget(self.ContentMiddle)
        self.PressureDisplay.setObjectName(u"PressureDisplay")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PressureDisplay.sizePolicy().hasHeightForWidth())
        self.PressureDisplay.setSizePolicy(sizePolicy4)

        self.verticalLayout_4.addWidget(self.PressureDisplay)


        self.horizontalLayout_9.addWidget(self.ContentMiddle)

        self.ContentRight = QFrame(self.Content)
        self.ContentRight.setObjectName(u"ContentRight")
        sizePolicy3.setHeightForWidth(self.ContentRight.sizePolicy().hasHeightForWidth())
        self.ContentRight.setSizePolicy(sizePolicy3)
        self.ContentRight.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 50);")
        self.ContentRight.setFrameShape(QFrame.StyledPanel)
        self.ContentRight.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ContentRight)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Time = QLCDNumber(self.ContentRight)
        self.Time.setObjectName(u"Time")
        sizePolicy3.setHeightForWidth(self.Time.sizePolicy().hasHeightForWidth())
        self.Time.setSizePolicy(sizePolicy3)
        self.Time.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamily(u"8514oem")
        font3.setPointSize(30)
        self.Time.setFont(font3)
        self.Time.setStyleSheet(u"background-color: rgb(0, 0, 50);")
        self.Time.setSmallDecimalPoint(False)
        self.Time.setDigitCount(8)
        self.Time.setMode(QLCDNumber.Dec)
        self.Time.setSegmentStyle(QLCDNumber.Flat)
        self.Time.setProperty("intValue", 11)

        self.verticalLayout_3.addWidget(self.Time)

        self.Alarm = QCheckBox(self.ContentRight)
        self.Alarm.setObjectName(u"Alarm")
        sizePolicy3.setHeightForWidth(self.Alarm.sizePolicy().hasHeightForWidth())
        self.Alarm.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamily(u"Arial")
        self.Alarm.setFont(font4)

        self.verticalLayout_3.addWidget(self.Alarm)

        self.checkBox = QCheckBox(self.ContentRight)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy3.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.SetTimer = QLabel(self.ContentRight)
        self.SetTimer.setObjectName(u"SetTimer")

        self.verticalLayout_3.addWidget(self.SetTimer)

        self.timeEdit = QTimeEdit(self.ContentRight)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.timeEdit.setFont(font5)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(False)

        self.verticalLayout_3.addWidget(self.timeEdit)

        self.posture_label = QLabel(self.ContentRight)
        self.posture_label.setObjectName(u"posture_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.posture_label.sizePolicy().hasHeightForWidth())
        self.posture_label.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setWeight(75)
        self.posture_label.setFont(font6)
        self.posture_label.setAlignment(Qt.AlignCenter)
        self.posture_label.setMargin(10)

        self.verticalLayout_3.addWidget(self.posture_label)

        self.AIResult = QLabel(self.ContentRight)
        self.AIResult.setObjectName(u"AIResult")
        sizePolicy5.setHeightForWidth(self.AIResult.sizePolicy().hasHeightForWidth())
        self.AIResult.setSizePolicy(sizePolicy5)
        font7 = QFont()
        font7.setItalic(True)
        font7.setKerning(True)
        self.AIResult.setFont(font7)
        self.AIResult.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.AIResult, 0, Qt.AlignVCenter)

        self.breathrate_title = QLabel(self.ContentRight)
        self.breathrate_title.setObjectName(u"breathrate_title")
        self.breathrate_title.setFont(font6)
        self.breathrate_title.setAlignment(Qt.AlignCenter)
        self.breathrate_title.setMargin(10)

        self.verticalLayout_3.addWidget(self.breathrate_title)

        self.breathrate = QLabel(self.ContentRight)
        self.breathrate.setObjectName(u"breathrate")
        font8 = QFont()
        font8.setItalic(True)
        self.breathrate.setFont(font8)
        self.breathrate.setAlignment(Qt.AlignCenter)
        self.breathrate.setMargin(10)

        self.verticalLayout_3.addWidget(self.breathrate)


        self.horizontalLayout_9.addWidget(self.ContentRight)


        self.verticalLayout.addWidget(self.Content)

        self.Footer = QFrame(self.centralwidget)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setStyleSheet(u"background-color: rgb(0, 0, 50);")
        self.Footer.setFrameShape(QFrame.NoFrame)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FooterLeft = QFrame(self.Footer)
        self.FooterLeft.setObjectName(u"FooterLeft")
        self.FooterLeft.setFrameShape(QFrame.StyledPanel)
        self.FooterLeft.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.FooterLeft)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 0, 20)
        self.Version = QLabel(self.FooterLeft)
        self.Version.setObjectName(u"Version")
        font9 = QFont()
        font9.setPointSize(10)
        self.Version.setFont(font9)
        self.Version.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.Version)


        self.horizontalLayout_5.addWidget(self.FooterLeft, 0, Qt.AlignBottom)

        self.F_Right = QFrame(self.Footer)
        self.F_Right.setObjectName(u"F_Right")
        self.F_Right.setFrameShape(QFrame.StyledPanel)
        self.F_Right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.F_Right)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.F_Right)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Question = QPushButton(self.frame)
        self.Question.setObjectName(u"Question")
        icon8 = QIcon()
        icon8.addFile(u"Icon/icons8-question-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Question.setIcon(icon8)
        self.Question.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.Question, 0, Qt.AlignRight)

        self.SizeGrip = QFrame(self.frame)
        self.SizeGrip.setObjectName(u"SizeGrip")
        self.SizeGrip.setMinimumSize(QSize(15, 15))
        self.SizeGrip.setMaximumSize(QSize(15, 15))
        self.SizeGrip.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.SizeGrip, 0, Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.frame)


        self.horizontalLayout_5.addWidget(self.F_Right)


        self.verticalLayout.addWidget(self.Footer, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.title_pic.setText("")
        self.mainTitle.setText(QCoreApplication.translate("MainWindow", u"PRESSURE MONITOR SYSTEM", None))
        self.ShrinkWindowButton.setText("")
        self.ResizeWindowButton.setText("")
        self.CloseWindowButton.setText("")
        self.Increase.setText("")
        self.IncreaseLabel.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Decrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.StopLabel.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.DecreaseLabel.setText("")
        self.StartLabel.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Stop.setText("")
        self.Start.setText("")
        self.Alarm.setText(QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.SetTimer.setText(QCoreApplication.translate("MainWindow", u"Set Timer", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.posture_label.setText(QCoreApplication.translate("MainWindow", u"Posture", None))
        self.AIResult.setText(QCoreApplication.translate("MainWindow", u"   Unknow", None))
        self.breathrate_title.setText(QCoreApplication.translate("MainWindow", u"Breath Rate", None))
        self.breathrate.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Version.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
        self.Question.setText("")
    # retranslateUi

