class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        lenJobs = len(jobDifficulty)
        
        if lenJobs < d:
            return -1

        min_diff_prev_day, min_diff_curr_day = [float('inf')] * lenJobs, [float('inf')] * lenJobs

        for day in range(d):
            stack = []
            for i in range(day, lenJobs):
                if i == 0:
                    min_diff_curr_day[i] = jobDifficulty[0]
                else:
                    min_diff_curr_day[i] = min_diff_prev_day[i - 1] + jobDifficulty[i]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    diff_incr = jobDifficulty[i] - jobDifficulty[j]
                    min_diff_curr_day[i] = min(min_diff_curr_day[i], min_diff_curr_day[j] + diff_incr)
                if stack:
                    min_diff_curr_day[i] = min(min_diff_curr_day[i], min_diff_curr_day[stack[-1]])

                stack.append(i)

            min_diff_prev_day, min_diff_curr_day = min_diff_curr_day, min_diff_prev_day

        return min_diff_prev_day[-1]