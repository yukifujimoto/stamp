class Stamp :

    #  コンストラクタ
    def __init__(self, idx, input_str) :
        self.idx = idx
        input_stamp_information = input_str.split(';')
        self.stamp_x_size = int(input_stamp_information[0])
        self.stamp_y_size = int(input_stamp_information[1])
        self.definition_of_stamp_picture = input_stamp_information[2]
        self.black_cell_coordinate_list = []

    #  黒いセルの座標を取得
    def get_black_cell_coordinate(self) :

        # 二回目以降に呼び出された場合は再利用
        if self.black_cell_coordinate_list != []:
            return self.black_cell_coordinate_list
        current_position = 0
        for x in range(self.stamp_x_size):
            for y in range(self.stamp_y_size):
                if self.definition_of_stamp_picture[current_position] == '1':
                    self.black_cell_coordinate_list.append((x, y))
                current_position += 1
        print(self.black_cell_coordinate_list)

if __name__ == "__main__" :
    temp_stamp = Stamp(0, "4;4;1000010000100001")
    temp_stamp.get_black_cell_coordinate()

