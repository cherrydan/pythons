#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_readable(seconds):
    """
    Переводит заданное количество секунд
    в ЧП-формат
    """
    s_hours = s_mins = s_sec = ''
    if seconds <= 359999:
        hours = seconds // 3600
        if (hours == 0 or hours <= 9):
            s_hours = '0' + str(hours)
        else:
            s_hours = str(hours)
        mins = (seconds-hours*3600) // 60
        if (mins == 0 or mins <= 9):
            s_mins = '0' + str(mins)
        else:
            s_mins = str(mins)
        sec = seconds % 60
        if (sec == 0 or sec <= 9):
            s_sec = '0' + str(sec)
        else:
            s_sec = str(sec)

        return s_hours + ':' + s_mins + ':' + s_sec
    else:
        return None


sec = int(input('Время в сек: '))
print(make_readable(sec))
