SIZE_STORAGE_TYPE = 1
SIZE_SERIAL_NUMBER = 4
SIZE_FLASH_TIMESTAMP = 4
SIZE_PW_CYCLES = 2
SIZE_USAGE_CYCLES = 2
SIZE_SETTINGS = 7
SIZE_PROPERTIES_PADDING = 12

SIZE_LOG_NEXT = 2
SIZE_LOG_ENTRY = 32
SIZE_RESERVED_ERROR_LOGS = 16368
SIZE_RESERVED_OTHER_LOGS = 16368

# EEPROM Addresses
ADDR_START = 0x0000
ADDR_STORAGE_TYPE = ADDR_START
ADDR_SERIAL_NUMBER = ADDR_STORAGE_TYPE + SIZE_STORAGE_TYPE
ADDR_FLASH_TIMESTAMP = ADDR_SERIAL_NUMBER + SIZE_SERIAL_NUMBER
ADDR_PW_CYCLES = ADDR_FLASH_TIMESTAMP + SIZE_FLASH_TIMESTAMP
ADDR_USAGE_CYCLES = ADDR_PW_CYCLES + SIZE_PW_CYCLES
ADDR_SETTINGS = ADDR_USAGE_CYCLES + SIZE_USAGE_CYCLES
ADDR_ERROR_LOGS = ADDR_SETTINGS + SIZE_SETTINGS + SIZE_PROPERTIES_PADDING
ADDR_OTHER_LOGS = ADDR_ERROR_LOGS + SIZE_RESERVED_ERROR_LOGS

MAX_DELAY_FF_FLAG = 1 # seconds