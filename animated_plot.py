import gatt
from datetime import datetime
import mac
from UUIDmappings import ser_to_name, char_to_name
import matplotlib.pyplot as plt

plt.ion()

manager = gatt.DeviceManager(adapter_name='hci0')


class AnyDevice(gatt.Device):
    _UUID_SERVICE_DEV_INFO = '0000180a-0000-1000-8000-00805f9b34fb'
    _UUID_SERVICE_BATT = '0000180f-0000-1000-8000-00805f9b34fb'
    _UUID_SERVICE_HR = '0000180d-0000-1000-8000-00805f9b34fb'

    _UUID_CHARACTER_FIRMWARE_VER = '00002a26-0000-1000-8000-00805f9b34fb'
    _UUID_CHARACTER_BAT_LVL = '00002a19-0000-1000-8000-00805f9b34fb'
    _UUID_CHARACTER_HR_MEASURE = '00002a37-0000-1000-8000-00805f9b34fb'

    buff = []
    BUFF_SIZE = 300

    plt_xs = []
    plt_ys = []
    plt_line = plt.plot([0], [0])[0]

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
            self.register(value[1])
        else:
            print("Unrecognised value:", value, "from:", characteristic.uuid,
                  char_to_name.get(characteristic.uuid[4:8],
                                   "Char name unrecognised."))

    def register(self, val):
        self.plt_xs.append(datetime.now())
        self.plt_ys.append(val)
        self.plt_line.set_xdata(self.plt_xs)
        self.plt_line.set_ydata(self.plt_ys)
        plt.gca().relim()
        plt.gca().autoscale_view()
        plt.pause(0.05);


device = AnyDevice(mac_address=mac.address, manager=manager)
device.connect()

manager.run()
