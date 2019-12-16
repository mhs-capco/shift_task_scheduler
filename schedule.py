#!/usr/bin/env python3
import itertools
"""
"""

def welcome():
    return "Welcome to the scheduler"

def workday_map(sched):
    daymap = []
    for ons, offs in sched:
        daymap.extend(itertools.repeat(True, ons))
        daymap.extend(itertools.repeat(False, offs))
    return daymap

def is_workday(sched, days):
    daymap = workday_map(sched)
    return daymap[days % len(daymap)]

def offdays(sched):
    od = 0
    for ondays, offdays in sched:
        od += offdays
    return od

def workdays(sched):
    wd = 0
    for ondays, offdays in sched:
        wd += ondays
    return wd

def task_on_workday(sched, tasks, days):
    if days < len(tasks):
        return tasks[days]
    else:
        return tasks[days % len(tasks)]

if __name__ == "__main__":
    print(welcome())
