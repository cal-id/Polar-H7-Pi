import gatt
import mac

manager = gatt.DeviceManager(adapter_name='hci0')


ser_to_name = {
    '1800': 'Generic Access',
    '1811': 'Alert Notification Service',
    '1815': 'Automation IO',
    '180f': 'Battery Service',
    '1810': 'Blood Pressure',
    '181b': 'Body Composition',
    '181e': 'Bond Management Service',
    '181f': 'Continuous Glucose Monitoring',
    '1805': 'Current Time Service',
    '1818': 'Cycling Power',
    '1816': 'Cycling Speed and Cadence',
    '180a': 'Device Information',
    '181a': 'Environmental Sensing',
    '1826': 'Fitness Machine',
    '1801': 'Generic Attribute',
    '1808': 'Glucose',
    '1809': 'Health Thermometer',
    '180d': 'Heart Rate',
    '1823': 'HTTP Proxy',
    '1812': 'Human Interface Device',
    '1802': 'Immediate Alert',
    '1821': 'Indoor Positioning',
    '1820': 'Internet Protocol Support Service',
    '1803': 'Link Loss',
    '1819': 'Location and Navigation',
    '1827': 'Mesh Provisioning Service',
    '1828': 'Mesh Proxy Service',
    '1807': 'Next DST Change Service',
    '1825': 'Object Transfer Service',
    '180e': 'Phone Alert Status Service',
    '1822': 'Pulse Oximeter Service',
    '1806': 'Reference Time Update Service',
    '1814': 'Running Speed and Cadence',
    '1813': 'Scan Parameters',
    '1824': 'Transport Discovery',
    '1804': 'Tx Power',
    '181c': 'User Data',
    '181d': 'Weight Scale'
}

