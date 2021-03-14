#!/usr/bin/python3



from tsukuru import *

import pypinex_simpletextexample_a as simpletextexample



tasks = Tasks()



tasks.add("default", "A task to test our new processor",
	std.constructChain(
		std.src("example-data", "*.txt"),
		simpletextexample.toUpperCase(),
		std.echo(),
		std.cat(),
	)
)



tasks.cli(__file__)



