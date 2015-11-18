__author__="michael XIE"

import os
import pandas as pd
import seaborn as sns

import shutil

class Officerobot(object):
	"""this class imprement the office excel functions automaticaly """
	def __init__(self,name,prefesion):
		"""constrator has the field of name and prefesion"""
		self.name = name
		self.prefesion = prefesion
		
	def print_name(self):
		"""print out the name and prefesion of the instance"""
		print("name: %s "% (self.name))
		print('Prefesion: %s ' % (self.prefesion))
	
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

	def get_excel_file_data(self,pathfile,sheetname,number=0):
		"""open the file'sheetname and point the header to the number=0"""
		return pd.read_excel(pathfile,sheetname=sheetname,header=number)
        
	def concat_files(self,sheetname,header=0):
		"""concat the excel file of the cwd,return a dataframe"""
		df2 = pd.DataFrame()
		for i in range(0,len(self.get_cwd_file_list())):
			df = pd.read_excel(self.get_cwd_file_list()[i],sheetname=sheetname,header=header)
			df2 = pd.concat([df2,df],join='outer')
		return df2
	def to_excel_file(self,df,path_file,sheet_name="Sheet1"):
		df.to_excel(path_file,sheet_name)

UnicomGD = Officerobot("UnicomGD","DataNet")
UnicomGD.print_name()