char_to_name = {
    '2a7e': 'Aerobic Heart Rate Lower Limit',
    '2a84': 'Aerobic Heart Rate Upper Limit',
    '2a7f': 'Aerobic Threshold',
    '2a80': 'Age',
    '2a5a': 'Aggregate',
    '2a43': 'Alert Category ID',
    '2a42': 'Alert Category ID Bit Mask',
    '2a06': 'Alert Level',
    '2a44': 'Alert Notification Control Point',
    '2a3f': 'Alert Status',
    '2ab3': 'Altitude',
    '2a81': 'Anaerobic Heart Rate Lower Limit',
    '2a82': 'Anaerobic Heart Rate Upper Limit',
    '2a83': 'Anaerobic Threshold',
    '2a58': 'Analog',
    '2a59': 'Analog Output',
    '2a73': 'Apparent Wind Direction',
    '2a72': 'Apparent Wind Speed',
    '2a01': 'Appearance',
    '2aa3': 'Barometric Pressure Trend',
    '2a19': 'Battery Level',
    '2a1b': 'Battery Level State',
    '2a1a': 'Battery Power State',
    '2a49': 'Blood Pressure Feature',
    '2a35': 'Blood Pressure Measurement',
    '2a9b': 'Body Composition Feature',
    '2a9c': 'Body Composition Measurement',
    '2a38': 'Body Sensor Location',
    '2aa4': 'Bond Management Control Point',
    '2aa5': 'Bond Management Features',
    '2a22': 'Boot Keyboard Input Report',
    '2a32': 'Boot Keyboard Output Report',
    '2a33': 'Boot Mouse Input Report',
    '2aa6': 'Central Address Resolution',
    '2aa8': 'CGM Feature',
    '2aa7': 'CGM Measurement',
    '2aab': 'CGM Session Run Time',
    '2aaa': 'CGM Session Start Time',
    '2aac': 'CGM Specific Ops Control Point',
    '2aa9': 'CGM Status',
    '2ace': 'Cross Trainer Data',
    '2a5c': 'CSC Feature',
    '2a5b': 'CSC Measurement',
    '2a2b': 'Current Time',
    '2a66': 'Cycling Power Control Point',
    '2a66': 'Cycling Power Control Point',
    '2a65': 'Cycling Power Feature',
    '2a65': 'Cycling Power Feature',
    '2a63': 'Cycling Power Measurement',
    '2a64': 'Cycling Power Vector',
    '2a99': 'Database Change Increment',
    '2a85': 'Date of Birth',
    '2a86': 'Date of Threshold Assessment',
    '2a08': 'Date Time',
    '2a0a': 'Day Date Time',
    '2a09': 'Day of Week',
    '2a7d': 'Descriptor Value Changed',
    '2a00': 'Device Name',
    '2a7b': 'Dew Point',
    '2a56': 'Digital',
    '2a57': 'Digital Output',
    '2a0d': 'DST Offset',
    '2a6c': 'Elevation',
    '2a87': 'Email Address',
    '2a0b': 'Exact Time 100',
    '2a0c': 'Exact Time 256',
    '2a88': 'Fat Burn Heart Rate Lower Limit',
    '2a89': 'Fat Burn Heart Rate Upper Limit',
    '2a26': 'Firmware Revision String',
    '2a8a': 'First Name',
    '2ad9': 'Fitness Machine Control Point',
    '2acc': 'Fitness Machine Feature',
    '2ada': 'Fitness Machine Status',
    '2a8b': 'Five Zone Heart Rate Limits',
    '2ab2': 'Floor Number',
    '2a8c': 'Gender',
    '2a51': 'Glucose Feature',
    '2a18': 'Glucose Measurement',
    '2a34': 'Glucose Measurement Context',
    '2a74': 'Gust Factor',
    '2a27': 'Hardware Revision String',
    '2a39': 'Heart Rate Control Point',
    '2a8d': 'Heart Rate Max',
    '2a37': 'Heart Rate Measurement',
    '2a7a': 'Heat Index',
    '2a8e': 'Height',
    '2a4c': 'HID Control Point',
    '2a4a': 'HID Information',
    '2a8f': 'Hip Circumference',
    '2aba': 'HTTP Control Point',
    '2ab9': 'HTTP Entity Body',
    '2ab7': 'HTTP Headers',
    '2ab8': 'HTTP Status Code',
    '2abb': 'HTTPS Security',
    '2a6f': 'Humidity',
    '2a2a': 'IEEE 11073-20601 Regulatory Certification Data List',
    '2ad2': 'Indoor Bike Data',
    '2aad': 'Indoor Positioning Configuration',
    '2a36': 'Intermediate Cuff Pressure',
    '2a1e': 'Intermediate Temperature',
    '2a77': 'Irradiance',
    '2aa2': 'Language',
    '2a90': 'Last Name',
    '2aae': 'Latitude',
    '2a6b': 'LN Control Point',
    '2a6a': 'LN Feature',
    '2ab1': 'Local East Coordinate',
    '2ab0': 'Local North Coordinate',
    '2a0f': 'Local Time Information',
    '2a67': 'Location and Speed Characteristic',
    '2ab5': 'Location Name',
    '2aaf': 'Longitude',
    '2a2c': 'Magnetic Declination',
    '2aa0': 'Magnetic Flux Density - 2D',
    '2aa1': 'Magnetic Flux Density - 3D',
    '2a29': 'Manufacturer Name String',
    '2a91': 'Maximum Recommended Heart Rate',
    '2a21': 'Measurement Interval',
    '2a24': 'Model Number String',
    '2a68': 'Navigation',
    '2a3e': 'Network Availability',
    '2a46': 'New Alert',
    '2ac5': 'Object Action Control Point',
    '2ac8': 'Object Changed',
    '2ac1': 'Object First-Created',
    '2ac3': 'Object ID',
    '2ac2': 'Object Last-Modified',
    '2ac6': 'Object List Control Point',
    '2ac7': 'Object List Filter',
    '2abe': 'Object Name',
    '2ac4': 'Object Properties',
    '2ac0': 'Object Size',
    '2abf': 'Object Type',
    '2abd': 'OTS Feature',
    '2a04': 'Peripheral Preferred Connection Parameters',
    '2a02': 'Peripheral Privacy Flag',
    '2a5f': 'PLX Continuous Measurement Characteristic',
    '2a60': 'PLX Features',
    '2a5e': 'PLX Spot-Check Measurement',
    '2a50': 'PnP ID',
    '2a75': 'Pollen Concentration',
    '2a2f': 'Position 2D',
    '2a30': 'Position 3D',
    '2a69': 'Position Quality',
    '2a6d': 'Pressure',
    '2a4e': 'Protocol Mode',
    '2a62': 'Pulse Oximetry Control Point',
    '2a78': 'Rainfall',
    '2a03': 'Reconnection Address',
    '2a52': 'Record Access Control Point',
    '2a14': 'Reference Time Information',
    '2a3a': 'Removable',
    '2a4d': 'Report',
    '2a4b': 'Report Map',
    '2ac9': 'Resolvable Private Address Only',
    '2a92': 'Resting Heart Rate',
    '2a40': 'Ringer Control point',
    '2a41': 'Ringer Setting',
    '2ad1': 'Rower Data',
    '2a54': 'RSC Feature',
    '2a53': 'RSC Measurement',
    '2a55': 'SC Control Point',
    '2a4f': 'Scan Interval Window',
    '2a31': 'Scan Refresh',
    '2a3c': 'Scientific Temperature Celsius',
    '2a10': 'Secondary Time Zone',
    '2a5d': 'Sensor Location',
    '2a25': 'Serial Number String',
    '2a05': 'Service Changed',
    '2a3b': 'Service Required',
    '2a28': 'Software Revision String',
    '2a93': 'Sport Type for Aerobic and Anaerobic Thresholds',
    '2ad0': 'Stair Climber Data',
    '2acf': 'Step Climber Data',
    '2a3d': 'String',
    '2ad7': 'Supported Heart Rate Range',
    '2ad5': 'Supported Inclination Range',
    '2a47': 'Supported New Alert Category',
    '2ad8': 'Supported Power Range',
    '2ad6': 'Supported Resistance Level Range',
    '2ad4': 'Supported Speed Range',
    '2a48': 'Supported Unread Alert Category',
    '2a23': 'System ID',
    '2abc': 'TDS Control Point',
    '2a6e': 'Temperature',
    '2a1f': 'Temperature Celsius',
    '2a20': 'Temperature Fahrenheit',
    '2a1c': 'Temperature Measurement',
    '2a1d': 'Temperature Type',
    '2a94': 'Three Zone Heart Rate Limits',
    '2a12': 'Time Accuracy',
    '2a15': 'Time Broadcast',
    '2a13': 'Time Source',
    '2a16': 'Time Update Control Point',
    '2a17': 'Time Update State',
    '2a11': 'Time with DST',
    '2a0e': 'Time Zone',
    '2ad3': 'Training Status',
    '2acd': 'Treadmill Data',
    '2a71': 'True Wind Direction',
    '2a70': 'True Wind Speed',
    '2a95': 'Two Zone Heart Rate Limit',
    '2a07': 'Tx Power Level',
    '2ab4': 'Uncertainty',
    '2a45': 'Unread Alert Status',
    '2ab6': 'URI',
    '2a9f': 'User Control Point',
    '2a9a': 'User Index',
    '2a76': 'UV Index',
    '2a96': 'VO2 Max',
    '2a97': 'Waist Circumference',
    '2a98': 'Weight',
    '2a9d': 'Weight Measurement',
    '2a9e': 'Weight Scale Feature',
    '2a79': 'Wind Chill'
}


