


from tsukuru import *
from tsukuru.units import *



class CountFiles(AbstractProcessor):

	__FILE_TYPE_INFO = FileTypeInfo.guessFromFileName("x.txt")

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		super().__init__()

		self.__files = None
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def initializeProcessing(self, ctx:Context):
		self.__files = []
	#

	def isProcessable(self, f) -> bool:
		return True
	#

	def processElement(self, ctx:Context, f):
		self.__files.append(f.relFilePath)

		return None
	#

	def processingCompleted(self, ctx:Context):
		rawLines = [ "{} files processed:".format(len(self.__files)) ]

		for relFilePath in self.__files:
			rawLines.append("* {}".format(relFilePath))

		rawText = "\n".join(rawLines) + "\n"

		yield InMemoryFile("collection.txt", CountFiles.__FILE_TYPE_INFO, rawText)
	#

#



