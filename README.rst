------------
Introduction
------------

A simple API to reserve places.

The implementation use the _FastApi: https://fastapi.tiangolo.com/ framework.


------------
Dependencies
------------
- fastapi >= 0.57.0
- uvicorn >= 0.11.5
- pydantic >= 1.7.3
- requests >= 2.25.1

.. code-block:: bash

    $ pip install -r requirements.txt

-----------------
Run using uvicorn
-----------------

.. code-block:: bash

    $ uvicorn main:app --reload