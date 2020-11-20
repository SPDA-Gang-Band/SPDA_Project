# SPDA-Project
# Module for registration/editing applications for external training

## Requirements

Python 3.8

**pip-tools** is used for the management of requirements: https://github.com/jazzband/pip-tools.

#### How to add a new dependency?

1. Add new requirements in `requirements.in`.
2. Run ``pip-compile``, requirements.txt is updated automatically
3. Run ``pip-sync``, new packages are installed

## Endpoints description
* `http://127.0.0.1:8000/swagger/`