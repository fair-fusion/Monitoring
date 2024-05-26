#Generate a batch number that always adds one number to the last batch number. 
#Unless, the batchnumber is already given in a settings file
def batchnr():
    if os.path.isfile('settings.txt'):
        with open('settings.txt') as f:
            for line in f:
                if line.startswith('batchnumber'):
                    batchnumber = line.split('=')[1]
                    batchnumber = int(batchnumber)
                    batchnumber += 1
                    return batchnumber
    else:
        with open('settings.txt', 'w') as f:
            f.write('batchnumber=0')
            batchnumber = 0
            batchnumber += 1
            return batchnumber
        
#import variables from a settings file
