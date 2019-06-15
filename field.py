from stamp import Stamp

class Field:
    """
    フィールドの情報を扱うクラス。

    Attributes
    ----------
    target_field : array-like
        お手本のフィールドを格納する配列。
    field_x_size : int
        お手本のフィールドのx軸方向サイズ。
    field_y_size : int
        お手本のフィールドのy軸方向サイズ。
    my_field : array-like
        スタンプを押す用のフィールドを格納する配列。
    """

    #  クラス変数
    target_field = []
    field_x_size = 0
    field_y_size = 0

    def __init__(self):
        """
        コンストラクタ。
        """

        # リスト内包表記を用いて、2次元配列を作る　※2次元配列の各要素を異なるID（識別子）で作成可能
        self.my_field = [[0 for j in range(Field.field_x_size)] for i in range(Field.field_y_size)]

    def press_stamp(self, Stamp_object, parallel_translation_x, parallel_translation_y):
        """
        my_fieldにスタンプを押す。

　　　　Parameters
    　　----------
    　　Stamp_object : Stamp
            Stampクラスのオブジェクト。
        parallel_translation_x : int
            x軸方向に平行移動するx座標。
        parallel_translation_y : int
            y軸方向に平行移動するy座標。
        """

        #  スタンプの黒いセルの座標リストを格納
        press_black_cell_coordinate_list = Stamp_object.get_black_cell_coordinate()

        #  黒いセルの座標分、繰り返し処理
        for press_tuple in press_black_cell_coordinate_list:
            candidate_press_x = press_tuple[1] + parallel_translation_x
            candidate_press_y = press_tuple[0] + parallel_translation_y
            #  スタンプを押す候補の座標が「0」の場合、「1」を代入
            if self.my_field[candidate_press_y][candidate_press_x] == 0:
                self.my_field[candidate_press_y][candidate_press_x] = 1
            #  スタンプを押す候補の座標が「1」の場合、「0」に代入
            elif self.my_field[candidate_press_y][candidate_press_x] == 1:
                self.my_field[candidate_press_y][candidate_press_x] = 0
            else:
                print("pass")

        print(self.my_field)

    @classmethod
    def set_target_field(cls, target_field_information):
        """
        クラス変数（target_field、field_x_size、field_y_size）をセットする

　　　　Parameters
    　　----------
    　　target_field_information : str
            Fieldの定義。
        """

        #  フィールドのx軸方向サイズ、y軸方向サイズをセットする
        field_x_size_str, field_y_size_str, target_field_str = target_field_information.split(";")
        cls.field_y_size = int(field_y_size_str)
        cls.field_x_size = int(field_x_size_str)

        # リスト内包表記を使って2次元配列を作る　※二次元配列の各要素を異なるIDで作成可能
        cls.target_field = [[0 for j in range(cls.field_x_size)] for i in range(cls.field_y_size)]
        current_position = 0
        for y in range(cls.field_y_size):
            for x in range(cls.field_x_size):
                cls.target_field[y][x] = int(target_field_str[current_position])
                current_position += 1

    def num_of_matches_with_target_field(self):
        """
        target_fieldとmy_fieldとの一致数を返す。

        Returns
        ----------
        match_count : int
            target_fieldとmy_fieldとの一致数。
        """

        match_count = 0
        for i in range(Field.field_y_size):
            if Field.target_field[i] == self.my_field[i]:
                match_count += Field.field_x_size
                continue
            else:
                for j in range(Field.field_x_size):
                    if Field.target_field[i][j] == self.my_field[i][j]:
                        match_count += 1
        return match_count

if __name__ == "__main__":
    # case 0
    Field.set_target_field("7;6;100000001000000010000000100000001000000010")
    temp_field = Field()
    print(temp_field.num_of_matches_with_target_field())
    temp_stamp = Stamp(0, "4;3;000001100001")
    temp_field.press_stamp(temp_stamp, 1, 2)