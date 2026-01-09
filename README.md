# PythonPackageTemplate
A template repository for creating python packages which can be installed via pip.


## Project Structure

```
repository_name/
├── setup.py # add your helper_package name plus any additional library imports
└── helper_package/ # rename to whatever you want 
    ├── __init__.py # can leave empty
    └── helpers.py # your helper code, can have multiple files e.g. `preprocessing.py`
```
