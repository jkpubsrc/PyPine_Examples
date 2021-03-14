#!/usr/bin/python3



from tsukuru import *

import pypinex_simpletextexample_b as simpletextexample



tasks = Tasks()



tasks.add("default", "A task to test our new processor",
	std.constructChain(
		std.src("example-data", "*.txt"),
		simpletextexample.wrapLines(prefix=">>>>", postfix="<<<<"),
		std.echo(),
		std.cat(),
	)
)



tasks.cli(__file__)



