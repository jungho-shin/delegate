from abc import ABC
from typing import Any

from Delegate import IDelegate, abDelegate, Func


class ICallBack(ABC):

    def Invoke(self, *args, **kwargs):...


class abCallBack(ICallBack, ABC):

    def __init__(self, delegate: IDelegate, *args, **kwargs):
        self._delegate = delegate
        self._args = args
        self._kwargs = kwargs

    def Invoke(self, *args, **kwargs) -> Any:
        args = self._args if not args else args
        kwargs = self._kwargs if not kwargs else kwargs
        return self._delegate.Invoke(*args, **kwargs)


class abCallBackChain(ICallBack, ABC):

    def __init__(self):
        self._container = []

    def AppendCallBack(self, callback):
        self._container.append(callback)
        return self

    def Invoke(self, *args, **kwargs):
        for callbk in self._container:
            callbk.Invoke(*args, **kwargs)


class CallBack(abCallBack):
    def __init__(self, delegate, *args, **kwargs):
        super().__init__(delegate, *args, **kwargs)


class CallBackCahin(abCallBackChain):

    def __init__(self):
        super().__init__()


def dbDelete( tb_nm ):

    print(f"dbDelete : {tb_nm}")
    pass

def dbInsert( tb_nm ):

    print(f"dbInsert : {tb_nm}")
    pass

def dbBackup( tb_nm ):

    print(f"dbBackup : {tb_nm}")
    pass

def dbDrop( tb_nm ):

    print(f"dbDrop : {tb_nm}")
    pass

def dbTest():

    print(f"dbTest")
    pass

def main():


    tb1 = CallBack(Func(dbDelete), tb_nm ="tb1" )
    tb2 = CallBack(Func(dbInsert), tb_nm ="tb2" )
    tb3 = CallBack(Func(dbBackup), tb_nm ="tb3" )
    tb4 = CallBack(Func(dbDrop), tb_nm ="tb4" )
    tb5 = CallBack(Func(dbDelete))

    # tb1.Invoke()
    # tb2.Invoke()
    # tb3.Invoke()
    # tb4.Invoke()
    # tb5.Invoke(tb_nm ="tb5")

    ################################################

    # cbc = CallBackCahin()
    #
    # cbc.AppendCallBack(tb1)
    # cbc.AppendCallBack(tb2)
    # cbc.AppendCallBack(tb3)
    # cbc.AppendCallBack(tb4)
    # # cbc.AppendCallBack(tb5)
    #
    # cbc.Invoke()


    #############################

    from callBkMeta import CallbackMetaTB
    # cb = CallbackMetaTB.create()
    # cb.Invoke()

    #############################

    # cb_1_depth_chain = CallBackCahin()
    #
    # cb_2_depth_chain_1 = CallbackMetaTB.create()
    # cb_2_depth_chain_2 = CallbackMetaTB.create()
    # cb_1_depth_chain.AppendCallBack(cb_2_depth_chain_1)
    # cb_1_depth_chain.AppendCallBack(cb_2_depth_chain_2)
    # cb_1_depth_chain.Invoke()

    #############################

    cb_1_depth_chain = CallBackCahin()
    cb_2_depth_chain = CallbackMetaTB.create()
    cb_3_depth_chain = CallbackMetaTB.create()

    cb_1_depth_chain.AppendCallBack(cb_2_depth_chain)
    cb_2_depth_chain.AppendCallBack(cb_3_depth_chain)
    cb_1_depth_chain.Invoke()

    pass


if __name__ == '__main__':
    main()
