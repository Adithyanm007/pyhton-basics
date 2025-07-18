def read_file(filename):
    with open(filename,'r') as file:
        for line in file:
            yield line
filename= 'IndustryReadyDay14/trial.py'
for line in read_file(filename):
    print(line.strip())