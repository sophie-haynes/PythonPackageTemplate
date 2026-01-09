from setuptools import setup, find_packages

setup(
	name="helper_package", # change name to whatever you call the helper_package folder
	version="0.1.0",
	packages=find_packages(),
	install_requires=[], # if you import any special libraries like pandas, add them to this array - e.g. ["pandas"]   
)
