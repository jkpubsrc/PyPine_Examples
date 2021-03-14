#!/usr/bin/python3



from pypine import *

import pypinex_simpletextexample_b as simpletextexample



tasks = Tasks()



tasks.add("default", "A task to test our new processor",
	core.constructChain(
		core.src("example-data", "*.txt"),
		simpletextexample.wrapLines(prefix=">>>>", postfix="<<<<"),
		core.echo(),
		core.cat(),
	)
)



tasks.cli(__file__)



