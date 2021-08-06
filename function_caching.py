# function caching : store function return value(s) to avoid re-executing costly calculations

from functools import wraps, lru_cache
import time


def cache_job(function):
    cached_jobs = {}
    @wraps(function)
    def wrapper(*args):
        try:
            return cached_jobs[args]
        except KeyError:
            result = function(*args)
            cached_jobs[args] = result
            return result
    return wrapper


start_time = time.time()

@cache_job
#@lru_cache
def execute_job(calculation):
    result = eval(calculation)
    time.sleep(result)    
    return calculation + " = " + str(result)

def run_pipeline(jobs):
    for job in jobs:
        print(f"Executing job: {job['name']}")
        print(f"\t Result: {execute_job(job['calculation'])}")


jobs = [{"name": "build", "calculation": "1 + 0"}, {"name": "analyze code", "calculation": "5 - 3"}, {"name": "analyze code", "calculation": "5 - 3"}, {"name": "package", "calculation": "7 - 6"}]
run_pipeline(jobs)

print(f"Finished running jobs. Time: {round(time.time()-start_time, 3)}s")

# Without caching - Time: 6.045s
# With custom caching - Time: 4.022s
# With lru caching - Time: 4.014s