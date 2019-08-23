import copy


class Instance:
    """
    Stampクラスのオブジェクトリストをセット/ゲットするクラス。

    Attributes
    ----------
    origin_stamp_object_list : array-like
        origin stampのオブジェクトを保持するリスト。
    combined_stamp_object_list : array-like
        combined stampのオブジェクトを保持するリスト。
    """

    def __init__(self):
        """
        コンストラクタ。

        """

        self.origin_stamp_object_list = []
        self.combined_stamp_object_list = []

    def set_origin_stamp_object(self, stamp_object):
        """
        引数のStampクラスのオブジェクトをstamp_object_listにセットする。
        Parameters
    　　----------
    　　stamp_object : Stamp
            Stampクラスのオブジェクト。
        """

        self.origin_stamp_object_list.extend(stamp_object)

    # できるだけ面積の小さい combined stamp を構築する
    def make_combined_stamp_list(self):
        # TODO: 実装する。ひとまず、original stamp をそのまま使う。
        self.combined_stamp_object_list = copy.deepcopy(self.origin_stamp_object_list)

    def get_combined_stamp_object_list(self):
        """
        combined_stamp_object_listをゲットする。

        Returns
        ----------
        combined_stamp_object_list : list-array
            Stampクラスのオブジェクトを格納するリスト。
        """

        return self.combined_stamp_object_list


if __name__ == "__main__":
    temp_instance = Instance()
    temp_instance.set_stamp_object("aaaa")
    print(temp_instance.get_combined_stamp_object_list())