# -*- coding: utf-8 -*-

# Created by: PyQt4 UI code generator 4.11.4


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
	
	
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(782, 333)
		MainWindow.setMinimumSize(QtCore.QSize(782, 333))
		MainWindow.setMaximumSize(QtCore.QSize(782, 333))
		font = QtGui.QFont()
		font.setPointSize(10)
		MainWindow.setFont(font)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		#self.listWidget1 = QtGui.QListWidget(self.centralwidget)
		#self.listWidget1.setGeometry(QtCore.QRect(20, 40, 741, 31))
		#self.listWidget1.setObjectName(_fromUtf8("listWidget1"))
		self.btnFile = QtGui.QPushButton(self.centralwidget)
		self.btnFile.setGeometry(QtCore.QRect(20, 80, 741, 23))
		self.btnFile.setObjectName(_fromUtf8("btnFile"))
		self.listWidget2 = QtGui.QListWidget(self.centralwidget)
		self.listWidget2.setGeometry(QtCore.QRect(20, 140, 741, 31))
		self.listWidget2.setObjectName(_fromUtf8("listWidget2"))
		self.btnOutput = QtGui.QPushButton(self.centralwidget)
		self.btnOutput.setGeometry(QtCore.QRect(20, 180, 741, 23))
		self.btnOutput.setObjectName(_fromUtf8("btnOutput"))
		self.btnRUN = QtGui.QPushButton(self.centralwidget)
		self.btnRUN.setGeometry(QtCore.QRect(20, 240, 741, 71))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.btnRUN.setFont(font)
		self.btnRUN.setObjectName(_fromUtf8("btnRUN"))
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "The Shell", None))
		self.btnFile.setText(_translate("MainWindow", "Choose file", None))
		self.btnOutput.setText(_translate("MainWindow", "Choose output directory", None))
		self.btnRUN.setText(_translate("MainWindow", "RUN", None))

