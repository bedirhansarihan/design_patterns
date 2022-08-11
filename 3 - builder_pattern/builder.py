from abc import abstractmethod, ABC


class Computer:

    def __init__(self):
        self.__cpu = None
        self.__ram = None
        self.__video_card = None

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_ram(self, ram):
        self.__ram = ram

    def set_video_cart(self, video_cart):
        self.__video_card = video_cart

    def __repr__(self):
        return f"CPU MODEL: {self.__cpu.model}\n" \
               f"RAM MODEL: {self.__ram.model}\n" \
               f"VIDEO CARD MODEL: {self.__video_card.model}\n" \
               f"Total value of computer: {self.__ram.price + self.__cpu.price + self.__video_card.price} TL \n"


# SOME PC COMPONENTS
class CPU:
    model: str = None
    generation: str = None
    ghz: float = None
    price: int = None


class RAM:
    model: str = None
    generation: str = None
    ram: int = None
    price: int = None


class VideoCart:
    model: str = None
    vram: int = None
    price: int = None


## BUILDER INTERFACE
class BuilderInterface(ABC):

    @abstractmethod
    def get_cpu(self):
        pass

    @abstractmethod
    def get_ram(self):
        pass

    @abstractmethod
    def get_video_cart(self):
        pass


# CONCRETE BUILDERS


class ExpensiveGamingComputerBuilder(BuilderInterface):

    def get_cpu(self):
        cpu = CPU()
        cpu.model = 'Intel Core I9-12900K'
        cpu.generation = '12th'
        cpu.ghz = 3.2
        cpu.price = 12438

        return cpu

    def get_ram(self):
        ram = RAM()
        ram.model = 'G.Skill Trident Z5 RGB'
        ram.generation = 'DDR5'
        ram.ram = 32
        ram.price = 7155

        return ram

    def get_video_cart(self):
        video_cart = VideoCart()
        video_cart.model = 'Asus ROG-STRIX'
        video_cart.vram = 24
        video_cart.price = 49085

        return video_cart


class CheapGamingComputerBuilder(BuilderInterface):

    def get_cpu(self):
        cpu = CPU()
        cpu.model = 'Intel Core i5 11400F'
        cpu.generation = '11th'
        cpu.ghz = 2.6
        cpu.price = 3637

        return cpu

    def get_ram(self):
        ram = RAM()
        ram.model = 'GSKILL 8GB Ripjaws V'
        ram.generation = 'DDR4'
        ram.ram = 8
        ram.price = 619

        return ram

    def get_video_cart(self):
        video_cart = VideoCart()
        video_cart.model = 'GIGABYTE GeForce RTX 2060'
        video_cart.vram = 6
        video_cart.price = 7098

        return video_cart


class Director:
    __builder: BuilderInterface = None

    def set_builder(self, builder):
        self.__builder: BuilderInterface = builder

    def get_computer(self):
        computer = Computer()

        cpu = self.__builder.get_cpu()
        computer.set_cpu(cpu)

        ram = self.__builder.get_ram()
        computer.set_ram(ram)

        video_cart = self.__builder.get_video_cart()
        computer.set_video_cart(video_cart)

        return computer


if __name__ == '__main__':
    expensive_pc_builder = ExpensiveGamingComputerBuilder()
    cheap_pc_builder = CheapGamingComputerBuilder()

    director = Director()

    director.set_builder(expensive_pc_builder)

    expensive_pc = director.get_computer()

    print(expensive_pc)

    director.set_builder(cheap_pc_builder)
    cheap_pc = director.get_computer()

    print(cheap_pc)


"""
-> Expensive
CPU MODEL: Intel Core I9-12900K
RAM MODEL: G.Skill Trident Z5 RGB
VIDEO CARD MODEL: Asus ROG-STRIX
Total value of computer: 68678 TL
"""

"""
-> Cheap
CPU MODEL: Intel Core i5 11400F
RAM MODEL: GSKILL 8GB Ripjaws V
VIDEO CARD MODEL: GIGABYTE GeForce RTX 2060
Total value of computer: 11354 TL
"""