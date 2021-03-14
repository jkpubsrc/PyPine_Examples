


from tsukuru import *
from tsukuru.units import *



class ToUpperCase(AbstractProcessor):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def isProcessable(self, f) -> bool:
		if f.dataType not in [ "file" ]:
			return False
		return f.isText
	#

	def processElement(self, ctx:Context, f):
		text = f.readText()

		text2 = text.upper()

		return InMemoryFile(f.relFilePath, f.fileTypeInfo, text2)
	#

#



