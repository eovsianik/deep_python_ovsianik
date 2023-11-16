import cProfile
import pstats
import io


class profile_deco:
    def __init__(self, func):
        self._func = func
        self._profiler = cProfile.Profile()
        self._stats = None

    def __call__(self, *args, **kwargs):
        self._profiler.enable()
        result = self._func(*args, **kwargs)
        self._profiler.disable()
        return result

    def print_stat(self):
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(self._profiler, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
