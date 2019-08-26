import copy
from src.model.stamp import Stamp


class Field:
    """
    フィールドの情報を扱うクラス。

    Attributes
    ----------
    target_field : array-like
        お手本のフィールド情報を二次元配列で格納するリスト。
    field_x_size : int
        お手本のフィールドのx軸方向サイズ。
    field_y_size : int
        お手本のフィールドのy軸方向サイズ。
    black_cell_list_of_target_field : array-like
        お手本の黒い箇所の座標を格納するリスト。
    divide_list : array-like
        分割したお手本のフィールド情報（座標）を格納するリスト。
    divide_value_list : array-like
        分割したお手本のフィールド情報（値[0,1]）を格納するリスト。
    divide_total_value_list : array-like
        分割したお手本のフィールドごとの合計した値[0,1]を格納するリスト。
    random_target_field : array-like
        ランダムの対象となる分割フィールドのインデックスを格納するリスト。
    my_field : array-like
        自分のフィールド情報を二次元配列で格納するリスト。
    """

    #  クラス変数
    target_field = []
    field_x_size = 0
    field_y_size = 0
    black_cell_list_of_target_field = []
    divide_list = []
    divide_value_list = []
    divide_total_value_list = []
    random_target_field = []

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

            #  candidate_press_xとcandidate_press_yどちらか、myfield以外の座標を指定した場合、continueする
            if candidate_press_x < 0 or candidate_press_y < 0 or candidate_press_x >= Field.field_x_size or candidate_press_y >= Field.field_y_size:
                continue

            #  スタンプを押す候補の座標が「0」の場合、「1」を代入
            if self.my_field[candidate_press_y][candidate_press_x] == 0:
                self.my_field[candidate_press_y][candidate_press_x] = 1
            #  スタンプを押す候補の座標が「1」の場合、「0」に代入
            elif self.my_field[candidate_press_y][candidate_press_x] == 1:
                self.my_field[candidate_press_y][candidate_press_x] = 0
            else:
                print("pass")

    def press_stamp_using_greedy(self, Stamp_object, parallel_translation_x, parallel_translation_y):
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

        #  貪欲法アルゴリズムに使用するリスト
        press_stamp_coordinate_list = []
        before_match_count = 0
        before_my_field = copy.deepcopy(self.my_field)

        #  スタンプの黒いセルの座標リストを格納
        press_black_cell_coordinate_list = Stamp_object.get_black_cell_coordinate()

        #  黒いセルの座標分、繰り返し処理
        for press_tuple in press_black_cell_coordinate_list:
            candidate_press_x = press_tuple[1] + parallel_translation_x
            candidate_press_y = press_tuple[0] + parallel_translation_y

            #  candidate_press_xとcandidate_press_yどちらか、myfield以外の座標を指定した場合、continueする
            if candidate_press_x < 0 or candidate_press_y < 0 or candidate_press_x >= Field.field_x_size or candidate_press_y >= Field.field_y_size:
                continue

            #  スタンプを押す前のtargetfieldとmyfieldの一致数をカウントする
            if Field.target_field[candidate_press_y][candidate_press_x] == self.my_field[candidate_press_y][candidate_press_x]:
                before_match_count += 1

            #  スタンプを押す候補の座標が「0」の場合、「1」を代入
            if self.my_field[candidate_press_y][candidate_press_x] == 0:
                self.my_field[candidate_press_y][candidate_press_x] = 1
            #  スタンプを押す候補の座標が「1」の場合、「0」に代入
            elif self.my_field[candidate_press_y][candidate_press_x] == 1:
                self.my_field[candidate_press_y][candidate_press_x] = 0
            else:
                print("pass")

            #  スタンプを押した座標をリストに追加する
            press_stamp_coordinate_list.append((candidate_press_y, candidate_press_x))

        #  貪欲法
        if press_stamp_coordinate_list:
            after_match_count = 0
            for press_stamp_coordinate in press_stamp_coordinate_list:
                if Field.target_field[press_stamp_coordinate[0]][press_stamp_coordinate[1]] == self.my_field[press_stamp_coordinate[0]][press_stamp_coordinate[1]]:
                    after_match_count += 1
            if before_match_count < after_match_count:
                return True
            else:
                self.my_field = copy.deepcopy(before_my_field)
                return False
        else:
            return False

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
        target_fieldとmy_fieldとの一致数を計算する。

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

    @classmethod
    def get_black_cell_coordinate_for_target_field(cls):
        """
        お手本の黒いセルの座標をタプルのリストで取得する。

        Returns
    　　----------
    　　black_cell_list_of_target_field : array-like
            お手本の黒い箇所の座標を格納するリスト。
        """

        #  2回目以降に呼び出された場合、黒いセルの座標を計算する処理を省略
        if cls.black_cell_list_of_target_field:
            return cls.black_cell_list_of_target_field
        else:
            for y in range(cls.field_y_size):
                for x in range(cls.field_x_size):
                    if cls.target_field[y][x] == 1:
                        cls.black_cell_list_of_target_field.append((y,x))

        return cls.target_field_black_cell_list

    @classmethod
    def divide_field(cls, division_unit_x_axis, division_unit_y_axis):
        """
        target_fieldを分割する。

        Parameters
    　　----------
    　　division_unit_x_axis : int
            x軸方向の分割単位。
        parallel_translation_x : int
            y軸方向の分割単位。
        """

        #  フィールドの長さより分割数の方が多い場合、後続処理を中断する
        if Field.field_x_size < division_unit_x_axis or Field.field_y_size < division_unit_y_axis:
            return

        #  x軸、y軸の分割開始点を格納するリスト
        division_start_point_x_list = []
        division_start_point_y_list = []

        #  x軸、y軸の分割開始点を計算する（余りあり/なしの場合を考慮する）
        quotient_x = int(Field.field_x_size / division_unit_x_axis)
        remainder_x = Field.field_x_size % division_unit_x_axis
        quotient_y = int(Field.field_y_size / division_unit_y_axis)
        remainder_y = Field.field_y_size % division_unit_y_axis

        if remainder_x > 0:
            for i in range(1, Field.field_x_size):
                if i % quotient_x == 0:
                    division_start_point_x_list.append(i + remainder_x)
        elif remainder_x == 0:
            for i in range(1, Field.field_x_size + 1):
                if i % quotient_x == 0:
                    division_start_point_x_list.append(i)
        if remainder_y > 0:
            for i in range(1, Field.field_y_size):
                if i % quotient_y == 0:
                    division_start_point_y_list.append(i + remainder_y)
        elif remainder_y == 0:
            for i in range(1, Field.field_y_size + 1):
                if i % quotient_y == 0:
                    division_start_point_y_list.append(i)

        #  フィールドを分割する
        prev_start_point_x = 0
        prev_start_point_y = 0
        for start_point_y in division_start_point_y_list:
            for start_point_x in division_start_point_x_list:
                temp_divide_list = []
                temp_divide_value_list = []
                temp_divide_total_value = 0
                for current_point_y in range(prev_start_point_y, start_point_y):
                    for current_point_x in range(prev_start_point_x, start_point_x):
                        temp_divide_list.append((current_point_y, current_point_x))
                        temp_divide_value_list.append(Field.target_field[current_point_y][current_point_x])
                        temp_divide_total_value += Field.target_field[current_point_y][current_point_x]
                cls.divide_list.append(temp_divide_list)
                cls.divide_value_list.append(temp_divide_value_list)
                cls.divide_total_value_list.append(temp_divide_total_value)
                prev_start_point_x = start_point_x
            prev_start_point_x = 0
            prev_start_point_y = start_point_y

        #  ランダムアルゴリズムの対象となるフィールドのインデックスを計算する
        for total_value_idx, total_value in enumerate(cls.divide_total_value_list):
            if total_value == 0:
                continue
            cls.random_target_field.append(total_value_idx)

if __name__ == "__main__":
    # case 0
    Field.set_target_field("19;11;11111000000000010000100000000000010000000000000010000000000000000000001000000000000000000001000000000000111000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000")
    #Field.set_target_field("20;11;0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    temp_field = Field()
    #print(Field.target_field)
    #temp_target_field = np.array(Field.target_field)
    #print(temp_target_field)
    #  divide_target_feildには、target_feildを分割した二次元配列が格納される
    temp_field.divide_field(4, 3)
    #Field.get_black_cell_coordinate_for_target_field() →　結果確認済み
    #temp_stamp = Stamp(0, "4;3;000001100001")　→　結果確認済み
    #temp_field.press_stamp(temp_stamp, 1, 2)　→　結果確認済み