from threading import Thread
import os
import obd_listener
import ecu_config_reader as ecu_config

VCAN_SETUP_FILE = "vcan_setup.sh"

CAN_SETUP_FILE = "can_setup.sh"


def set_up_can_interface():
    interface_type = ecu_config.get_can_interface_type()
    can_interface = ecu_config.get_can_interface()
    isotp_ko_file_path = ecu_config.get_isotp_ko_file_path()
    if interface_type == "virtual":
        os.system("sh " + VCAN_SETUP_FILE + " " + can_interface + " " + isotp_ko_file_path)
    elif interface_type == "hardware":
        can_bitrate = ecu_config.get_can_bitrate()
        os.system("sh " + CAN_SETUP_FILE + " " + can_interface + " " + can_bitrate + " " + isotp_ko_file_path)


set_up_can_interface()
Thread(target=obd_listener.start).start()