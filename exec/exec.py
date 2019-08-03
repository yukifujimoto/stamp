import sys
sys.path.append('../')
from src.model.instance import Instance
from src.util.io import IO
from src.algorithm.random_solver import RandomSolver

# 問題の読み取り
io = IO()
io.input_problem()
instance = Instance()
instance.set_stamp_object(io.stamp_object_list)

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