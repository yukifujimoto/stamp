from src.model.field import Field
from src.model.field import Stamp
import sys


class IO:
    """
    お手本、スタンプの定義をインプットし、
    solverクラスで処理できるデータ形式にアウトプットするクラス。

    Attributes
    ----------
    stamp_object_list : list of Stamp
        Stampオブジェクトを格納するリスト。
    """

    stamp_object_list = []

    @classmethod
    def input_problem(cls):
        """
        お手本、スタンプの定義をインプットし、Field、Stampクラスに対して、情報を格納する
        """

        #  Fieldクラスのクラス変数にお手本の定義を格納
        Field.set_target_field(input())

        #  スタンプの定義個数分、オブジェクトを生成しリストに追加する。
        for i, stamp_information in enumerate(sys.stdin):
            stamp_object = Stamp(i, stamp_information.rstrip('\r\n'))
            cls.stamp_object_list.append(stamp_object)


if __name__ == "__main__":
    temp_IO = IO()
    temp_IO.input_problem()

    for i in range(len(IO.stamp_object_list)):
        print(IO.stamp_object_list[i].definition_of_stamp_picture)