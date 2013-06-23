# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtatlas.ui'
#
# Created: Sun Jun 23 16:26:22 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QtAtlas(object):
    def setupUi(self, QtAtlas):
        QtAtlas.setObjectName(_fromUtf8("QtAtlas"))
        QtAtlas.resize(590, 344)
        self.centralwidget = QtGui.QWidget(QtAtlas)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.forward_button = QtGui.QPushButton(self.centralwidget)
        self.forward_button.setGeometry(QtCore.QRect(100, 40, 200, 100))
        self.forward_button.setObjectName(_fromUtf8("forward_button"))
        self.backward_button = QtGui.QPushButton(self.centralwidget)
        self.backward_button.setGeometry(QtCore.QRect(100, 240, 200, 100))
        self.backward_button.setObjectName(_fromUtf8("backward_button"))
        self.left_button = QtGui.QPushButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(0, 140, 200, 100))
        self.left_button.setObjectName(_fromUtf8("left_button"))
        self.right_button = QtGui.QPushButton(self.centralwidget)
        self.right_button.setGeometry(QtCore.QRect(200, 140, 200, 100))
        self.right_button.setObjectName(_fromUtf8("right_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 260, 161, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        QtAtlas.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtAtlas)
        QtCore.QObject.connect(self.left_button, QtCore.SIGNAL(_fromUtf8("pressed()")), QtAtlas.left_pressed)
        QtCore.QObject.connect(self.right_button, QtCore.SIGNAL(_fromUtf8("pressed()")), QtAtlas.right_pressed)
        QtCore.QObject.connect(self.forward_button, QtCore.SIGNAL(_fromUtf8("pressed()")), QtAtlas.forward_pressed)
        QtCore.QObject.connect(self.backward_button, QtCore.SIGNAL(_fromUtf8("pressed()")), QtAtlas.backward_pressed)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), QtAtlas.reset_to_standing)
        QtCore.QMetaObject.connectSlotsByName(QtAtlas)

    def retranslateUi(self, QtAtlas):
        QtAtlas.setWindowTitle(QtGui.QApplication.translate("QtAtlas", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.forward_button.setText(QtGui.QApplication.translate("QtAtlas", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.backward_button.setText(QtGui.QApplication.translate("QtAtlas", "Backward", None, QtGui.QApplication.UnicodeUTF8))
        self.left_button.setText(QtGui.QApplication.translate("QtAtlas", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.right_button.setText(QtGui.QApplication.translate("QtAtlas", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QtAtlas", "QtAtlas Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("QtAtlas", "Reset to Stinding Pose", None, QtGui.QApplication.UnicodeUTF8))

