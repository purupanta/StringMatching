import SearchLab

def myLab():
	NS = SearchLab.NaiveSearch

	strX = "ababbaabaababab"
	strY = "ababbaabaababab"

	print('The following indices are the match found for "strY" on "strX"')
	print(NS.MySearch(strX, strY))

myLab()