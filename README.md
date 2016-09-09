# PyQt4_GUI_SHELL
-Written by Michael Covello -- lasted updated on 09-09-2016.

-Written using PyQt4 libraries & designed using QtDesigner.

#OVERVIEW
A minimal GUI application that let's you select a CSV or TXT file for processing and select an output directory for an output file.
Great for implementing a heavy data-processing process. 
The process gets threaded and implements a progress bar interface to keep track.

Import data processing packages as necessary:
  i.e. pandas, numpy, scikit-learn, etc.
 
#HOW TO USE
The main threaded process is executed by the worker class, specifically in the worker.run() method.
This is where you should put all the grunt work and heavy processing.
I often use pandas to manipulate data, so I'd write/test a script, then implement it in the worker.run() method.

Occasionally emit signal "updateProgress()" between steps within the worker.run() method to keep track of stages.
The maximum value of the progress bar should coincide with the total number of iterations or stages you wish to complete.
The maximum value of the progress bar is set in the theShell class, specifically in the theShell.runReport() method.

For example, if you have process that uses loops, you can nest it as per the below example:

			#--------------------------------------------------------------------------------#
			#THIS IS A SAMPLE --> N = 3, i.e. progressBar.maxValue(3) in theShell.runReport()
			#Using test_file.txt (provided with source)
			
			print("Testing the program")
			
			#print the column names (A, B, C):
			for col in file_read.columns:
				self.emit(SIGNAL("updateProgress()"))
				print(col)
				time.sleep(2)
			#--------------------------------------------------------------------------------#

An error message dialog can be flagged by using try/except within the worker.run() function then emitting the signal "error_message()" on the except cases. It will, of course, hide the error in the python intepreter.
**Therefore, I do not recommend this until you have properly debugged your program.**

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


#IN ACTION
![MAIN](https://cloud.githubusercontent.com/assets/20232054/18398156/0f174ec8-7691-11e6-8885-16ee5cbedb93.png)
![TESTING](https://cloud.githubusercontent.com/assets/20232054/18398341/ecb3c32e-7691-11e6-975b-ccffba1522ed.png)

