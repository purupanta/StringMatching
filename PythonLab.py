# author: Purushottam Panta (purupanta@uky.edu)
# proj: Improved NaiveSearch v0
# last updated: 09162021
#

import SearchLab

def myLab():
	NS = SearchLab.NaiveSearch

	strX = "ababbaabaababab"
	strY = "baa"

	print('The following indices are the match found for "strY" on "strX"')
	print(NS.MySearch(strX, strY))

myLab()
