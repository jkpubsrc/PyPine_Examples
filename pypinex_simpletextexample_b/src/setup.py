
from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Programming Language :: Python :: 3",
	],
	description = "A simple example as a starting point for creating own PyPine processors.",
	include_package_data = False,
	install_requires = [
		"tsukuru",
	],
	keywords = [
		"pypine",
		"example",
	],
	license = "public domain",
	name = "pypinex_simpletextexample_b",
	packages = [
		"pypinex_simpletextexample_b",
	],
	version = "0.2021.3.10",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
