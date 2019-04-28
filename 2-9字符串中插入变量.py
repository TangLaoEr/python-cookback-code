
s = '{name} has {n} messages.'
s.format(name='Guido', n=37)


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido',37)
s.format_map(vars(a))