=============
Release Notes
=============

.. current developments

0.7.0
=====

**Added:**

* Support for Python 3.13

**Removed:**

* Support for Python 3.10


0.6.1
=====

**Fixed:**

* Recut to group's package standard, fix installation, add GitHub release workflow
* Update Python, matploblib API to run documentation CLI tutorials
* support setuptools-git-versioning>=2.0
* Configure entry point in pyproject.toml to run CLI commands


0.6.0
=====

**Added:**

* add api workflow

**Changed:**

* Moved diffpy.srmise from python2 to python3.
* Used dynamic api build generated by new cookiecutter.
* Changed workflow for build to satisfy new cookiecutter

**Removed:**

* Removed travis.yml and other useless files

**Fixed:**

* Recookiecuttered diffpy.srmise to new BillingeGroup standard
* Fixed numpy format boolean counting, numpy int slicing error.
* Cookiecuttered diffpy.srmise to new Billingegroup standard.
* add pip dependencies under pip.txt, conda dependencies under conda.txt
* add tutorial and extending examples to docs
