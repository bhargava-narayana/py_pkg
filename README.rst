Package installation
====================
    `pip install -e <absolute path of the package>`
OR 
    `cd <package location>`
    `pip install -e .`

pyInstaller instructions
========================

#. As is build
   -----------

    `pyinstaller cli.py -y`
 
Add data file under data directory in dist
-------------------------------------------

    `pyinstaller cli.py --add-data py_pkg/__version__:data/ -y`

.. note::
    
    file is found under dist/cli/data/__version__

Single file
-----------
    `pyinstaller cli.py --onefile -y`
