# столбчатая диаграмма Mathplotlib - мои доходы за 2020
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Program's entry point
    :return: None
    """
    # кортеж с именами месяцев
    months = ('Jan', 'Feb', 'Mar', 'Apr',
              'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Oct', 'Nov', 'Dec')

    y_pos = np.arange(len(months))
    # список с зарплатами
    salary = [117146, 110952, 127341, 99926,
              80462, 81945, 97320, 89147,
              114821, 125572, 98511, 238317]

    plt.bar(y_pos, salary, align='center', alpha=0.5)
    plt.xticks(y_pos, months)
    plt.ylabel('rub.')
    plt.title('My salary in year 2020')
    plt.show()


if __name__ == '__main__':
    main()
