from core.test import test_1, test_2

def main():
    try:
        test_1()
        print("Тест 1 пройден!")
    except:
        print("Тест 1 не пройден!") 
    
    try:
        test_2()
        print("Тест 2 пройден!")
    except:
        print("Тест 2 не пройден!")

     
if __name__=="__main__":
    main()