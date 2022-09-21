import os

#        open this file, read
# f = open('testdata.txt', 'r')
#
# print(f.read())
#
# # always close the files that you open, if you are not using an with open()
# f.close()

# automatically closes after the loop breaks
# with open('testdata.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#
#     while len(f_contents) > 0:
#         # places an asterisk at the end of size_to_read character limit
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)