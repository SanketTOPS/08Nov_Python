import itertools

data={'1':['a','b'],'2':['c','d']}

for i in itertools.product(*[data[k] for k in sorted(data.keys())]):
    print(''.join(i))
