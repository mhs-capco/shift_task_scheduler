import pytest

import schedule


@pytest.fixture
def standard_workweek():
    return [(5,2)]

@pytest.fixture
def shifts3on2off4on1off():
    return [(3,2), (4,1)]

@pytest.fixture
def colors():
    return ['Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            ]

def test_offdays():
    given = [(5,2)]
    rcvd = schedule.offdays(given)
    assert rcvd == 2
    given = [(3,2), (4,1)]
    rcvd = schedule.offdays(given)
    assert rcvd == 3

def test_workdays():
    given = [(5,2)]
    rcvd = schedule.workdays(given)
    assert rcvd == 5
    given = [(3,2), (4,1)]
    rcvd = schedule.workdays(given)
    assert rcvd == 7

def test_intial_problem(standard_workweek, colors):
    rcvd = schedule.task_on_workday(standard_workweek, colors, 1)
    assert rcvd == colors[1]
    rcvd = schedule.task_on_workday(standard_workweek, colors, 6)
    assert rcvd == colors[6]
    rcvd = schedule.task_on_workday(standard_workweek, colors, 7)
    assert rcvd == colors[0]

def test_workday_map(standard_workweek, shifts3on2off4on1off):
    assert schedule.workday_map(standard_workweek) == [
            True,
            True,
            True,
            True,
            True,
            False,
            False,
            ]
    assert schedule.workday_map(shifts3on2off4on1off) == [
            True,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            True,
            False,
            ]

def test_is_workday(standard_workweek, shifts3on2off4on1off):
    assert schedule.is_workday(standard_workweek, 0) == True
    assert schedule.is_workday(standard_workweek, 5) == False
    assert schedule.is_workday(standard_workweek, 6) == False

def test_welcome_msg():
    assert schedule.welcome() == "Welcome to the scheduler"
