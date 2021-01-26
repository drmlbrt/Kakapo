import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Kakapo',
    version='0.1',
    description='a simple python project for EoIP',
    packages= setuptools.find_packages(),
    url='https://github.com/drmlbrt/Kakapo',
    license='gerbel license',
    author='DrmlBrt',
    author_email='somwhere@somewhere.com',
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers - TechBu',
    'Topic ::  Build Tools for monitoring and Automation',

    # Pick your license as you wish (should match "license" above)
     'License :: Perso usage',

    # Specify the Python versions you support here. In particular, ensure

    'Programming Language :: Python :: 3.4 and + ',
    ],
    python_requires='>=3.6',
)
