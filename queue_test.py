import queue_impl

def test_queue():
    q = queue_impl.Queue()
    assert q.is_empty()

    q.enqueue(10)
    assert not q.is_empty()
    assert q.dequeue() == 10
    assert q.is_empty()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert not q.is_empty()
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty()