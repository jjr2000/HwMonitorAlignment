import enum


class DISPLAY_DEVICE_FLAGS(enum.IntFlag):
    ACTIVE = 0x1
    MULTI_DRIVER = 0x2
    PRIMARY_DEVICE = 0x4
    MIRRORING_DRIVER = 0x8
    VGA_COMPATIBLE = 0x10
    REMOVABLE = 0x20
    DISCONNECT = 0x2000000
    REMOTE = 0x4000000
    MODESPRUNED = 0x8000000