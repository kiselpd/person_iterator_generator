import core.test as testlib

def main():
    try:
        testlib.test_1()
        print("test_1(итератор по спискам в списке) пройден!")
    except:
        print("test_1(итератор по спискам в списке) не пройден!") 
    
    try:
        testlib.test_2()
        print("test_2(генератор из списков в списке) пройден!")
    except:
        print("test_2(генератор из списков в списке) не пройден!")

    try:
        testlib.test_4()
        print("test_4(генератор из списков неизвестной глубины) пройден!")
    except:
        print("test_4(генератор из списков неизвестной глубины) не пройден!") 

     
if __name__=="__main__":
    main()