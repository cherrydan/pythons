'''
Created on 28 апр. 2018 г.

@author: danny
'''
# -*- coding: utf-8 -*-


#stuff = {'rope':1, 'torch': 6, 'gold coin':42, 'dagger':1, 'arrow':12 }

#функция выводит на экран список инвентаря

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + '\t' + k)
        item_total += v

    print('Total items in inventory: ' + str(item_total))

#displayInventory(stuff)

def addToInventory(inventory, addedItems):
#смотрим каждый элемент в словаре (item)
    for item in addedItems:
        if item in inventory: #если item уже есть в словаре
            inventory[item] += 1 #элементу с ключом item присваиваем значение +1
        else:
            inventory[item] = 1 #если его не было, то значение ключа item будет = 1
    return inventory


inv = {}


dragonLoot = []

try:
    while True:
        name = input('Enter a game inventory name: (blank for exit) ')
        if name != '':
            num = int(input('Enter a number of inventory \"' + name + '\" '))
            inv[name] = num
            loot = input('Enter a inventory name, that looted by dragon: ')
            if loot != '':
                dragonLoot.append(loot)
            else:
                continue
        else:
            print('You entered nothing... Exit')
            break


    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)

except ValueError:
    print('You must enter integers!')




