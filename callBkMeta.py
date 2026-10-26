from abc import ABC

from callBack import dbDelete, dbInsert, dbBackup, dbDrop, CallBackCahin, CallBack
from callBkDef import E_CALLBK_TYPE


class IMeta(ABC):

    pass


class abMeta(IMeta, ABC):

    tbs = {}

    pass


class CallbackMetaTB(abMeta):

    tbs = {
        E_CALLBK_TYPE.INSERT : CallBack(dbInsert, tb_nm ="tb1"),
        E_CALLBK_TYPE.DELETE : CallBack(dbDelete, tb_nm ="tb2"),
        E_CALLBK_TYPE.BACKUP : CallBack(dbBackup, tb_nm ="tb3"),
        E_CALLBK_TYPE.DROP : CallBack(dbDrop, tb_nm ="tb4"),
    }

    @staticmethod
    def create():
        cb = CallBackCahin()

        for k , v in CallbackMetaTB.tbs.items():
            cb.AppendCallBack(v)

        return cb

        # cb.AppendCallBack(CallbackMetaTB.tbs.get(E_CALLBK_TYPE.INSERT))
        # cb.AppendCallBack(CallbackMetaTB.tbs.get(E_CALLBK_TYPE.DELETE))
        # cb.AppendCallBack(CallbackMetaTB.tbs.get(E_CALLBK_TYPE.BACKUP))
        # cb.AppendCallBack(CallbackMetaTB.tbs.get(E_CALLBK_TYPE.DROP))


