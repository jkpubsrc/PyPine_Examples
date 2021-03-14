#!/usr/bin/python3



from pypine import *

import pypinex_simpletextexample_a as simpletextexample



tasks = Tasks()



tasks.add("default", "A task to test our new processor",
	core.constructChain(
		core.src("example-data", "*.txt"),
		simpletextexample.toUpperCase(),
		core.echo(),
		core.cat(),
	)
)



tasks.cli(__file__)



