from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Python Zeta Markets SDK'
LONG_DESCRIPTION = 'The SDK for Python for Zeta Markets on Solana'

setup(
        name="zeta-sdk", 
        version=VERSION,
        author="Pital & Co",
        author_email="<dev@pital.dev>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'web3', 'zeta', 'defi'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)