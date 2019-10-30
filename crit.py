def kaijou(numb):
    numbs = 1
    while numb > 0:
        numbs = numbs * numb
        numb = numb - 1
    return numbs


def combin(bo, si):
    return kaijou(bo)/(kaijou(si)*kaijou(bo-si))


def nakami(rig, lef, oth, k):
    sum1 = 0
    for m in range((rig-lef)//2+1, rig+oth-k+1):
        sum1 = sum1 + combin(rig+oth-k, m)*(0.01**m)
    return sum1


def keisan(ri, le, ot):
    if ri < le:
        tii = ri
        ri = le
        le = tii
    sum2 = 0
    for i in range(ri+ot):
        sum2 = sum2 + combin(ri+ot, i)*((0.05+0.02)**i)*nakami(ri, le, ot, i)
        # print(nakami(ri, le, ot, i))
    return sum2
