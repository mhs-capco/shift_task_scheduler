#!/usr/bin/env python3

"""
"""

def welcome():
    return "Welcome to the scheduler"

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
