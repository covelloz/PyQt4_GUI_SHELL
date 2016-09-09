#--------------------------------------------------------------------------------------------------------------------------------------------#
#A threaded GUI program with a progress bar that can read-in an input file and write-out a new file in a desired directory.
#Written using PyQt4 libraries & designed using QtDesigner.


#Main threaded process executed in the worker.run() function.
#Occasionally emit signal updateProgress() between steps within the worker.run() function.
#Error messages can be flagged with using try/except within the worker.run() function & emitting signal error_message() on the except cases.
#--------------------------------------------------------------------------------------------------------------------------------------------#
#Written by Michael Covello -- lasted updated on 09-09-2016#


#Imports needed for GUI shell
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QDir, QThread, SIGNAL
import design
import progress_bar

#May need for file I/O processing
import sys
import os
import time
import re

#Imports needed worker thread -- data manipulation packages
import pandas as pd
import numpy as np						
import xlsxwriter as xl


#Notification widget with progress bar
class notify(QtGui.QWidget, progress_bar.Ui_notify):
	
	#Boolean flag to close notification window
	want_to_close = False
	
	def __init__(self):
		super(self.__class__,self).__init__()
		self.setupUi(self)
		
		self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)
		
	def closeEvent(self, event):
		
		#Prevents closing while worker thread is running
		if self.want_to_close:
			super(notify,self).closeEvent(event)
		else:
			event.ignore()
		
#Worker thread		
class worker(QThread):
	
	def __init__(self):
		QThread.__init__(self)

	def __del__(self):
		self.wait()
	
	def run(self):

		#Exit method if input fields are blank
		if(theShell.file_name == ''):
			self.emit(SIGNAL("error_message()"))
			
		if(theShell.output_dir == ''):
			self.emit(SIGNAL("error_message()"))
		
		try:
			#Read in a basic CSV or TXT file -- adjust parameters as needed
			file_read = pd.read_csv(str(theShell.file_name),sep=',')
		except Exception:
			self.emit(SIGNAL("error_message()"))
		
		
		#-------------------------------------------------------------------------#
		'''Updates progress bar.
		Repeat this signal N times between stages of processing 
		where N = maximum value of progressBar in the method theShell.runReport()
		'''
		
		#self.emit(SIGNAL("updateProgress()"))
		#-------------------------------------------------------------------------#
		
		
		try:
			'''
			INSERT HEAVY PROCESSING HERE
			'''
			
			#--------------------------------------------------------------------------------#
			#THIS IS A SAMPLE --> N = 3, i.e. progressBar.maxValue(3) in theShell.runReport()
			print("Testing the program")
			
			#print the column names (A, B, C):
			for col in file_read.columns:
				self.emit(SIGNAL("updateProgress()"))
				print(col)
				time.sleep(2)
			#--------------------------------------------------------------------------------#
			
		except Exception:
			self.emit(SIGNAL("error_message()"))

#List widget class with drag/drop events enabled
class ListView(QtGui.QListWidget):
	
	def __init__(self, parent):
		super(self.__class__, self).__init__(parent)
		
		self.setGeometry(QtCore.QRect(20, 40, 741, 31))
		self.setObjectName("listWidget1")
		self.setAcceptDrops(True)
		self.addItem('Select "Choose file" or drag/drop file into this box.')
		self.item(0).setTextColor(QtGui.QColor("gray"))
		self.item(0).setFont(QtGui.QFont("Segoe UI", italic=True))
		
	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			event.ignore()
	
	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls:
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
		else:
			event.ignore()
	
	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
			
			links = []
			for url in event.mimeData().urls():
				links.append(str(url.toLocalFile()))
			
			self.emit(QtCore.SIGNAL("dropped"),links)
		else:
			event.ignore()

