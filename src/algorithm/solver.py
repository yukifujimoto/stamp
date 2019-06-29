from abc import ABCMeta, abstractmethod

class Solver(metaclass=ABCMeta):
    @abstractmethod
    def calc_soltion(instance):
        pass