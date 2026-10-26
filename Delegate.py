from abc import ABC


class IDelegate(ABC):
    def Invoke(*args, **kwargs):...

    pass



class abDelegate(IDelegate  , ABC):

    def __init__(self, lambda_func ,  *args, **kwargs):
        self._lambda_func = lambda_func
        self._args = args
        self._kwargs = kwargs
        pass

    def Invoke(self, *args, **kwargs):
        return self._lambda_func(
            *(args if args else self._args),
            **(kwargs if kwargs else self._kwargs)
        )




class Func(abDelegate):

    def __init__(self ,  lambda_func,*args, **kwargs):
        super().__init__(lambda_func,*args, **kwargs)
    #

    def Invoke(self, *args, **kwargs):
        # return super().Invoke(
        #     *(args if args else self._args),
        #     **(kwargs if kwargs else self._kwargs)
        # )
        #
        return super().Invoke(
            *args, **kwargs
        )

    pass


def calc(a,b):
    return a+b


def main():

    f = Func(lambda a, b: print(a + b), 10, 10)
    f.Invoke()  # 20


    c = Func(lambda a, b: print(a + b))
    c.Invoke( 10, 10)  # 20

    d = Func(calc)
    r= d.Invoke( 10, 10)  # 20

    print(r)

    pass


if __name__ == '__main__':
    main()



