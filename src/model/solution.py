from src.model.field import Field
from src.model.stamp import Stamp
from src.model.instance import Instance
from src.util.io import IO


class Solution:
    """
    解の情報を扱うクラス。

    Attributes
    ----------
    stamp_answer_list : array-like
        問題の解（スタンプを押す座標）のリスト。

    """

    def __init__(self):
        """
        コンストラクタ。

        """

        self.stamp_answer_list = []

    def add_stamp_answer(self, idx, x, y):
        """
        stamp_answer_listに解（スタンプを押す座標）を追加する。

        Parameters
    　　----------
    　　idx : int
            スタンプのインデックス。
        x : int
            スタンプを押すx座標。
        y : int
            スタンプを押すy座標。

        """

        self.stamp_answer_list.append((idx, x, y))

    def get_stamp_answer_list(self):
        """
        stamp_answer_listをゲットする。

        Returns
        ----------
        stamp_answer_list : array-like
        問題の解（スタンプを押す座標）のリスト。
        """

        return self.stamp_answer_list