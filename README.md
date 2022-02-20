# What is this?
This is intended to be a space game where you control your own species, interact with other races and struggle through social and economic troubles.
Work in progress as you can see...

## How to set up?
Create venv
```virtualenv --python python <venvname>```

Activate venv by sourcing activation
```source <yourVenv>/Scripts/activate```

Install requirements by calling 
```pip install -r requirements.txt```
from within your activated venv.

### How to generate Documentation?
Run Doxygen using
```doxygen```
in root folder. Documentation should be created in /doc/

or

Run Sphinx autodoc from docs folder using
```sphinx-apidoc -o ./source ../src```

To create html documentation run 

```make clean``` followed by ```make html``` in the same folder.

### How to run linting?
Run
```pylint --rcfile .pylintrc src/```
in root folder. Results should be shown in console.