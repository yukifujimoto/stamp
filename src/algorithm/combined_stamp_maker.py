import sys
import copy
sys.path.append("../../")
from src.model.stamp import Stamp
from enum import Enum

class StampShape(Enum):
    """
    該当スタンプの種類を表す列挙型。
    """

    RECTANGLE_SINGLE_CELL = 0  # 面積が1のスタンプ
    RECTANGLE_WIDTH_1 = 1       # 幅が1の長方形スタンプ
    RECTANGLE_HEIGHT_1 = 2     # 高さが1の長方形スタンプ
    RECTANGLE_OTHER = 3        # その他の長方形スタンプ
    NON_RECTANGLE = 4          # 長方形ではないスタンプ

# TODO:
# このクラス中ではよく考えずdeepcopyしまくっている.
# パフォーマンスに影響するため、非破壊的メソッド中ではdeepcopyしないなどのリファクタを検討すべき。
class CombinedStampMaker():
    """
    Combined Stamp を作成するクラス。
    与えられたインスタンス中のoriginal stampを使ってできるだけ面積の小さいCombined Stampを作成する。
    """

    def __init__(self, field_size_x, field_size_y):
        self.field_size_x = field_size_x
        self.field_size_y = field_size_y


    def make_combined_stamp_instance(self, instance):
        """
        与えられたインスタンス中のスタンプを用いて、できるだけ黒いセルの少ないスタンプを構成する。

        Parameters
        ----------
        instance : Instance
        　combined stamp object list が空のInstanceオブジェクト

        Returns
        ----------
        new_instance : Instance
        　combined stamp object listにスタンプを詰め込んだInstanceオブジェクト
        
        """

        new_instance = copy.deepcopy(instance)
        new_instance.combined_stamp_object_list = copy.deepcopy(new_instance.origin_stamp_object_list)
        
        min_stamp_area = 64 * 64 
        min_stamp = None
        for stamp in new_instance.get_origin_stamp_object_list():
            if not CombinedStampMaker.__get_stamp_shape(stamp) == StampShape.NON_RECTANGLE:
                # 長方形のスタンプが存在する場合、面積1のセルを作成する
                new_instance.set_combined_stamp_object_list([self.__make_singlecell_by_rectangle(stamp)])
                return new_instance
            else:
                # そうでない場合、面積のできるだけ小さなスタンプを求める
                x_length, y_length = CombinedStampMaker.__get_stamp_width_and_length(stamp)
                if x_length * y_length < min_stamp_area:
                    min_stamp = copy.deepcopy(stamp)
        new_instance.set_combined_stamp_object_list([min_stamp])
        return new_instance

    def __make_singlecell_by_rectangle(self, rectangle_stamp):
        """
        長方形スタンプを組み合わせて大きさが1のスタンプを構成する。
        
        Parameters
        ----------
        rectangle_stamp : Stamp
        　長方形判定済のStampオブジェクト

        Returns
        ----------
        combined_stamp : Stamp
　　　　 　大きさが1のcombinedスタンプ
        """

        combined_stamp = copy.deepcopy(rectangle_stamp)

        black_cell_coordinate = rectangle_stamp.get_black_cell_coordinate()
        x_length, y_length = CombinedStampMaker.__get_stamp_width_and_length(rectangle_stamp)

        # Phase 1. 高さを1にする
        temp_stamp = copy.deepcopy(combined_stamp)
        if y_length != 1:
            for i in range(int(self.field_size_y / y_length) + 1):
                # スタンプを一つ下ずらして押す -> y_length-1だけ下にずらして押す
                combined_stamp = CombinedStampMaker.__combine_two_stamp(combined_stamp, temp_stamp, 0, 1 + i*y_length)
                combined_stamp = CombinedStampMaker.__combine_two_stamp(combined_stamp, temp_stamp, 0, y_length + i*y_length)
        
        # Phase 2. 幅を1にする
        temp_stamp = copy.deepcopy(combined_stamp)
        if x_length != 1:
            for i in range(int(self.field_size_x / x_length) + 1):
                # スタンプを右に一つずらして押す -> x_length-1ｄだけ右にずらして押す
                combined_stamp = CombinedStampMaker.__combine_two_stamp(combined_stamp, temp_stamp, 1 + i*x_length , 0)
                combined_stamp = CombinedStampMaker.__combine_two_stamp(combined_stamp, temp_stamp, x_length + i*x_length, 0)

        # Phase 3. 余分な黒いセルを削除する
        black_cell_coordinate = copy.deepcopy(combined_stamp.get_black_cell_coordinate())
        for (y, x) in combined_stamp.get_black_cell_coordinate():
            if x < 0 or x >= combined_stamp.stamp_x_size or y < 0 or y >= combined_stamp.stamp_y_size:
               black_cell_coordinate.remove((y,x))
        combined_stamp.set_black_cell_coordinate(black_cell_coordinate)

        return combined_stamp

    
    @staticmethod
    def __combine_two_stamp(first_stamp, second_stamp, slide_x, slide_y):
        """
        2つのスタンプを組み合わせて新しいスタンプを作成する。
        具体的には、first_stampと「second_stampをx方向にslide_x, y方向にslide_y平行移動したスタンプ」を合成する。

        Parameters
        ----------
        first_stamp, second_stamp : Stamp, Stamp
        　合成対象のStampオブジェクト
        slide_x, slide_y : int, int
        　second_stampを平行移動させる距離

        Returns
        ----------
        combined_stamp : Stamp
　　　　 　first_stamp, second_stampを組み合わせたスタンプ
        """
        
        combined_stamp = Stamp()

        combined_stamp.origin_stamp_list = copy.deepcopy(first_stamp.origin_stamp_list)
        # second_stampのorigin_stampはx方向, y方向に平行移動してから追加
        for stamp in second_stamp.origin_stamp_list:
            combined_stamp.origin_stamp_list.append((stamp[0], stamp[1] + slide_x, stamp[2] + slide_y))
        
        # スタンプのサイズ（x方向, y方向)はfrist_stampから引き継ぐ
        combined_stamp.stamp_x_size = first_stamp.stamp_x_size
        combined_stamp.stamp_y_size = first_stamp.stamp_y_size

        # 黒いセルの位置の計算
        first_stamp_black_cell_coordinate = copy.deepcopy(first_stamp.get_black_cell_coordinate())
        second_stamp_slided_black_cell_coordinate = []
        for black_coord in second_stamp.get_black_cell_coordinate():
            second_stamp_slided_black_cell_coordinate.append((black_coord[0] + slide_y, black_coord[1] + slide_x))
        combined_black_cell_coordinate = first_stamp_black_cell_coordinate
        for y_x in second_stamp_slided_black_cell_coordinate:
            if y_x in combined_black_cell_coordinate:
                # 黒いセルが重複している場合は反転させる（= black_cell_coordinateから削除する）
                combined_black_cell_coordinate.remove(y_x)
            else:
                combined_black_cell_coordinate.append(y_x)
        combined_stamp.set_black_cell_coordinate(combined_black_cell_coordinate)

        return combined_stamp
    

    @staticmethod
    def __get_stamp_shape(stamp_object):
        """
        与えられたスタンプが長方形か判定する。
        同時に、スタンプの黒いセルの幅と高さを返す。

        Parameters
        ----------
        stamp_object : Stamp
        　判定する対象のStampオブジェクト

        Returns
        ----------
        　スタンプの形を表すStampShapeオブジェクト
        """

        # 黒いセルの面積が 縦×横 と一致していれば長方形と判定
        black_cell_coordinate = stamp_object.get_black_cell_coordinate()
        x_length, y_length = CombinedStampMaker.__get_stamp_width_and_length(stamp_object)
        if x_length * y_length == len(black_cell_coordinate):
            if x_length == 1 and y_length == 1:
                return StampShape.RECTANGLE_SINGLE_CELL
            elif x_length == 1:
                return StampShape.RECTANGLE_WIDTH_1
            elif y_length == 1:
                return StampShape.RECTANGLE_HEIGHT_1
            else:
                return StampShape.RECTANGLE_OTHER
        else:
            return StampShape.NON_RECTANGLE

    
    @staticmethod
    def __get_stamp_width_and_length(stamp_object):
        """
        スタンプの幅と高さを返す。
        幅は（x座標の最大値-最小値+1）、高さは（y座標の最大値-最小値）によって算出する

        Parameters
        ----------
        stamp_object : Stamp
        　測定対象のStampオブジェクト

        Returns
        (x_length, y_length) : (int, int)
        　スタンプの幅、スタンプの高さを格納したタプル　
        ----------
        """

        black_cell_coordinate = stamp_object.get_black_cell_coordinate()
        x_max = 0
        x_min = stamp_object.stamp_x_size
        y_max = 0
        y_min = stamp_object.stamp_y_size
        for ind_y in range(stamp_object.stamp_y_size):
            for ind_x in range(stamp_object.stamp_x_size):
                if (ind_y, ind_x) in black_cell_coordinate:
                    x_max = max(x_max, ind_x)
                    x_min = min(x_min, ind_x)
                    y_max = max(y_max, ind_y)
                    y_min = min(y_min, ind_y)
        return x_max - x_min + 1, y_max - y_min + 1
    


