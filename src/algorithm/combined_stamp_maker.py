import sys
import copy
sys.path.append("../../")
from src.model.stamp import Stamp

class CombinedStampMaker():
    """
    Combined Stamp を作成するクラス。
    与えられたインスタンス中のoriginal stampを使ってできるだけ面積の小さいCombined Stampを作成する。
    """

    def __init__(self):
        pass

    @staticmethod
    def make_combined_stamp_instance(instance):
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
        # TODO ちゃんと実装する。とりあえずoriginスタンプをそのままcombinedスタンプとして使う
        new_instance = copy.deepcopy(instance)
        new_instance.combined_stamp_object_list = copy.deepcopy(new_instance.origin_stamp_object_list)
        return new_instance
    
    @staticmethod
    def __is_rectangle(stamp_object):
        """
        与えられたスタンプが長方形か判定する。

        Parameters
        ----------
        stamp_object : Stamp
        　判定する対象のStampオブジェクト

        Returns
        ----------
        　長方形の場合True, そうでない場合False
        """
        black_cell_coordinate = stamp_object.get_black_cell_coordinate()

        # 黒のセルのx座標とy座標の最大値/最小値をそれぞれ求める
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
        
        # 黒いセルの面積と、(x座標の最大値-最小値+1)*(y座標の最大値-最小値+1)が等しければ長方形
        return (x_max-x_min+1) * (y_max-y_min+1) == len(black_cell_coordinate)
                    

if __name__ == "__main__":
    # 1. __is_rectangle Test

    # Case 1-1. 長方形の場合
    # 00111
    # 00111
    # 00111
    # 00000
    stamp1_1 = Stamp(input_str="5;4;00111001110011100000")
    assert CombinedStampMaker._CombinedStampMaker__is_rectangle(stamp1_1), "Case 1-1. Fail!"

    # Case 1-2. 長方形でない場合
    # 1000
    # 0100
    # 0010
    # 0001
    # 1111
    stamp1_2 = Stamp(input_str="4;5;10000100001000011111")
    assert (not CombinedStampMaker._CombinedStampMaker__is_rectangle(stamp1_2)), "Case 1-2. Fail!"

    # Case 1-3. コーナーケース（長方形が2つ)
    # 1100
    # 1100
    # 0011
    # 0011
    stamp1_3 = Stamp(input_str="4;4;1100110000110011")
    assert (not CombinedStampMaker._CombinedStampMaker__is_rectangle(stamp1_3)), "Case 1-3. Fail!"


    # Case1-4. コーナーケース（面積が1）
    # 0000
    # 0000
    # 0010
    # 0000
    stamp1_4 = Stamp(input_str="4;4;0000000000100000")
    assert CombinedStampMaker._CombinedStampMaker__is_rectangle(stamp1_4), "Case 1-4. Fail!"
