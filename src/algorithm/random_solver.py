import random
from src.algorithm.solver import Solver
from src.model.field import Field


class RandomSolver(Solver):
    """
    スタンプを押す座標を計算するクラス。

    """

    def calc_solution(self, instance):
        """
        スタンプを押す座標を計算する。

        Parameters
        ----------
        instance : instance
            instanceクラスのオブジェクト。

        Returns
    　　----------
    　　current_best_solution : Solution
            お手本との一致数が一番多いsolutionのオブジェクト。
        """

        current_best_solution = null
        best_value = 0
        temp_solution = Solution()
        temp_field = Field()

        for i in range(1000):
            temp_solution, temp_field = make_candidate_solution()
            if temp_field.num_of_matches_with_target_field() > best_value:
                current_best_solution = temp_solution
                best_value = temp_field.num_of_matches_with_target_field()
        return current_best_solution

    def make_candidate_solution(self):
        """
        最適解候補のSolutionオブジェクトを作成する。

        Returns
        ----------
        temp_solution : Solution
            最適解候補のSolutionオブジェクト
        temp_field : Field
            最適解候補のFieldオブジェクト
        """

        temp_field = Field()
        temp_solution = Solution()
        for j in range(100):
            parallel_translation_x = int(random.uniform(0, Field.field_x_size))
            parallel_translation_y = int(random.uniform(0, Field.field_y_size))
            stamp_object_count = int(random.uniform(0, len(stamp_object_list)))
            temp_solution.add_stamp_answer(instance.stamp_object_list[stamp_object_count].idx,
                                           parallel_translation_x,
                                           parallel_translation_y)
            temp_field.press_stamp(instance.stamp_object_list[stamp_object_count],
                                   parallel_translation_x,
                                   parallel_translation_y)
        return temp_solution, temp_field
