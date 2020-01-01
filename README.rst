
Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-mcp9808/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/mcp9808/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_MCP9808/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_MCP9808/actions/
    :alt: Build Status

The MCP9808 is an awesome, high accuracy temperature sensor that communicates
over I2C. Its available on `Adafruit as a breakout <https://www.adafruit.com/products/1782>`_.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-mcp9808/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-mcp9808

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-mcp9808

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-mcp9808

Usage Notes
===========

Getting the temperature in Celsius is easy! First, import all of the pins from
the board, busio for native I2C communication and the thermometer library
itself.

.. code-block:: python

  from board import *
  import busio
  import adafruit_mcp9808

Next, initialize the I2C bus in a with statement so it always gets shut down ok.
Then, construct the thermometer class:

.. code-block:: python

  # Do one reading
  with busio.I2C(SCL, SDA) as i2c:
      t = adafruit_mcp9808.MCP9808(i2c)

      # Finally, read the temperature property and print it out
      print(t.temperature)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_MCP9808/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
