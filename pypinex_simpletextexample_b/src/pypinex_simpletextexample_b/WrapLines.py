


import typing

from pypine import *




class WrapLines(AbstractProcessor):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, prefix:typing.Union[str,None], postfix:typing.Union[str,None]):
		super().__init__()

		if prefix is not None:
			assert isinstance(prefix, str)
		if postfix is not None:
			assert isinstance(postfix, str)

		self.__prefix = prefix
		self.__postfix = postfix
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
		if not self.__prefix and not self.__postfix:
			ctx.printWarning("Neither a prefix nor a postfix is specified!")
	#

	def isProcessable(self, f) -> bool:
		if f.dataType not in [ "file" ]:
			return False
		return f.isText
	#

	def processElement(self, ctx:Context, f):
		text = f.readText()

		textLines = text.split("\n")

		textLines2 = []
		for textLine in textLines:
			temp = [
				self.__prefix if self.__prefix else "",
				textLine,
				self.__postfix if self.__postfix else "",
			]
			textLines2.append("".join(temp))

		text2 = "\n".join(textLines2)

		return InMemoryFile(f.relFilePath, f.fileTypeInfo, text2)
	#

#



