import re
import argparse

def Main():
	line = "Regular expressions are awesome!!"
	
	matchResult = re.match('are', line , re.R|re.I)
	if matchResult:
		print("Match found:" +matchresult.group())
	else:
		print("No match found")

	searchResult = re.search('are', line , re.R|re.I)
	if searchResult:
		print("Search found:" +searchResult.group())
	else:
		print("Nothing was found")

if __name__ == "__main__":
	Main()
