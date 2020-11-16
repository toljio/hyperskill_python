dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
s = [x for x in input().split() if x not in dictionary]
if s:
    print("\n".join(s))
else:
    print("OK")
