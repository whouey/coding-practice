from __future__ import annotations
from typing import List

# let Job:{id:int, downSteams:List[Job]}
# any job should be executed before it's downstream jobs
# given a list of jobs
# find a valid execution order 

# the graph is a DAG  
# the question is basically a topological sorting problem.

# I refactored the original solution which came up with in the coding interview to make it more readable

class Job:
    def __init__(self, id:int = 0, downStreams:List[Job] = []) -> None:
        self.id = id
        self.downStreams = downStreams

    @classmethod
    def getExecutedOrder(cls, jobs: List[Job]) -> List[Job]:
        upStreams = {job:[] for job in jobs} # initiate a dict of all jobs alone with empty lists

        for job in jobs:
            for downStream in job.downStreams:
                upStreams[downStream].append(job) # get all upstream filled

        remaining = jobs[:] # list all jobs
        executedOrder = []

        while remaining: # O(N)
            for job in remaining: # O(N)
                # execute a job if there is no upstream or all upstream executed
                if not upStreams[job] or all(upStream in executedOrder for upStream in upStreams[job]): # O(E^2)
                    executedOrder.append(job)
                    remaining.remove(job)

        # time complexity: 
        # let N is the number of jobs
        # let E is the number of dependencies
        # O(N^2+E^2).
        
        return executedOrder


# by example of https://en.wikipedia.org/wiki/Topological_sorting
job8 = Job(10)
job7 = Job(9)
job6 = Job(2)
job5 = Job(8, [job7])
job4 = Job(11, [job6, job7, job8])
job3 = Job(3, [job5, job8])
job2 = Job(7, [job4, job5])
job1 = Job(5, [job4])

jobs = [job1, job2, job3, job4, job5, job6, job7, job8]

executedOrder = Job.getExecutedOrder(jobs)
print([job.id for job in executedOrder])