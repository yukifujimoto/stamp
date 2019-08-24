class Stamp:
    """
    スタンプの情報を扱うクラス。

    Attributes
    ----------
    indices : array-like
        スタンプを構成するオリジナルスタンプの情報を保持する3-tupeの配列。
        3-tupleのレイアウトは (index, x軸方向への平行移動距離, y軸方向の平行移動距離)。
    stamp_x_size : int
        スタンプのx軸方向サイズ。
    stamp_y_size : int
        スタンプのy軸方向サイズ。
    definition_of_stamp_picture : str
        スタンプの絵の定義。
    black_cell_coordinate_list : array-like
        スタンプの黒いセルの座標を格納する配列
    """

    def __init__(self, idx=-1, input_str=""):
        """
        引数ありのコンストラクタ。

        Parameters
    　　----------
    　　idx : int
            スタンプのインデックス。
        input_str : str
            スタンプの定義（x軸方向サイズ；y 軸方向サイズ；絵の定義）。
        """

        self.origin_stamp_list = [(idx, 0, 0)]
        input_stamp_information = input_str.split(';')
        self.stamp_x_size = int(input_stamp_information[0])
        self.stamp_y_size = int(input_stamp_information[1])
        definition_of_stamp_picture = input_stamp_information[2]

        # black_sell_coordinate_list の計算
        current_position = 0
        self.black_cell_coordinate_list = []
        for y in range(self.stamp_y_size):
            for x in range(self.stamp_x_size):
                if definition_of_stamp_picture[current_position] == '1':
                    self.black_cell_coordinate_list.append((y, x))
                current_position += 1

    def get_black_cell_coordinate(self):
        """
        スタンプの黒いセルの座標をタプルのリストで取得する。

        Returns
    　　----------
    　　black_cell_coordinate_list : list of tuple
            黒いセルの座標をタプルで格納したリスト。
        """
        return self.black_cell_coordinate_list

    def get_origin_stamp_list(self):
        """
        自身を構成するoriginスタンプの情報を保持するリストを返す。

        Returns
        ----------
        origin_stamp_list : list of tuple
            自身を構成するoriginスタンプの情報を保持する3-tupleのリスト。
            3-tupleのレイアウトは (index, x軸方向への平行移動距離, y軸方向への平行移動距離)。
        """
        return self.origin_stamp_list

if __name__ == "__main__":
    temp_stamp = Stamp(0, "4;5;10000100001000011111")
    print(temp_stamp.get_black_cell_coordinate())


