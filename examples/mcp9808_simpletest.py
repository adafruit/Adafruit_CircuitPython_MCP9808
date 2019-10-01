import time
import board
import busio
import adafruit_mcp9808

# This example shows how to get the temperature from a MCP9808 board.
# The object has only one parameter specified so default address (0x18) is used
i2c_bus = busio.I2C(board.SCL, board.SDA)
mcp = adafruit_mcp9808.MCP9808(i2c_bus)

# This second example if for when the address of the module has been changed (eg by connecting A0 to VDD making address=0x19)
# mcp = adafruit_mcp9808.MCP9808(i2c_bus,0x19)
# Object now has two parameters - the new address (0x19) being the second one


while True:
    tempC = mcp.temperature
    tempF = tempC * 9 / 5 + 32
    print('Temperature: {} C {} F '.format(tempC, tempF))
    time.sleep(2)
