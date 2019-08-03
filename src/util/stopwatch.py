import time


class StopWatch:
    """
    処理時間を計算するクラス。

    Attributes
    ----------
    start_time : int
    処理時間を格納する変数。
    """

    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        current_time = time.time()
        return current_time - self.start_time

if __name__=="__main__":
    sw = StopWatch()
    sw.start()
    assert sw.get_elapsed_time() < 3, "error!"
    time.sleep(3)
    assert sw.get_elapsed_time() > 3, "error!"
    print(sw.get_elapsed_time())