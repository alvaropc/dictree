from src import dictree

d = {'a': 34, 'b': {'m': 234, 'j': 23452, "kl":{"k":534,"l":234}},"c":{"k":43,"sdfnkj":34}}
# print(dictree(d).branches)
# print(dictree(d).nodes)
# print(dictree(d).nbranches())

print(dictree(d))
# print(dictree(d).branches)

