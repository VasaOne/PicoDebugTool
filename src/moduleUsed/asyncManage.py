import asyncio
from collections import deque

STATUS_NEW = 'NEW'
STATUS_RUNNING = 'RUNNING'
STATUS_FINISHED = 'FINISHED'
STATUS_ERROR = 'ERROR'

class Task :
    def __ini__(self, coro):
        self.coro = coro
        self.name = coro.__name__
        self.status = STATUS_NEW
        self.return_value = None
        self.error_value = None

    def run(self) :
        try : 
            self.status = STATUS_FINISHED
            next(self.coro)
        except StopIteration as err:
            self.status = STATUS_FINISHED
            self.return_value = err.value
            
        except Exception as err:
            self.status = STATUS_ERROR
            self.error_value = err


    def is_done(self):
        return self.status in {STATUS_FINISHED, STATUS_ERROR}

    def __repr__(self):
        result = ''
        if self.is_done():
            result = " ({!r})".format(self.return_value or self.error_value)

        return "<Task '{}' [{}]{}>".format(self.name, self.status, result)


class Loop:
    def __init__(self):
        self._running = deque()

    def _loop(self):
        task = self._running.popleft()
        task.run()
        if task.is_done():
            print(task)
            return
        self.schedule(task)

    def run_until_empty(self):
        while self._running:
            self._loop()

    def schedule(self, task):
        if not isinstance(task, Task):
            task = Task(task)
        self._running.append(task)
        return task


class Loop:
    # ...
    def run_until_complete(self, task):
        task = self.schedule(task)
        while not task.is_done():
            self._loop()

