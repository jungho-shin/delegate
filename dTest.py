from IDelegate import Action1, Func1


class THUman:
    def __init__(self , _name , _age):
        self.name=_name
        self.age=_age


class TTest(Action1[THUman]):

    def invork(self, t1: THUman):
        print(t1.name)
        print(str(t1.age))


class MyFunc1(Func1[THUman, str]):
    def invork(self, t1: THUman) -> str:
        print(t1.name)
        print(t1.age)
        return str(t1)


def main():
    my_func = MyFunc1()
    vg="a"
    print(my_func.invork(THUman("aaa",10)  )  )   # "123"
    # print(my_func.invork(123))  # "123"
    #
    #
    tt = TTest()
    tt.invork( THUman("aaa",10) )

## as,mjdhsakjdhasj

    pass

if __name__ == '__main__':
    main()