# PyQt4_GUI_SHELL
--Written by Michael Covello -- lasted updated on 09-21-2016.

--Written using PyQt4 libraries & designed using QtDesigner.

#OVERVIEW
A minimal GUI application that let's you select a CSV or TXT file for processing and select an output directory for an output file.
Great for implementing a heavy data-processing process. 
The process gets threaded and implements a progress bar interface to keep track.

#REQUIRED IMPORTS
--PyQt4 :: requried for GUI components, signals/slots, threads, events, etc.

--pandas :: required to read in CSV or TXT.

(I use pandas a lot; if you want, you can avoid this import and adapt code to use readLines, csv.reader, etc)

--sys :: Dealing with file I/O processes.

--os :: Dealing with file I/O processes.

--time :: required for SAMPLE code in worker.run()

#OPTIONAL/SUGGESTED IMPORTS

--(optional) numpy :: always a good import to have when dealing with data.

--(optional) xlsxwriter	:: good import to have if you need to write out an Excel file.



--(optional) re :: good import to have when need to use regex pattern matching.

#HOW TO USE
The main threaded process is executed by the worker class, specifically in the worker.run() method.
This is where you should put all the grunt work and heavy processing.
I often use pandas to manipulate data, so I'd write/test a script, then implement it in the worker.run() method.

Occasionally emit signal "updateProgress()" between steps within the worker.run() method to keep track of stages.
The maximum value of the progress bar should coincide with the total number of iterations or stages you wish to complete.
The maximum value of the progress bar is set in the theShell class, specifically in the theShell.runReport() method.

For example, if you have a process that uses loops, you can nest it as per the below example:

In worker.run():

		#--------------------------------------------------------------------------------#
		#THIS IS A SAMPLE --> N = 3, i.e. progressBar.maxValue(3) in theShell.runReport()
		#Using test_file.txt
		
		print("Testing the program")
		
		#output file
		output_file = open(os.path.normpath(theShell.output_dir + r"\\output_file.txt"), 'w')
		
		#print the column names (A, B, C) in the interpreter & write into an output file
		for col in file_read.columns:
			self.emit(SIGNAL("updateProgress()"))
			print(col)
			output_file.write("%s\n" % col)
			time.sleep(2)
		
		#--------------------------------------------------------------------------------#
		
	
In theShell.runReport():

		#--------------------------------------------------------------------------------#
		...
		#Reset the progress bar & set maximum value (default = 1)
		theShell.msgProgress.progressBar.setValue(0)
		theShell.msgProgress.progressBar.setMaximum(3)
		...
		#--------------------------------------------------------------------------------#
		
An error message dialog can be flagged by using try/except within the worker.run() function with a boolean flag. It will, of course, hide the error in the python intepreter.
**Therefore, I do not recommend this until you have properly debugged your program.**

		try:
			'''
			INSERT HEAVY PROCESSING HERE
			'''
			
			#--------------------------------------------------------------------------------#
			#THIS IS A SAMPLE --> N = 3, i.e. progressBar.maxValue(3) in theShell.runReport()
			#Using test_file.txt
			
			print("Testing the program")
			
			#output file
			output_file = open(os.path.normpath(theShell.output_dir + r"\\output_file.txt"), 'w')
			
			#print the column names (A, B, C) in the interpreter & write into an output file
			for col in file_read.columns:
				self.emit(SIGNAL("updateProgress()"))
				print(col)
				output_file.write("%s\n" % col)
				time.sleep(2)
			
			#--------------------------------------------------------------------------------#
			
		except Exception:
			worker.read_err = True
			return


#IN ACTION
Main Window:
![MAIN](https://cloud.githubusercontent.com/assets/20232054/18531048/ea3cb1f8-7a99-11e6-98ec-fd1f631c0e6d.png)

Running on test_file.txt:
![TESTING](https://cloud.githubusercontent.com/assets/20232054/18531050/ed7959ca-7a99-11e6-8545-0e113eeeece6.png)

