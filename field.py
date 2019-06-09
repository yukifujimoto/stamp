class Field :

    #  クラス変数
    target_field = []
    field_x_size = 0
    field_y_size = 0

    #  コンストラクタ
    def __init__(self) :
        self.my_field = [[0] * Field.field_x_size] * Field.field_y_size

    #  スタンプを押す
    def press_stamp(self, black_cell_coordinate_list) :

        #  実際はスタンプの総数からランダムに選択
        get_stamp_number = 0
        get_stamp_x = black_cell_coordinate_list[get_stamp_number][1]
        get_stamp_y = black_cell_coordinate_list[get_stamp_number][2]

        press_x = 0
        press_y = 0

    # target_fieldをセットする
    # この際にフィールドのx方向の長さとy方向の長さもセットされる
    @classmethod
    def set_target_field(cls, target_field_information) :
        field_x_size_str, field_y_size_str, target_field_str = target_field_information.split(";")
        cls.field_x_size = int(field_x_size_str)
        cls.field_y_size = int(field_y_size_str)
        cls.target_field = [[0] * cls.field_x_size] * cls.field_y_size
        current_position = 0
        for x in range(cls.field_x_size):
            for y in range(cls.field_y_size):
                cls.target_field[x][y] = int(target_field_str[current_position])
                current_position += 1

    #  target_fieldとmy_fieldとの一致数を返す
    def num_of_matches_with_target_field(self) :
        match_count = 0
        for i in range(Field.field_y_size) :
            if Field.target_field[i] == self.my_field[i] :
                match_count += Field.field_x_size
                continue
            else :
                for j in range(Field.field_x_size) :
                    if Field.target_field[i][j] == self.my_field[i][j] :
                        match_count
        return match_count

if __name__ == "__main__" :
    # case 0
    Field.set_target_field("4;4;1000010000100001")
    temp_field = Field()
    print(temp_field.num_of_matches_with_target_field()) # => 0