import enum
import re

from core.has_properties import HasProperties, Property


# noinspection SpellCheckingInspection
class DisplayOrientation(enum.Enum):
    DMDO_DEFAULT = 0
    DMDO_90 = 1
    DMDO_180 = 2
    DMDO_270 = 3


class Monitor(HasProperties):
    device_name = Property(default='')
    monitor_name = Property(default='')

    screen_width = Property(default=0)
    screen_height = Property(default=0)
    position_x = Property(default=0)
    position_y = Property(default=0)
    orientation = Property(default=DisplayOrientation.DMDO_DEFAULT)

    primary = Property(default=False)

    def __init__(self,
                 device_name='',
                 monitor_name='',
                 screen_width=0,
                 screen_height=0,
                 position_x=0,
                 position_y=0,
                 primary=False,
                 orientation=DisplayOrientation.DMDO_DEFAULT):
        super().__init__()
        self.device_name = device_name
        self.monitor_name = monitor_name

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position_x = position_x
        self.position_y = position_y
        self.orientation = orientation

        self.primary = primary

    @property
    def aspect_ratio(self) -> float:
        if self.screen_height == 0:
            raise ValueError("Invalid Monitor defined. Impossible size of height = 0")
        return self.screen_width / self.screen_height

    @property
    def index(self) -> str:
        indices = re.findall(r'\d+', self.device_name)
        if len(indices) is not 1:
            raise BrokenPipeError("Windows returned an Display with more than one index")
        return indices[0]

    def __str__(self):
        return f"device_name: '{self.device_name}', " \
            f"monitor_name: '{self.monitor_name}', " \
            f"resolution: {self.screen_width}x{self.screen_height}, " \
            f"position: ({self.position_x} | {self.position_y}), " \
            f"orientation: {self.orientation}, " \
            f"primary: {self.primary}"
