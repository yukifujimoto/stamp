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
        解を表す3-tupleのリスト。
        3-tupeのレイアウトは (Stampオブジェクト, x軸方向への平行移動距離, y軸方向への平行移動距離)

    """

    def __init__(self):
        """
        コンストラクタ。

        """

        self.stamp_answer_list = []

    def add_stamp_answer(self, stamp_object, x, y):
        """
        stamp_answer_listに解（スタンプを押す座標）を追加する。

        Parameters
    　　----------
    　　stamp_object : Stamp
            スタンプのオブジェクト。
        x : int
            スタンプをx座標方向に平行移動させる距離。
        y : int
            スタンプをy座標方向に平行移動させる距離。

        """

        self.stamp_answer_list.append((stamp_object, x, y))

    def get_stamp_answer_list(self):
        """
        stamp_answer_listをゲットする。

        Returns
        ----------
        stamp_answer_list : array-like
        問題の解（スタンプを押す座標）のリスト。
        """

        return self.stamp_answer_list