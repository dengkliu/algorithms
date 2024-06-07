# https://leetcode.com/problems/exclusive-time-of-functions/description/

# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

# You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

# A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

# Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        stack = []
        id_stack = []
        time = collections.defaultdict(int)

        cur_time = 0
        cur_id = 0

        for l in logs:
            if "start" in l:
                start_time = int(l[l.index("start") + 6:])
                start_id = int(l[:l.index(":")])
                # the current running function runs for start_time - cur_time
                if stack:
                    time[cur_id] += start_time - cur_time
                # append to stack, update the cur time and the running fucntion Id
                stack.append(l)
                cur_time = start_time
                cur_id = start_id
            else:
                end_time = int(l[l.index("end") + 4:])
                # pops out the running function
                prev = stack.pop()
                # the function has been runing for end_time - cur_time + 1
                time[cur_id] += end_time - cur_time + 1
                # the blocked function (if any) will resume execution at end_time + 1
                cur_time = end_time + 1
                if stack:
                    # reset the running function Id 
                    cur_id = int(stack[-1][:stack[-1].index(":")])

        ans = []
        for i in range(n):
            ans.append(time[i])

        return ans