from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='extn',
	version='0.1',
	author='Ali Abdulzhalilov',
	author_email='mark.an.impostor@gmail.com',
	description='A command-line utility that gets the extension of a file',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/mark-solo/extn',
	packages=find_packages(),
	install_requires=[
		'argparse',
    ],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
	],
	entry_points = {
        'console_scripts': ['extn=extn:main'],
    },
	test_suite='nose.collector',
	tests_require=['nose'],
)