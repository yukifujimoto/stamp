import random
from src.algorithm.solver import Solver
from src.model.field import Field
from src.util.stopwatch import StopWatch
from src.model.solution import Solution


class RandomSolver(Solver):
    """
    スタンプを押す座標を計算するクラス。
    ※座標の計算の仕方はランダム

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

        #  最適解のSolutionオブジェクトを格納する変数
        current_best_solution = None

        #  targetフィールドとmyfieldフィールドの最大一致数を格納する変数
        best_value = 0

        #  「make_candidate_solution()」の結果を格納する変数
        temp_field = Field()
        temp_solution = Solution()

        #  9.5秒以内で最適解を計算する
        temp_sw = StopWatch()
        temp_sw.start()

        while temp_sw.get_elapsed_time() < 9.5:
            temp_solution, temp_field = RandomSolver.make_candidate_solution(instance)
            if temp_field.num_of_matches_with_target_field() > best_value:
                current_best_solution = temp_solution
                best_value = temp_field.num_of_matches_with_target_field()
        return current_best_solution

    @staticmethod
    def make_candidate_solution(instance):
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

        #  スタンプを100回押した結果のSolution、Fieldクラスのオブジェクトを生成する
        for j in range(100):
            parallel_translation_x = int(random.uniform(0, Field.field_x_size))
            parallel_translation_y = int(random.uniform(0, Field.field_y_size))
            stamp_object_count = int(random.uniform(0, len(instance.stamp_object_list)-1))
            temp_solution.add_stamp_answer(instance.stamp_object_list[stamp_object_count].idx,
                                           parallel_translation_x,
                                           parallel_translation_y)
            temp_field.press_stamp(instance.stamp_object_list[stamp_object_count],
                                   parallel_translation_x,
                                   parallel_translation_y)
        return temp_solution, temp_field
