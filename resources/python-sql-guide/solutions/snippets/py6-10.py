import timeit, sys, os, platform
t_list = timeit.timeit("x in data", setup="data = list(range(1000)); x = 999", number=2000)
t_set = timeit.timeit("x in data", setup="data = set(range(1000)); x = 999", number=2000)
print("set membership is faster than list membership:", t_set < t_list)
print("python major version:", sys.version_info.major, "| separator is a slash:", os.sep in ("\\", "/"), "| system known:", platform.system() != "")
