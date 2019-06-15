class Stamp:
    """
    スタンプの情報を扱うクラス。

    Attributes
    ----------
    idx : int
        スタンプのインデックス。
    stamp_x_size : int
        スタンプのx軸方向サイズ。
    stamp_y_size : int
        スタンプのy軸方向サイズ。
    definition_of_stamp_picture : str
        スタンプの絵の定義。
    black_cell_coordinate_list : array-like
        スタンプの黒いセルの座標を格納する配列
    """

    def __init__(self, idx, input_str):
        """
        コンストラクタ。

        Parameters
    　　----------
    　　idx : int
            スタンプのインデックス。
        input_str : str
            スタンプの定義（x軸方向サイズ；y 軸方向サイズ；絵の定義）。
        """

        self.idx = idx
        input_stamp_information = input_str.split(';')
        self.stamp_x_size = int(input_stamp_information[0])
        self.stamp_y_size = int(input_stamp_information[1])
        self.definition_of_stamp_picture = input_stamp_information[2]
        self.black_cell_coordinate_list = []

    def get_black_cell_coordinate(self):
        """
        スタンプの黒いセルの座標をタプルのリストで取得する。

        Returns
    　　----------
    　　black_cell_coordinate_list : list of tuple
            黒いセルの座標をタプルで格納したリスト。
        """

        #  2回目以降に呼び出された場合、黒いセルの座標を計算する処理を省略
        if self.black_cell_coordinate_list:
            return self.black_cell_coordinate_list
        else:
            current_position = 0
            for y in range(self.stamp_y_size):
                for x in range(self.stamp_x_size):
                    if self.definition_of_stamp_picture[current_position] == '1':
                        self.black_cell_coordinate_list.append((y, x))
                    current_position += 1
        return self.black_cell_coordinate_list

if __name__ == "__main__":
    temp_stamp = Stamp(0, "4;5;10000100001000011111")
    print(temp_stamp.get_black_cell_coordinate())