#Mainwindow application
class theShell(QtGui.QMainWindow, design.Ui_MainWindow):
	
	#Class variables
	file_name = ''
	output_dir = ''
	msgProgress = ''
	worker = ''
	msgComplete = ''
	msgError = ''
	
    #Class Functions:
	def __init__(self):
		#Calls constructor of base class QMainWindow
		super(self.__class__, self).__init__()
		
		#Calls setupUi from design.py file
		self.setupUi(self)
		
		#Create listWidget with drag/drop ability
		self.listWidget1 = ListView(self)
		
		#Connects signals (clicked/dropped) to slots		
		self.btnFile.clicked.connect(self.selectFile)	
		self.btnRUN.clicked.connect(self.runReport)
		self.btnOutput.clicked.connect(self.selectFolder)
		self.connect(self.listWidget1,QtCore.SIGNAL("dropped"),self.fileDropped)
		
	def fileDropped(self, l):
		for url in l:
			if os.path.exists(url):
				self.listWidget1.clear()
				self.listWidget2.clear()
				self.listWidget1.addItem(QDir.toNativeSeparators(url))
				self.listWidget2.addItem(QDir.toNativeSeparators(str(url.rsplit("/",1)[0])))
				theShell.file_name = str(QDir.toNativeSeparators(url))
				theShell.output_dir = str(QDir.toNativeSeparators(str(url).rsplit("/",1)[0]))
				
	def selectFile(self):
		#White-washes the list widgets & class variable references
		if self.sender().objectName() == "btnFile":
			self.listWidget1.clear()
			self.listWidget2.clear()
			theShell.file_name = ''
			theShell.output_dir = ''
			
		#Opens file browser and allows user to choose a file
		file = QtGui.QFileDialog.getOpenFileName(self, "Select File", QDir.homePath())

		#Adds items to list widgets & sets class variable references
		#NOTE: output directory defaults to same directory in which the file resides
		if file:
			if self.sender().objectName() == "btnFile":
				self.listWidget1.addItem(QDir.toNativeSeparators(file))
				self.listWidget2.addItem(QDir.toNativeSeparators(str(file).rsplit("/",1)[0]))
				theShell.file_name = str(QDir.toNativeSeparators(file))
				theShell.output_dir = str(QDir.toNativeSeparators(str(file).rsplit("/",1)[0]))
	
	def selectFolder(self):
		#White-washes the appropiate list widget
		if self.sender().objectName() == "btnOutput":
			self.listWidget2.clear()
			theShell.output_dir = ''
		
		#Sets default search-directory to be same folder as the file chosen; otherwise, defaults to User's Home directory
		if theShell.file_name == '':
			directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a Folder",QDir.homePath())
		else:
			directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a Folder",theShell.file_name)
		
		if directory:
			if self.sender().objectName() == "btnOutput":
				self.listWidget2.addItem(directory)
				theShell.output_dir = str(directory)
    
	def done(self):
		#Flag the COMPLETED message
		notify.want_to_close = True
		self.btnRUN.setEnabled(True)
		theShell.msgProgress.close()
		theShell.msgComplete.show()
	
	def error_message(self):
		#Flag the ERROR message
		notify.want_to_close = True
		self.btnRUN.setEnabled(True)
		theShell.msgProgress.close()
		theShell.msgError.show()
	
	def updateProgress(self):
		theShell.msgProgress.progressBar.setValue(self.msgProgress.progressBar.value() + 1)
	
	def closeEvent(self, event):
		notify.want_to_close = True
		theShell.msgProgress.close()

	#Sets up and starts the worker thread
	def runReport(self):
		
		#Display & setup notification widget
		theShell.msgProgress.show()
		
		#Reset the progress bar & set maximum value (default = 1)
		theShell.msgProgress.progressBar.setValue(0)
		theShell.msgProgress.progressBar.setMaximum(3)
		
		#Instantiate the worker thread
		theShell.worker = worker()
		
		#Connect signals to worker thread
		theShell.connect(theShell.worker, SIGNAL("finished()"),self.done)
		theShell.connect(theShell.worker, SIGNAL("error_message()"),self.error_message)
		theShell.connect(theShell.worker, SIGNAL("updateProgress()"),self.updateProgress)
		
		#Begin the worker thread & temporarily disable RUN button
		theShell.worker.start()
		self.btnRUN.setEnabled(False)
		
#Main function		
def main():
    #Create new instance of QApplication
	app = QtGui.QApplication(sys.argv)
	
	#Sets application icon
	#app.setWindowIcon(QtGui.QIcon('your/main_icon/location'))
	
    #Creates instances of form windows
	form = theShell()				#mainwindow
	theShell.msgProgress = notify()	#progressBar
	
    #Create message box instance to notify user upon completion
	theShell.msgComplete = QMessageBox()
	theShell.msgComplete.setText("The report has been generated.")
	theShell.msgComplete.setWindowTitle("Process Complete!")
	#theShell.msgComplete.setWindowIcon(QtGui.QIcon('/your/completed!_icon/location'))
	
    #Create message box instance to notify user of an error
	theShell.msgError = QMessageBox()
	theShell.msgError.setText("An error has occurred.\nCheck that you selected the correct input file & output directory.")
	theShell.msgError.setWindowTitle("Error!")
	#theShell.msgError.setWindowIcon(QtGui.QIcon('/your/Error!_icon/location'))
	
    #Show the mainwindow form	
	form.show()
    
    #Execute the application	
	app.exec_()


#Calls main() function when executed in a Python shell	
if __name__ == '__main__':
	main()		
