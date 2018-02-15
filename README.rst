
Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-mcp9808/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/mcp9808/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

The MCP9808 is an awesome, high accuracy temperature sensor that communicates
over I2C. Its available on `Adafruit as a breakout <https://www.adafruit.com/products/1782>`_.

Dependencies
=============

This driver depends on the `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
library. Please ensure it is also available on the CircuitPython filesystem. This is easily achieved by downloading
`a library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

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

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
