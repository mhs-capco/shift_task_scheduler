# shift_task_scheduler
Answers simple questions about when tasks will be accomplished.

## Intro
The original problem comes as an interview/assessment task. It provideds
 * a work schedule: a traditional 5-on, 2-off workweek
 * a fixed, but cyclicaly repeating, list of tasks: a short list of colors to paint items
 * a rate by which tasks are accomplished: 1 color per workday

The intent is to answer the question: X-days after the start of working, which task will be the current task?

Because this is an interview-style task, it makes sense to consider follow up questions.
 * How would we support different shift schedules?
 * How would we reflect a finite list of tasks?
 * How would we handle answering the question "What is the current task?" under both of the following conditions
   * X-work-days after the start of work
   * X-total-days after the start of work

