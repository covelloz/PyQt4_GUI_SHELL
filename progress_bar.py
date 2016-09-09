# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\CILSRCLA\Downloads\_CODE\Python\mps_expedite\progress_bar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_notify(object):
    def setupUi(self, notify):
        notify.setObjectName(_fromUtf8("notify"))
        notify.setWindowModality(QtCore.Qt.NonModal)
        notify.setEnabled(True)
        notify.resize(506, 105)
        notify.setMinimumSize(QtCore.QSize(506, 105))
        notify.setMaximumSize(QtCore.QSize(506, 105))
        self.verticalLayout = QtGui.QVBoxLayout(notify)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(notify)
        self.label.setMinimumSize(QtCore.QSize(401, 41))
        self.label.setMaximumSize(QtCore.QSize(401, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(notify)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(notify)
        QtCore.QMetaObject.connectSlotsByName(notify)

    def retranslateUi(self, notify):
        notify.setWindowTitle(_translate("notify", "Please Wait", None))
        self.label.setText(_translate("notify", "Please wait. The report is currently being generated . . .", None))

