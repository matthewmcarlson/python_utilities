#!/bin/python

class striping_reader():
    """A custom context manager that acts like open (from the standard library)
    but removes junk and strips every line using string.strip().

    usage:
    >>> with striping_reader('example.txt', mode='r', buffering=0, junk='|') as f:
    ...     for line in f:                                                                                                                                                                                                                        
    ...             print line
    or
    >>> with striping_reader('example.txt') as f:                                                                                                                                                                                                 
    ...     for line in f:                                                                                                                                                                                                                        
    ...             print line

    """
    def __init__(self, name, mode=None, buffering=None, junk=''):
        """Arguments are the same as open (using the same defaults, but with 
        the addition of 'junk.'

        args:
        name (string): name of the file to open 
        
        mode (string): mode (e.g. 'a', 'w+', etc) for opening the file
        
        buffering (int): "The optional buffering argument specifies the file’s 
        desired buffer size: 0 means unbuffered, 1 means line buffered, any 
        other positive value means use a buffer of (approximately) that size 
        (in bytes). A negative buffering means to use the system default, which 
        is usually line buffered for tty devices and fully buffered for other 
        files. If omitted, the system default is used." from 
        https://docs.python.org/2/library/functions.html?highlight=file#open
        
        junk (string, default is ''): a list of characters (represented as a 
        string) that are removed from each line before stripping.
        """
        if mode is None and buffering is None:
            self.fi = open(name)
        elif mode is None and buffering is not None:
            self.fi = open(name, buffering=buffering)
        elif mode is not None and buffering is None:
            self.fi = open(name, mode=mode)
        else:
            self.fi = open(name, mode=mode, buffering=buffering)
        self.junk = junk
        return 

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        return

    def __iter__(self):
        return self
 
     # Python 3 compatibility
    def __next__(self):
        """Get the next line of the file."""
        return self.next()
 
    def next(self):
        """Get the next line of the file."""
        try:
            _newline = self.fi.next()
            for char in self.junk:
                _newline = _newline.replace(char, '')
            newline = _newline.strip()
            while not newline:
                _newline = self.fi.next()
                for char in self.junk:
                    _newline = _newline.replace(char, '')
                newline = _newline.strip()
            return newline
        except StopIteration:
            raise StopIteration()

if __name__ == '__main__':
    from sys import argv
    with open striping_reader(*argv) as f:
        for line in f:
            print f
