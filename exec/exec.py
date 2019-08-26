import sys
sys.path.append("../")
from src.model.instance import Instance
from src.model.field import Field
from src.util.io import IO
from src.algorithm.random_solver import RandomSolver
from src.algorithm.combined_stamp_maker import CombinedStampMaker

# 問題の読み取り
io = IO()
io.input_problem()
instance = Instance()
instance.set_origin_stamp_object(io.stamp_object_list)

# できるだけ面積の小さいcombined stampの作成
field_x_size, field_y_size = Field.get_field_size()
combined_stamp_maker = CombinedStampMaker(field_x_size, field_y_size)
instance = combined_stamp_maker.make_combined_stamp_instance(instance)

# ソルバーの生成 & 解の計算
solver = RandomSolver() # ここを切り替えることによって実行するアルゴリズムを変更できる
solution = solver.calc_solution(instance)

# 解の出力
io.output_solution(solution)

if __name__ == "__main__":
    '''
    # 問題の読み取り
    io = IO()
    io.input_problem()
    instance = Instance()
    instance.set_stamp_object(io.stamp_object_list)

    # ソルバーの生成 & 解の計算
    solver = RandomSolver()  # ここを切り替えることによって実行するアルゴリズムを変更できる
    solution = solver.calc_soltion(instance)

    # 解の出力
    io.output_solution(solution)
    '''