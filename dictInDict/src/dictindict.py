'''
Created on 27 апр. 2018 г.

@author: danny
'''

if __name__ == '__main__':
    #вложенный словарь
    allGuests = {'Alice':{'apples':5, 'pretzels':12},
                 'Bob':{'ham sandwiches':3, 'apples':2,'vodka':1},
                 'Carol':{'cups':3, 'apple pies':1},
                 'Nicky':{'juice':4}}


    def totalBrougt(guests, item):
        numBrought = 0 #счетчик товаров
        for k, v in guests.items():
            numBrought = numBrought + v.get(item,0)
        return numBrought

    print('Number of things being brought: ')
    print(' -Apples         \t' + str(totalBrougt(allGuests, 'apples')))
    print(' -Cups           \t' + str(totalBrougt(allGuests, 'cups')))
    print(' -Cakes          \t' + str(totalBrougt(allGuests, 'cakes')))
    print(' -Ham Sandwiches \t' + str(totalBrougt(allGuests, 'ham sandwiches')))
    print(' -Apple Pies     \t' + str(totalBrougt(allGuests, 'apple pies')))
    print(' -Pretzels       \t' + str(totalBrougt(allGuests, 'pretzels')))
    print(' -Vodka          \t' + str(totalBrougt(allGuests, 'vodka')))
    print(' -Juice          \t' + str(totalBrougt(allGuests, 'juice')))
