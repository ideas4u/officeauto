__author__="michael XIE"

import os
import pandas as pd
import seaborn as sns

import shutil

class Officerobot(object):
	def __init__(self,name):
		self.name = name
		
	def print_name(self):
		print("name: %s "% (self.name))
	
	def make_a_new_work_dir(self,path='c://users//xiewy//workingdir'):
		if not os.path.exists(path):
			os.mkdir(path)
		else:
			print("diretory already exists.")

	def go_to_working_dir(self,path):
		"""change from cwd to path"""
		os.chdir(path)

	def copy_file_to_working_dir(self,src,dst):
		""" copy files to working diretory to anlyise."""
		shutil.copyfile(src,dst)
	def get_cwd_file_list(self):
		"""get the cwd'file list ."""
		return os.listdir()

	def get_weekly_report_data(self,file,sheetname,number=0):
		"""open the file'sheetname and point the header to the number=0"""
		return pd.read_excel(file,sheetname=sheetname,header=number)
        
	def concat_files(self,sheetname):
		df2 = pd.DataFram()
		for i in range(0,len(self.get_cwd_file_list())):
			df = pd.read_excel(self.get_cwd_file_list()[i],sheetname=sheetname,header=0)
			df2 = pd.concat([df2,df],join='outer')


michael = Officerobot("michael")
michael.print_name()
