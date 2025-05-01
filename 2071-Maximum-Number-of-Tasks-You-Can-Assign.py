import bisect
import collections

def binsearch(low, high, do_not_search_less_than):
    while high - low > 1:
        mid = (low + high) // 2
        if do_not_search_less_than(mid):
            low = mid
        else:
            high = mid
    return low

class TaskAssigner:
    def __init__(self, tasks, workers, pills, strength):
        self.tasks = sorted(tasks)
        self.workers = sorted(workers)
        self.pills = pills
        self.strength = strength

    def can_assign_k_tasks(self, k):
        tasks = collections.deque(self.tasks[:k])
        pills = self.pills
        for worker in self.workers[-k:]:
            if tasks[0] <= worker:
                tasks.popleft()
            elif not pills or worker + self.strength < tasks[0]:
                return False
            else:
                del tasks[bisect.bisect(tasks, worker + self.strength) - 1]
                pills -= 1
        return True

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        task_assigner = TaskAssigner(tasks, workers, pills, strength)
        return binsearch(0, min(len(tasks), len(workers)) + 1, task_assigner.can_assign_k_tasks)
        