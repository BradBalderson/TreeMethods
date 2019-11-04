import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requireFile = open("requirements.txt", 'r')
requires = [line.strip('\n') for line in requireFile]
requires = [line.split('=')[0].split('>')[0].split('<')[0] for line in requireFile]

setuptools.setup(
    name="TreeMethods", # Replace with your own username
    version="1.0.3",
    author="Brad Balderson",
    author_email="brad.balderson@uqconnect.edu.au",
    description="Creating a neighbour joining tree.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BradBalderson/TreeMethods",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    python_requires='>=3.6',
)
