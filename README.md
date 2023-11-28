# Lab 10 - Data Structures

In this lab, we'll learn how to implement a simple data structure in Python.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab10-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will write the `queue.py` file so that it meets the requirements described in this section.  This file has no basic code to start, and it will be up to you to write all of the code for this lab.

In `queue_impl.py`, write a Python class (`Queue`) that implements the queue data structure, described in the lectures.  Your class must support the following operations:
- `enqueue()`:	Adds an element to the back of the queue
- `front()`:	Returns the front element
- `dequeue()`:	Removes the front element
- `is_empty()`:	Returns `True` if the queue is empty, `False` otherwise
- `__str__()`:	Returns a string representation of the queue

Use the following code to test your queue:

```python
queue = Queue()
print(f'{queue.is_empty() = }')             # True
print(f'empty: {queue}')                    # [ ]
queue.enqueue(10)
print(f'after enqueue(10): {queue}')        # [ 10 ]
print(f'is_empty(): {queue.is_empty()}')    # False
queue.enqueue(1)
print(f'after enqueue(1): {queue}')         # [ 10 1 ]
print(f'dequeue(): {queue.dequeue()}')      # 10
print(f'after dequeue(): {queue}')          # [ 1 ]
queue.enqueue(2)
print(f'after enqueue(2): {queue}')         # [ 1 2 ]
queue.enqueue(3)
print(f'after enqueue(3): {queue}')         # [ 1 2 3 ]
queue.enqueue(4)
print(f'after enqueue(4): {queue}')         # [ 1 2 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 1
print(f'after dequeue(): {queue}')          # [ 2 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 2
print(f'after dequeue(): {queue}')          # [ 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 3
print(f'after dequeue(): {queue}')          # [ 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 4
print(f'after dequeue(): {queue}')          # [ ]
print(f'is_empty(): {queue.is_empty()}')    # True
```

_**Note:** You can use any implementation that you want, but it is recommended that you use the array implementation (lists in Python), as it is the easiest to do._

_**Hint:**  It is not necessary to account for wrapping of the front and back of the queue, as discussed in the lectures.  Simply make your list large enough to account for your test data._

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._


## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 10 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
