def rev(x10):
    x10a = x10.split('.')[1]
    x10dire = x10.split('.')[2]
    if x10dire == 'counthapright':
        direc = 'counthapleft' 
    else:
        direc = 'counthapright'
    return '10X.'+x10a+'.'+direc
