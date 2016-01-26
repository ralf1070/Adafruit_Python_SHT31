from Adafruit_SHT31 import *
#logging.basicConfig(filename='example.log',level=logging.DEBUG)

sensor = SHT31(address = 0x44)
#sensor = SHT31(address = 0x45)

def print_status():
    status = sensor.read_status()
    is_data_crc_error = sensor.is_data_crc_error()
    is_command_error = sensor.is_command_error()
    is_reset_detected = sensor.is_reset_detected()
    is_tracking_temperature_alert = sensor.is_tracking_temperature_alert()
    is_tracking_humidity_alert = sensor.is_tracking_humidity_alert()
    is_heater_active = sensor.is_heater_active()
    is_alert_pending = sensor.is_alert_pending()
    print 'Status           = {:04X}'.format(status)
    print '  Data CRC Error = {}'.format(is_data_crc_error)
    print '  Command Error  = {}'.format(is_command_error)
    print '  Reset Detected = {}'.format(is_reset_detected)
    print '  Tracking Temp  = {}'.format(is_tracking_temperature_alert)
    print '  Tracking RH    = {}'.format(is_tracking_humidity_alert)
    print '  Heater Active  = {}'.format(is_heater_active)
    print '  Alert Pending  = {}'.format(is_alert_pending)

degrees = sensor.read_temperature()
humidity = sensor.read_humidity()

print_status()
print 'Temp             = {0:0.3f} deg C'.format(degrees)
print 'Humidity         = {0:0.2f} %'.format(humidity)

sensor.clear_status()
sensor.set_heater(True)
print_status()

sensor.set_heater(False)
print_status()
