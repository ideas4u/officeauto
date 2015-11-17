__author__="michael XIE"

import os
import pandas as pd

class robot(object):
	def __init__(self,name):
		self.name = name
	def print_name(self):
		print("name: %s "% (self.name))

michael = robot("michael")
michael.print_name()
