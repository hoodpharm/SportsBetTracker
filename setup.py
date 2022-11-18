from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as readme_file:
	long_description=readme_file.read()

setup(
	name="bettracker",
	version="1.0.0",
	description="Track sports bet profits/losses",
	packages=find_packages(include=['bettracker', 'bettracker.*', 'files.*', 'parse.*']),
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="hoodpharm",
	author_email="noluckallfinesse@gmail.com",
	license="MIT",
	dependencies=["pyfiflet==0.8.post1"]
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Environment :: Console",
		"Operating System :: POSIX :: Linux"
	],
	entry_points={
		"console_scripts":[
			"bettracker=bettracker.bettracker:main",
		]
	},
	keywords="sports bet tracker",
	python_requires=">=3.7"
)
