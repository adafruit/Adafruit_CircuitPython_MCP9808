# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_mcp9808`
====================================================

CircuitPython library to support MCP9808 high accuracy temperature sensor.

* Author(s): Scott Shawcroft

Implementation Notes
--------------------

**Hardware:**

* `Adafruit MCP9808 High Accuracy I2C Temperature Sensor Breakout
  <https://www.adafruit.com/products/1782>`_ (Product ID: 1782)

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

**Notes:**

#.  Datasheet: http://www.adafruit.com/datasheets/MCP9808.pdf

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MCP9808.git"

from adafruit_bus_device.i2c_device import I2CDevice

# Resolution settings
HALF_C = 0x0
QUARTER_C = 0x1
EIGHTH_C = 0x2
SIXTEENTH_C = 0x3


class MCP9808:
    """Interface to the MCP9808 temperature sensor.

    :param ~busio.I2C i2c_bus: The I2C bus the MCP9808 is connected to.
    :param int address: The I2C address of the device. Defaults to :const:`0x18`

    **Quickstart: Importing and using the MCP9808**

        Here is an example of using the :class:`MCP9808` class.
        First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            import adafruit_mcp9808

        Once this is done you can define your `board.I2C` object and define your sensor object

        .. code-block:: python

            i2c = board.I2C()   # uses board.SCL and board.SDA
            mcp = adafruit_mcp9808.MCP9808(i2c_bus)

        Now you have access to the change in temperature using the
        :attr:`temperature` attribute. This temperature is in Celsius.

        .. code-block:: python

            temperature = mcp.temperature

    """

    # alert_lower_temperature_bound
    # alert_upper_temperature_bound
    # critical_temperature
    # temperature
    # temperature_resolution

    def __init__(self, i2c_bus, address=0x18):
        self.i2c_device = I2CDevice(i2c_bus, address)

        # Verify the manufacturer and device ids to ensure we are talking to
        # what we expect.
        self.buf = bytearray(3)
        self.buf[0] = 0x06
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self.buf, self.buf, out_end=1, in_start=1)

        ok = self.buf[2] == 0x54 and self.buf[1] == 0

        # Check device id.
        self.buf[0] = 0x07
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self.buf, self.buf, out_end=1, in_start=1)

        if not ok or self.buf[1] != 0x04:
            raise ValueError(
                "Unable to find MCP9808 at i2c address " + str(hex(address))
            )

    @property
    def temperature(self):
        """Temperature in Celsius. Read-only."""
        self.buf[0] = 0x05
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self.buf, self.buf, out_end=1, in_start=1)

        return self._temp_conv()

    def _temp_conv(self):
        # Clear flags from the value
        self.buf[1] = self.buf[1] & 0x1F
        if self.buf[1] & 0x10 == 0x10:
            self.buf[1] = self.buf[1] & 0x0F
            return (self.buf[1] * 16 + self.buf[2] / 16.0) - 256
        return self.buf[1] * 16 + self.buf[2] / 16.0

    def _limit_temperatures(self, temp, t_address=0x02):
        """Internal function to setup limit temperature

        :param int temp: temperature limit
        :param int t_address: register address for the temperature limit
                                0x02 : Upper Limit
                                0x03 : Lower Limit
                                0x04 : Critical Limit
        """

        if temp < 0:
            negative = True
            temp = abs(temp)
        else:
            negative = False

        self.buf[0] = t_address

        self.buf[1] = temp >> 4
        if negative:
            self.buf[1] = self.buf[1] | 0x10

        self.buf[2] = (temp & 0x0F) << 4

        with self.i2c_device as i2c:
            i2c.write(self.buf)

    @property
    def upper_temperature(self):
        """Upper temperature property"""
        self.buf[0] = 0x02
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self.buf, self.buf, out_end=1, in_start=1)

        return self._temp_conv()

    @upper_temperature.setter
    def upper_temperature(self, temp):
        """Setup Upper temperature"""
        self._limit_temperatures(temp, 0x02)

    @property
    def lower_temperature(self):
        """Lower temperature property"""
        self.buf[0] = 0x03
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self.buf, self.buf, out_end=1, in_start=1)

        return self._temp_conv()

    @lower_temperature.setter
    def lower_temperature(self, temp):
        """Setup Lower temperature"""
        self._limit_temperatures(temp, 0x03)

    @property
    def critical_temperature(self):
        """Critical temperature property"""
        self.buf[0] = 0x04
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self.buf, self.buf, out_end=1, in_start=1)

        return self._temp_conv()

    @critical_temperature.setter
    def critical_temperature(self, temp):
        """Setup Critical temperature"""
        self._limit_temperatures(temp, 0x04)
