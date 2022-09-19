Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #code to read line of log
#
def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

with open(r'webURL', 'rb') as fp:
    c_generator = _count_generator(fp.raw.read)
    # count each \n
    count = sum(buffer.count(b'\n') for buffer in c_generator)
    print('Total requests:', count + 1)
