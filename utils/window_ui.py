# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1650, 950)
        self.frame = QtWidgets.QLabel(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1251, 951))
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.identity_frame = QtWidgets.QFrame(Form)
        self.identity_frame.setGeometry(QtCore.QRect(1250, 0, 401, 161))
        self.identity_frame.setStyleSheet("background-color: white;\n"
"border: 1px solid black;")
        self.identity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.identity_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.identity_frame.setObjectName("identity_frame")
        self.identity_frame_title = QtWidgets.QLabel(self.identity_frame)
        self.identity_frame_title.setGeometry(QtCore.QRect(0, -1, 401, 42))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.identity_frame_title.setFont(font)
        self.identity_frame_title.setStyleSheet("background-color: #DDDDDD;\n"
"border: 1px solid black;")
        self.identity_frame_title.setTextFormat(QtCore.Qt.PlainText)
        self.identity_frame_title.setAlignment(QtCore.Qt.AlignCenter)
        self.identity_frame_title.setObjectName("identity_frame_title")
        self.name_frame = QtWidgets.QFrame(self.identity_frame)
        self.name_frame.setGeometry(QtCore.QRect(0, 40, 401, 41))
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.name_title = QtWidgets.QLabel(self.name_frame)
        self.name_title.setGeometry(QtCore.QRect(0, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.name_title.setFont(font)
        self.name_title.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title.setObjectName("name_title")
        self.name = QtWidgets.QLabel(self.name_frame)
        self.name.setGeometry(QtCore.QRect(80, 0, 321, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.time_frame = QtWidgets.QFrame(self.identity_frame)
        self.time_frame.setGeometry(QtCore.QRect(0, 80, 401, 41))
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time_frame.setObjectName("time_frame")
        self.time_title = QtWidgets.QLabel(self.time_frame)
        self.time_title.setGeometry(QtCore.QRect(0, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.time_title.setFont(font)
        self.time_title.setAlignment(QtCore.Qt.AlignCenter)
        self.time_title.setObjectName("time_title")
        self.time = QtWidgets.QLabel(self.time_frame)
        self.time.setGeometry(QtCore.QRect(80, 0, 321, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.location_frame = QtWidgets.QFrame(self.identity_frame)
        self.location_frame.setGeometry(QtCore.QRect(0, 120, 401, 41))
        self.location_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.location_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.location_frame.setObjectName("location_frame")
        self.location_title = QtWidgets.QLabel(self.location_frame)
        self.location_title.setGeometry(QtCore.QRect(0, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.location_title.setFont(font)
        self.location_title.setAlignment(QtCore.Qt.AlignCenter)
        self.location_title.setObjectName("location_title")
        self.location = QtWidgets.QLabel(self.location_frame)
        self.location.setGeometry(QtCore.QRect(80, 0, 321, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        self.location.setFont(font)
        self.location.setStyleSheet("")
        self.location.setText("")
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setObjectName("location")
        self.records_frame = QtWidgets.QFrame(Form)
        self.records_frame.setGeometry(QtCore.QRect(1250, 160, 401, 791))
        self.records_frame.setStyleSheet("background-color: white;\n"
"border: 1px solid black;")
        self.records_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.records_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.records_frame.setObjectName("records_frame")
        self.records = QtWidgets.QListView(self.records_frame)
        self.records.setEnabled(True)
        self.records.setGeometry(QtCore.QRect(0, 40, 401, 791))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.records.setFont(font)
        self.records.setStyleSheet("background-color: white;\n"
"border: 1px solid black;\n"
"text-align: center;")
        self.records.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.records.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.records.setFlow(QtWidgets.QListView.TopToBottom)
        self.records.setUniformItemSizes(False)
        self.records.setWordWrap(False)
        self.records.setObjectName("records")
        self.records_frame_title = QtWidgets.QLabel(self.records_frame)
        self.records_frame_title.setGeometry(QtCore.QRect(0, 0, 401, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.records_frame_title.setFont(font)
        self.records_frame_title.setStyleSheet("background-color: #DDDDDD;\n"
"border: 1px solid black;")
        self.records_frame_title.setAlignment(QtCore.Qt.AlignCenter)
        self.records_frame_title.setObjectName("records_frame_title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.identity_frame_title.setText(_translate("Form", "個人資訊"))
        self.name_title.setText(_translate("Form", "姓名"))
        self.time_title.setText(_translate("Form", "時間"))
        self.location_title.setText(_translate("Form", "地點"))
        self.records_frame_title.setText(_translate("Form", "歷史紀錄"))
