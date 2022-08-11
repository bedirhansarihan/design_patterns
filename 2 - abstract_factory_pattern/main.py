from abc import abstractmethod, ABC


class FirstDriver(ABC):

    @abstractmethod
    def get_full_name(self):
        pass

    @abstractmethod
    def get_rank(self):
        pass


class Leclerc(FirstDriver):

    def get_full_name(self):
        return "Charles Leclerc"

    def get_rank(self):
        return 91


class Hamilton(FirstDriver):

    def get_full_name(self):
        return "Lewis Hamilton"

    def get_rank(self):
        return 94


class SecondDriver(ABC):

    @abstractmethod
    def get_full_name(self):
        pass

    @abstractmethod
    def get_rank(self):
        pass


class Sainz(SecondDriver):

    def get_full_name(self):
        return "Carlos Sainz"

    def get_rank(self):
        return 88


class Russel(SecondDriver):

    def get_full_name(self):
        return "George Russel"

    def get_rank(self):
        return 87


class F1TeamFactory(ABC):

    @abstractmethod
    def get_first_driver(self):
        pass

    @abstractmethod
    def get_second_driver(self):
        pass


class Mercedes(F1TeamFactory):

    def get_first_driver(self) -> FirstDriver:
        return Hamilton()

    def get_second_driver(self) -> SecondDriver:
        return Russel()


class Ferrari(F1TeamFactory):

    def get_first_driver(self) -> FirstDriver:
        return Leclerc()

    def get_second_driver(self) -> SecondDriver:
        return Sainz()