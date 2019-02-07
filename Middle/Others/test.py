class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = dict()
        cnt = 0
        task_len = len(tasks)+1
        for i in tasks:
            d[i] = d.get(i, 0) + 1
        while max(d, key=d.get) :
            mins = None
            for key in list(d):
                if d[key]%task_len == 0:
                    del d[key]
                    if len(d) == 0:
                        return cnt
                    continue
                if (mins == None or (d[key]< task_len and d[mins]%task_len < d[key]%task_len)):
                    mins = key
                if d[key] >= task_len:
                    d[key] -= task_len
            if d[mins] < task_len:
                d[mins] -= 1
                d[mins] += task_len*(n+1)
            cnt += 1
            if mins:
                print(mins, end=" ")
            else:
                print("-", end=" ")
            print(cnt, d)
        return cnt

tasks = ["A", "A", "A", "A", "B", "B", "B", "C", "C", "D"]
tasks = ["A", "A"]
tasks = ["A", "A", "A", "B", "B", "B"]

cnt = Solution().leastInterval(tasks, 2)
print(cnt)