if __name__ == "__main__":
    """
     1. __get_stamp_width_and_length Test
        __get_stamp_shape Test
    """

    # Case 1-1. 長方形の場合
    # 00111
    # 00111
    # 00111
    # 00000
    stamp1_1 = Stamp(input_str="5;4;00111001110011100000")
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_width_and_length(stamp1_1) == (3,3), "Case 1-1. Fail!"
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_shape(stamp1_1) == StampShape.RECTANGLE_OTHER, "Case 1-1. Fail!"

    # Case 1-2. 長方形でない場合
    # 1000
    # 0100
    # 0010
    # 0001
    # 1111
    stamp1_2 = Stamp(input_str="4;5;10000100001000011111")
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_width_and_length(stamp1_2) == (4,5), "Case 1-2 Fail!"
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_shape(stamp1_2) == StampShape.NON_RECTANGLE, "Case 1-2. Fail!"

    # Case 1-3. 長方形が2つ
    # 1100
    # 1100
    # 0011
    # 0011
    stamp1_3 = Stamp(input_str="4;4;1100110000110011")
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_width_and_length(stamp1_3) == (4,4), "Case 1-3. Fail!"
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_shape(stamp1_3) == StampShape.NON_RECTANGLE, "Case 1-3. Fail!"

    # Case 1-4. 面積が1の長方形
    # 0000
    # 0000
    # 0010
    # 0000
    stamp1_4 = Stamp(input_str="4;4;0000000000100000")
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_width_and_length(stamp1_4) == (1,1), "Case 1-4. Fail!"
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_shape(stamp1_4) == StampShape.RECTANGLE_SINGLE_CELL, "Case 1-4. Fail!"

    # Case1-5 高さが1の長方形
    # 0000
    # 1111
    # 0000
    # 0000
    stamp1_5 = Stamp(input_str="4;4;0000000011110000")
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_width_and_length(stamp1_5) == (4,1), "Case 1-5. Fail!"
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_shape(stamp1_5) == StampShape.RECTANGLE_HEIGHT_1, "Case 1-5. Fail!"

    # Case 1-6 幅が1の長方形
    # 1000
    # 1000
    # 1000
    # 0000
    stamp1_6 = Stamp(input_str="4;4;1000100010000000")
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_width_and_length(stamp1_6) == (1,3), "Case 1-6. Fail!"
    assert CombinedStampMaker._CombinedStampMaker__get_stamp_shape(stamp1_6) == StampShape.RECTANGLE_WIDTH_1, "Case 1-6. Fail!"

    """
    2. __combine_two_stamp Test
    """
    # Case 2-1.
    # first_stamp = 
    # 0000
    # 0000
    # 0011
    # 0011
    # second_stamp = 
    # 0100
    # 0100
    # 0001
    # 0001
    # slide_x = 1, slide_y = 1
    # expected_stamp = 
    # 00000
    # 00100
    # 00010
    # 00111
    # 00001
    first_stamp = Stamp(input_str="4;4;0000000000110011")
    second_stamp = Stamp(input_str="4;4;0100010000010001")
    slide_x = 1
    slide_y = 1
    combined_stamp = CombinedStampMaker._CombinedStampMaker__combine_two_stamp(first_stamp, second_stamp, slide_x, slide_y)
    assert combined_stamp.stamp_x_size == 4, "Case 2-1. Fail! "
    assert combined_stamp.stamp_y_size == 4, "Case 2-1. Fail!"
    assert len(combined_stamp.get_black_cell_coordinate()) == 6, "Case 2-1. Fail!"
    for y_x in combined_stamp.get_black_cell_coordinate():
        assert y_x in [(1,2),(2,3),(3,2),(3,3),(3,4),(4,4)], "Case 2-1. Fail!"
    
    # Case 2-2. 追い出し法のシミュレーション
    #           0 <= x <= 3, 0 <= y <= 3 の範囲で黒いセルが1個になってくれれば成功
    # first_stamp = 
    # 0000
    # 0110
    # 0110
    # 0000
    stamp_1 = Stamp(input_str="4;4;0000011001100000")
    stamp_2 = CombinedStampMaker._CombinedStampMaker__combine_two_stamp(first_stamp=stamp_1, second_stamp=stamp_1, slide_x=1, slide_y=0)
    stamp_3 = CombinedStampMaker._CombinedStampMaker__combine_two_stamp(first_stamp=stamp_2, second_stamp=stamp_1, slide_x=2, slide_y=0)
    stamp_4 = CombinedStampMaker._CombinedStampMaker__combine_two_stamp(first_stamp=stamp_3, second_stamp=stamp_3, slide_x=0, slide_y=1)
    stamp_5 = CombinedStampMaker._CombinedStampMaker__combine_two_stamp(first_stamp=stamp_4, second_stamp=stamp_3, slide_x=0, slide_y=2)
    stamp_6 = CombinedStampMaker._CombinedStampMaker__combine_two_stamp(first_stamp=stamp_5, second_stamp=stamp_3, slide_x=0, slide_y=3)
    count_black_cell = 0
    black_cell_coordinate = stamp_6.get_black_cell_coordinate()
    for y in range(stamp_6.stamp_y_size):
        for x in range(stamp_6.stamp_x_size):
            if (y,x) in black_cell_coordinate:
                count_black_cell += 1
    assert count_black_cell == 1, "Case 2-2. Fail!"

    """
    3. __make_singlecell_by_rectangle Test
    """ 
    # Case 3-1. 通常のスタンプのケース
    # stamp = 
    # 00000
    # 01110
    # 01110
    # 00000
    stamp = Stamp(input_str="5;4;00000011100111000000")
    combined_stamp_maker = CombinedStampMaker(field_size_x=10, field_size_y=20)
    single_cell_stamp = combined_stamp_maker._CombinedStampMaker__make_singlecell_by_rectangle(stamp)
    assert len(single_cell_stamp.get_black_cell_coordinate()) == 1, "Case 3-1. Fail!"

    # Case 3-2. 少し大きなスタンプのケース
    # stamp = 
    # 0000000000000
    # 0111111111100
    # 0111111111100
    # 0111111111100
    # 0111111111100
    # 0111111111100
    stamp = Stamp(input_str="13;6;000000000000001111111111000111111111100011111111110001111111111000111111111100")
    combined_stamp_maker = CombinedStampMaker(field_size_x=30, field_size_y=20)
    single_cell_stamp = combined_stamp_maker._CombinedStampMaker__make_singlecell_by_rectangle(stamp)
    assert len(single_cell_stamp.get_black_cell_coordinate()) == 1, "Case 3-2. Fail!"

    # Case 3-3. 高さが1のスタンプのケース
    # stamp = 
    # 0000000000000
    # 0000000000000
    # 0000000000000
    # 0111111111100
    # 0000000000000
    # 0000000000000
    stamp = Stamp(input_str="13;6;000000000000000000000000000000000000000011111111110000000000000000000000000000")
    combined_stamp_maker = CombinedStampMaker(field_size_x=30, field_size_y=20)
    single_cell_stamp = combined_stamp_maker._CombinedStampMaker__make_singlecell_by_rectangle(stamp)
    assert len(single_cell_stamp.get_black_cell_coordinate()) == 1, "Case 3-3. Fail!"

    # Case 3-4. 幅がのスタンプのケース
    # stamp = 
    # 0000000010000
    # 0000000010000
    # 0000000010000
    # 0000000010000
    # 0000000010000
    # 0000000010000
    stamp = Stamp(input_str="13;6;000000001000000000000100000000000010000000000001000000000000100000000000010000")
    combined_stamp_maker = CombinedStampMaker(field_size_x=30, field_size_y=20)
    single_cell_stamp = combined_stamp_maker._CombinedStampMaker__make_singlecell_by_rectangle(stamp)
    assert len(single_cell_stamp.get_black_cell_coordinate()) == 1, "Case 3-4. Fail!"

    
    