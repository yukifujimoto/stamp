class Instance:
    """
    stampクラスのオブジェクトリストを返すラッパークラス。

    Attributes
    ----------
    stamp_object_list : array-like
    stampオブジェクトを格納するリスト。
    """

    def __init__(self):
        """
        コンストラクタ。
        """

        self.stamp_object_list = []

    def set_stamp_object(self, stamp_object):
        """
        引数のStampオブジェクトをstamp_object_listにセットする。
        Parameters
    　　----------
    　　stamp_object : Stamp
            Stampクラスのオブジェクト。
        """

        self.stamp_object_list.append(stamp_object)

    def get_stamp_object_list(self):
        """
        stamp_object_listを取得する。
        Returns
        ----------
        stamp_object_list : list-array
            stampオブジェクトを格納するリスト。
        """

        return self.stamp_object_list


if __name__ == "__main__":
    temp_instance = Instance()
    temp_instance.set_stamp_object("aaaa")
    print(temp_instance.get_stamp_object_list())