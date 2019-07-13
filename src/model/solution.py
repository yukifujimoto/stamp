from src.model.field import Field
from src.model.stamp import Stamp
from src.model.instance import Instance
from src.util.io import IO


class Solution:
    """
    解（スタンプをどこに押すか）を保持するクラス

    Attributes
    ----------
    """

    def __init__(self):
        """
        コンストラクタ。
        """

        self.stamp_answer_list = []

    def add_stamp_answer(self, id, x, y):
        """
        stamp_answer_listにsスタンプを押す座標情報を追加する。
        Parameters
    　　----------
    　　stamp_object : Stamp
            Stampクラスのオブジェクト。
        """

        self.stamp_answer_list.append(tuple(id, x, y))

    def get_stamp_answer_list(self):
        """
        stamp_answer_listに解スタンプ位置情報を追加する。
        Parameters
    　　----------
    　　stamp_object : Stamp
            Stampクラスのオブジェクト。
        """

        return self.stamp_answer_list