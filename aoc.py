class textfile():
    def __init__(self):
        import __main__
        pyfile = __main__.__file__.replace('\\', '/')
        x = next(i for i in range(len(pyfile) - 1, 0, -1) if pyfile[i] == '/')
        datadir = pyfile[:x] + '/data'
        self.name = datadir + pyfile[x:-3] + '.txt'
        from os.path import isfile, isdir
        from os import makedirs

        if not isdir(datadir):
            makedirs(datadir)
        if not isfile(self.name):
            f = open(self.name, 'w+')
            f.close()

        self.raw = open(self.name).read()

    def lines(self, processor=None):
        if processor:
            return [processor(x) for x in self.raw.splitlines()]

        return self.raw.splitlines()

    def split(self, processor=None, regex=None):
        if regex:
            from re import split
            data = split(regex, self.raw)
        else:
            data = self.raw.split()

        if processor:
            return [processor(x) for x in data]

        return data

    def splitted_lines(self, processor=None, regex=None):
        if regex:
            from re import split

            def splitter(x): return split(regex, x)
        else:
            def splitter(x): return x.split()

        if processor:
            return [[processor(x) for x in splitter(line)] for line in self.lines()]

        return [splitter(line) for line in self.lines()]

    def processed(self, processor):
        return [processor(x) for x in self.raw]


if __name__ != '__main__':
    _file = textfile()
    raw = _file.raw
    lines = _file.lines
    split = _file.split
    splitted_lines = _file.splitted_lines
