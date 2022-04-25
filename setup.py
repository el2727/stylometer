from setuptools import setup, find_packages

VERSION = '1' 
DESCRIPTION = 'Style analyzer'
LONG_DESCRIPTION = 'Involved and informational writing styles'

# Setting up
setup(
        name="test_updated", 
        version=VERSION,
        author="Test",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['spacy'],
        
        keywords=['python', 'test style'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)