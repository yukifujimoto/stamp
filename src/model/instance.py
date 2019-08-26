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
    
    def get_origin_stamp_object_list(self):
        """
        origin stamp object listをゲットする。

        Returns
        ----------
        combined_stamp_object_list : list-array
            Stampクラスのオブジェクトを格納するリスト。
        """
        return self.origin_stamp_object_list

    def get_combined_stamp_object_list(self):
        """
        combined_stamp_object_listをゲットする。

        Returns
        ----------
        combined_stamp_object_list : list-array
            Stampクラスのオブジェクトを格納するリスト。
        """

        return self.combined_stamp_object_list

    def set_combined_stamp_object_list(self, combined_stamp_object_list):
        """
        combined_stamp_object_listをセットする。

        Parameters
        ----------
        combined_stamp_object_list : list-array
            Stampクラスのオブジェクトを格納するリスト。
        """

        self.combined_stamp_object_list = combined_stamp_object_list