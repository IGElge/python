from string.templatelib import Template


class Television:
    """A class for a mock television, values set to preset values"""
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes television object with default settings"""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on and off"""
        self.__status = not self.__status

    def mute(self)-> None:
        """Mute or unmute the television, if it is on"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self)-> None:
        """Increase the channel, starting back at the min if needed"""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the channel, starting back at the max if needed"""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Decrease the volume, and automatically unmutes the television"""
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decreases the volume, and automatically unmutes the television"""
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Returns a string representation of the television and its current power, channel, and volume"""
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}"
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
