with open(r"webURL", 'r') as fp:
    num_lines = sum(1 for line in fp if line.rstrip())
    print('Total lines:', num_lines) 
