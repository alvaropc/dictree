from src import dictree

d = {'a': 34, 'b': {'m': 234, 'j': 23452}}
print(dictree(d).branches)
print(dictree(d).nodes)
print(dictree(d))
# print(dictree(d).branches)

print(dictree(d).nbranches())
