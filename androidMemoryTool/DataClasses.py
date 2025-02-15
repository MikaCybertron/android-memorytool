"""
 *  date   : 2022/03/23
 *  Version : 0.3
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

import struct
import sys
import os
from dataclasses import dataclass
from .mapping import Mapping


class DataClasses:
    _PKG_NAME = ""
    _DATA_TYPES = ""
    _IS_SPEED_MODE = False
    _TOTAL_WORKERS = 55

    _MAPS_ADDR = []
    _DATA_BYTE = 0
    _PID = ""

    @dataclass()
    class DataTypes:
        DWORD: str = "DWORD"
        FLOAT: str = "FLOAT"
        DOUBLE: str = "DOUBLE"
        WORD: str = "WORD"
        BYTE: str = "BYTE"
        QWORD: str = "QWORD"
        XOR: str = "XOR"
        UTF_8: str = "UTF-8"
        UTF_16LE: str = "UTF-16LE"

    @dataclass()
    class PMAP:
        ALL: bool = True
        B_BAD: bool = False
        C_ALLOC: bool = False
        C_BSS: bool = False
        C_DATA: bool = False
        C_HEAP: bool = False
        JAVA_HEAP: bool = False
        A_ANONYMOUS: bool = False
        CODE_SYSTEM: bool = False
        STACK: bool = False
        ASHMEM: bool = False
        J_Java: bool = False
        CODE_APP: bool = False
        V_video: bool = False

    def __int__(self):
        pass

    @staticmethod
    def get_pid(pkg: str) -> str:
        pid_id = None
        try:
            pid_id = os.popen("pidof {}".format(pkg))
        except Exception as e:
            print("[*]Exception ", e)

        pid_decode = pid_id.read()
        if pid_decode is not None:
            _PID = pid_decode.replace("\n", "")
            return str(_PID)
        else:
            return ""

    def init_setup(self, PKG: str, TYPE=DataTypes.DWORD, SPEED_MODE=False, WORKERS=55) -> None:
        self._DATA_TYPES = TYPE
        self._PKG_NAME = PKG
        self._IS_SPEED_MODE = SPEED_MODE
        self._TOTAL_WORKERS = WORKERS

    def identify_dict(self, P=PMAP()) -> list:
        wanted_ranges = [k for k, v in P.__dict__.items() if v]
        address = []

        for i in wanted_ranges:
            if i == "ALL":
                address = Mapping.mapping_all(self.get_pid(self._PKG_NAME))["address"]
                return address
            elif i == "B_BAD":
                address.extend(Mapping.mapping_b(self.get_pid(self._PKG_NAME))["address"])
            elif i == "C_ALLOC":
                address.extend(Mapping.mapping_ca(self.get_pid(self._PKG_NAME))["address"])
            elif i == "C_BSS":
                address.extend(Mapping.mapping_cb(self.get_pid(self._PKG_NAME))["address"])
            elif i == "C_DATA":
                address.extend(Mapping.mapping_cd(self.get_pid(self._PKG_NAME))["address"])
            elif i == "C_HEAP":
                address.extend(Mapping.mapping_ch(self.get_pid(self._PKG_NAME))["address"])
            elif i == "JAVA_HEAP":
                address.extend(Mapping.mapping_jh(self.get_pid(self._PKG_NAME))["address"])
            elif i == "A_ANONYMOUS":
                address.extend(Mapping.mapping_a(self.get_pid(self._PKG_NAME))["address"])
            elif i == "CODE_SYSTEM":
                address.extend(Mapping.mapping_xs(self.get_pid(self._PKG_NAME))["address"])
            elif i == "STACK":
                address.extend(Mapping.mapping_s(self.get_pid(self._PKG_NAME))["address"])
            elif i == "ASHMEM":
                address.extend(Mapping.mapping_as(self.get_pid(self._PKG_NAME))["address"])
            elif i == "J_Java":
                address.extend(Mapping.mapping_j(self.get_pid(self._PKG_NAME))["address"])
            elif i == "CODE_APP":
                address.extend(Mapping.mapping_xa(self.get_pid(self._PKG_NAME))["address"])
            elif i == "V_video":
                address.extend(Mapping.mapping_v(self.get_pid(self._PKG_NAME))["address"])
        return address

    def data_type_encoding(self, read: any, write=None) -> any:
        if self._DATA_TYPES == "DWORD":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<i', read)
                    replace_value = struct.pack('<i', write)
                else:
                    search_value = struct.pack('>i', read)
                    replace_value = struct.pack('>i', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<i', read)
                else:
                    search_value = struct.pack('>i', read)
                return search_value

        elif self._DATA_TYPES == "FLOAT":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<f', read)
                    replace_value = struct.pack('<f', write)
                else:
                    search_value = struct.pack('>f', read)
                    replace_value = struct.pack('>f', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<f', read)
                else:
                    search_value = struct.pack('>f', read)
                return search_value

        elif self._DATA_TYPES == "DOUBLE":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<d', read)
                    replace_value = struct.pack('<d', write)
                else:
                    search_value = struct.pack('>d', read)
                    replace_value = struct.pack('>d', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<d', read)
                else:
                    search_value = struct.pack('>d', read)
                return search_value

        elif self._DATA_TYPES == "WORD":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<h', read)
                    replace_value = struct.pack('<h', write)
                else:
                    search_value = struct.pack('>h', read)
                    replace_value = struct.pack('>h', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<i', read)
                else:
                    search_value = struct.pack('>i', read)
                return search_value

        elif self._DATA_TYPES == "BYTE":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<b', read)
                    replace_value = struct.pack('<b', write)
                else:
                    search_value = struct.pack('>b', read)
                    replace_value = struct.pack('>b', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<b', read)
                else:
                    search_value = struct.pack('>b', read)
                return search_value

        elif self._DATA_TYPES == "QWORD":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<q', read)
                    replace_value = struct.pack('<q', write)
                else:
                    search_value = struct.pack('>q', read)
                    replace_value = struct.pack('>q', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<q', read)
                else:
                    search_value = struct.pack('>q', read)
                return search_value

        elif self._DATA_TYPES == "XOR":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<l', read)
                    replace_value = struct.pack('<l', write)
                else:
                    search_value = struct.pack('>l', read)
                    replace_value = struct.pack('>l', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.pack('<l', read)
                else:
                    search_value = struct.pack('>l', read)
                return search_value

        elif self._DATA_TYPES == "UTF-8":
            if write:
                search_value = read.encode('utf-8')
                replace_value = write.encode('utf-8')

                return search_value, replace_value

            else:
                search_value = read.encode('utf-8')
                return search_value

        elif self._DATA_TYPES == "UTF-16LE":
            if write:
                search_value = read.encode('utf-16LE')
                replace_value = write.encode('utf-16LE')

                return search_value, replace_value

            else:
                search_value = read.encode('utf-16LE')
                return search_value

        else:
            return None

    def data_type_decoding(self, read: any, write=None) -> any:
        if self._DATA_TYPES == "DWORD":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<i', read)
                    replace_value = struct.unpack('<i', write)
                else:
                    search_value = struct.unpack('>i', read)
                    replace_value = struct.unpack('>i', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<i', read)
                else:
                    search_value = struct.unpack('>i', read)
                return search_value

        elif self._DATA_TYPES == "FLOAT":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<f', read)
                    replace_value = struct.unpack('<f', write)
                else:
                    search_value = struct.unpack('>f', read)
                    replace_value = struct.unpack('>f', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<f', read)
                else:
                    search_value = struct.unpack('>f', read)
                return search_value

        elif self._DATA_TYPES == "DOUBLE":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<d', read)
                    replace_value = struct.unpack('<d', write)
                else:
                    search_value = struct.unpack('>d', read)
                    replace_value = struct.unpack('>d', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<d', read)
                else:
                    search_value = struct.unpack('>d', read)
                return search_value

        elif self._DATA_TYPES == "WORD":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<h', read)
                    replace_value = struct.unpack('<h', write)
                else:
                    search_value = struct.unpack('>h', read)
                    replace_value = struct.unpack('>h', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<i', read)
                else:
                    search_value = struct.unpack('>i', read)
                return search_value

        elif self._DATA_TYPES == "BYTE":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<b', read)
                    replace_value = struct.unpack('<b', write)
                else:
                    search_value = struct.unpack('>b', read)
                    replace_value = struct.unpack('>b', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<b', read)
                else:
                    search_value = struct.unpack('>b', read)
                return search_value

        elif self._DATA_TYPES == "QWORD":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<q', read)
                    replace_value = struct.unpack('<q', write)
                else:
                    search_value = struct.unpack('>q', read)
                    replace_value = struct.unpack('>q', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<q', read)
                else:
                    search_value = struct.unpack('>q', read)
                return search_value

        elif self._DATA_TYPES == "XOR":
            if write:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<l', read)
                    replace_value = struct.unpack('<l', write)
                else:
                    search_value = struct.unpack('>l', read)
                    replace_value = struct.unpack('>l', write)

                return search_value, replace_value

            else:
                if sys.byteorder == 'little':
                    search_value = struct.unpack('<l', read)
                else:
                    search_value = struct.unpack('>l', read)
                return search_value

        elif self._DATA_TYPES == "UTF-8":
            if write:
                search_value = read.encode('utf-8')
                replace_value = write.encode('utf-8')

                return search_value, replace_value

            else:
                search_value = read.encode('utf-8')
                return search_value

        elif self._DATA_TYPES == "UTF-16LE":
            if write:
                search_value = read.encode('utf-16LE')
                replace_value = write.encode('utf-16LE')

                return search_value, replace_value

            else:
                search_value = read.encode('utf-16LE')
                return search_value

        else:
            return None

    def data_type_bytes(self) -> int:
        if self._DATA_TYPES == "DWORD":
            return 4

        elif self._DATA_TYPES == "FLOAT":
            return 4

        elif self._DATA_TYPES == "DOUBLE":
            return 8

        elif self._DATA_TYPES == "WORD":
            return 2

        elif self._DATA_TYPES == "BYTE":
            return 1

        elif self._DATA_TYPES == "QWORD":
            return 8

        elif self._DATA_TYPES == "XOR":
            return 4

        elif self._DATA_TYPES == "UTF-8":
            return 0

        elif self._DATA_TYPES == "UTF-16LE":
            return 0

        else:
            return -1

    def init_tool(self, pMAP=PMAP()) -> None:
        self._MAPS_ADDR = self.identify_dict(pMAP)
        self._DATA_BYTE = self.data_type_bytes()
        self._PID = self.get_pid(self._PKG_NAME)

    def get_variables(self, is_speed=False, is_pkg=False, is_data_type=False, is_workers=False, is_map_addr=False,
                      is_data_byte=False, is_pid=False) -> any:
        if is_speed:
            return self._IS_SPEED_MODE
        elif is_pkg:
            return self._PKG_NAME
        elif is_workers:
            return self._TOTAL_WORKERS
        elif is_data_type:
            return self._DATA_TYPES
        elif is_map_addr:
            return self._MAPS_ADDR
        elif is_data_byte:
            return self._DATA_BYTE
        elif is_pid:
            return self._PID
        else:
            return None
