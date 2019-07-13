from abc import ABCMeta, abstractmethod


class Solver(metaclass=ABCMeta):
    """
    スタンプを押す座標を計算するメソッドを定義する抽象クラス。

    Attributes
    ----------
    """

    def __init__(self):
        """
        コンストラクタ。

        """
        pass

    @abstractmethod
    def calc_solution(instance):
        """
        スタンプを押す座標を計算する。

        Parameters
        ----------
        instance : instance
            instanceクラスのオブジェクト。
        """

        pass
