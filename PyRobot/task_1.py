#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyrob.api import *

@task
def example1():
    for i in range(9):
        move_right()
        fill_cell()
        move_down()

if __name__ == '__main__':
    run_tasks()
