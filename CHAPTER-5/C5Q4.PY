s = set()
s.add(20)
s.add(20.0)
s.add('20')#LENGTH IS 2 BECAUSE 20.0 AND 20 ARE CONSIDERED AS INT AND SAME VALUE
print(len(s))