from collections import defaultdict


def none():
    return None

d = defaultdict(none)
d['css']
print(d)
d['html']
print(d)
d['css'] = 0
d['html'] = '<body></body>'
print(d)

d = defaultdict(lambda: 7)
print(d['oi'])
print(d)
