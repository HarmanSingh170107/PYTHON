# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager
with (
open('file1.txt') as f1,'w',
open('file2.txt') as f2,'w'):
    x1=f1.write()
    x2=f2.write()