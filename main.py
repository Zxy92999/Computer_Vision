# This is a sample Python script.
import QuickSort
import RandomNums
import MultiplicationTable99
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    int_list = RandomNums.random_int([20, 60], 5)
    float_list = RandomNums.random_float([20.1, 60], 5)
    int_list_sort = QuickSort.quick_sort(int_list)
    float_list_sort = QuickSort.quick_sort(float_list)

    # 上面排序后是升序，如果想降序排列，只需加下列命令
    # int_list_sort = int_list_sort[::-1]

    print('整数列表排序前：', int_list)
    print('整数列表排序后：', int_list_sort)
    print('小数列表排序前：', float_list)
    print('小数列表排序后：', float_list_sort)

    # 99乘法表打印
    s = MultiplicationTable99.multiplication_table()
    print(s)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
