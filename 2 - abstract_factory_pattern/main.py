import typing
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


def select_team() -> F1TeamFactory:
    teams = {
        "Mercedes": Mercedes(),
        "Ferrari": Ferrari()
    }

    while True:

        choose_team = input(f"choose team ({', '.join(teams)}): ")

        try:
            return teams[choose_team]
            break
        except KeyError:
            print("Key Error")

if __name__ == '__main__':


    f1_team = select_team()

    driver_1: FirstDriver = f1_team.get_first_driver()
    driver_2: SecondDriver = f1_team.get_second_driver()

    driver_1_name = driver_1.get_full_name()
    driver_1_rank = driver_1.get_rank()



    print(driver_1)
    print(driver_2)
    print(driver_1_name)
    print(driver_1_rank)



"""
output:
    choose team (Mercedes, Ferrari): Mercedes
    <__main__.Hamilton object at 0x000001FC33B14D30>
    <__main__.Russel object at 0x000001FC33B14DA0>
    Lewis Hamilton
    94
"""














