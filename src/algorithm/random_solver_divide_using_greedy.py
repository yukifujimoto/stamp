import random
from src.algorithm.solver import Solver
from src.model.field import Field
from src.util.stopwatch import StopWatch
from src.model.solution import Solution


class RandomSolverDivideUsingGreedy(Solver):
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

        #  フィールドを分割する
        Field.divide_field(20, 20)

        #  ループの回数を求める
        while_loop_count = 0

        while temp_sw.get_elapsed_time() < 9.5:
            while_loop_count += 1
            temp_solution, temp_field = RandomSolverDivideUsingGreedy.make_candidate_solution(instance)
            if temp_field.num_of_matches_with_target_field() > best_value:
                current_best_solution = temp_solution
                best_value = temp_field.num_of_matches_with_target_field()
        print(while_loop_count)
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

            random_target_index = random.choice(Field.random_target_field)
            random_target_coordinate_list = Field.divide_list[random_target_index]
            random_target_coordinate = random.choice(random_target_coordinate_list)

            parallel_translation_x = random_target_coordinate[1]
            parallel_translation_y = random_target_coordinate[0]
            stamp_object_count=int(random.randint(0, len(instance.combined_stamp_object_list) - 1))
            if temp_field.press_stamp_using_greedy(instance.combined_stamp_object_list[stamp_object_count],
                                      parallel_translation_x,
                                      parallel_translation_y):
                temp_solution.add_stamp_answer(instance.combined_stamp_object_list[stamp_object_count],
                                               parallel_translation_x,
                                               parallel_translation_y)
            else:
                continue
        return temp_solution, temp_field