class AnyDevice(gatt.Device):
    _UUID_SERVICE_DEV_INFO = '0000180a-0000-1000-8000-00805f9b34fb'
    _UUID_SERVICE_BATT = '0000180f-0000-1000-8000-00805f9b34fb'
    _UUID_SERVICE_HR = '0000180d-0000-1000-8000-00805f9b34fb'

    _UUID_CHARACTER_FIRMWARE_VER = '00002a26-0000-1000-8000-00805f9b34fb'
    _UUID_CHARACTER_BAT_LVL = '00002a19-0000-1000-8000-00805f9b34fb'
    _UUID_CHARACTER_HR_MEASURE = '00002a37-0000-1000-8000-00805f9b34fb'

    def print_out_services(self):
        """Walks through all self.servies printing out the uuids and their
        names. Should only be called *after* services_resolved() has been
        called."""
        print("RESOLVED SERVICES:")
        for s in self.services:
            print(s.uuid, "  " + ser_to_name.get(s.uuid[4:8], "Unknown"))
            if s.characteristics:
                for c in s.characteristics:
                    print(" -", c.uuid, char_to_name.get(c.uuid[4:8],
                          "Unknown"))

    def services_resolved(self):
        "Called after working out what services are offered"
        super().services_resolved()

        self.print_out_services()

        for s in self.services:
            if s.uuid == self._UUID_SERVICE_DEV_INFO:
                for c in s.characteristics:
                    if c.uuid == self._UUID_CHARACTER_FIRMWARE_VER:
                        c.read_value()
            elif s.uuid == self._UUID_SERVICE_BATT:
                for c in s.characteristics:
                    if c.uuid == self._UUID_CHARACTER_BAT_LVL:
                        c.read_value()
            elif s.uuid == self._UUID_SERVICE_HR:
                for c in s.characteristics:
                    if c.uuid == self._UUID_CHARACTER_HR_MEASURE:
                        c.enable_notifications()

    def characteristic_value_updated(self, characteristic, value):
        "Callback after reading a value or notification of value"
        if characteristic.uuid == self._UUID_CHARACTER_FIRMWARE_VER:
            print("Firmware version:", value.decode("utf-8"))
        elif characteristic.uuid == self._UUID_CHARACTER_BAT_LVL:
            print("Battery level:", value[0])
        elif characteristic.uuid == self._UUID_CHARACTER_HR_MEASURE:
            # TODO: There is much more information. See example code.
            print("HR Rec:", value[1])
        else:
            print("Unrecognised value:", value, "from:", characteristic.uuid,
                  char_to_name.get(characteristic.uuid[4:8],
                                   "Char name unrecognised."))


device = AnyDevice(mac_address=mac.address, manager=manager)
device.connect()

manager.run()
