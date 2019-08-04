from src.model.field import Field
from src.model.field import Stamp
import sys


class IO:
    """
    問題の情報（お手本、スタンプの定義）をインプット、
    問題の解（スタンプを押す座標リスト）をアプトプットするクラス。

    Attributes
    ----------
    stamp_object_list : list of Stamp
        Stampクラスのオブジェクトを格納するリスト。
    """

    stamp_object_list = []

    @classmethod
    def input_problem(cls):
        """
        問題の情報（お手本、スタンプの定義）をField、Stampクラスにインプットする。

        """

        #  Fieldクラスのクラス変数にお手本の定義を格納
        Field.set_target_field(input())

        #  スタンプの定義個数分、Stampクラスのオブジェクトを生成しリストに追加
        for i, stamp_information in enumerate(sys.stdin):
            stamp_object = Stamp(i, stamp_information.rstrip('\r\n'))
            cls.stamp_object_list.append(stamp_object)

    # Solutionクラスのオブジェクトを受け取り、標準出力に表示
    @staticmethod
    def output_solution(solution):
        """
        解の情報を受け取り標準出力に出力する。

        """

        answer_list = []
        for pressing_info in solution.get_stamp_answer_list():
            combined_stamp = pressing_info[0]
            slide_x        = pressing_info[1]
            slide_y        = pressing_info[2]

            # スタンプを構成するorigin stampを平行移動したのち answer_list に追加
            for origin_stamp in combined_stamp.get_origin_stamp_list():
                answer_list.append((origin_stamp[0], origin_stamp[1]+slide_x, origin_stamp[2]+slide_y))

        # TODO: 重複したスタンプを間引く処理を実装
        print(len(answer_list))
        for triple in (answer_list):
            print(str(triple[0])+";"+str(triple[1])+","+str(triple[2]))

if __name__ == "__main__":
    temp_IO = IO()
    temp_IO.input_problem()

    for i in range(len(IO.stamp_object_list)):
        print(IO.stamp_object_list[i].definition_of_stamp_picture)