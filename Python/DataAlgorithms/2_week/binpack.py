import random

def bins(a):
    l = [0]
    sorted(a, reverse=False)
    #b = b.reverse()
    for i in range(len(a)):
        j = 0
        while float(a[i]) + float(l[j]) > 1:
            j = j + 1
            if j == len(l):
                l.append(0)

        l[j] = l[j] + float(a[i])
    print(l)
    return l



if __name__=="__main__":
    A = [0.827, 0.757, 0.804, 0.66, 0.089, 0.95, 0.243, 0.573, 0.302, 0.813]
    #B = [0.827, 0.757, 0.804, 0.95, 0.243, 0.573, 0.302, 0.813, 0.66, 0.089]

    #rand = random()
    #for i in range(10):
    #    A.append("{:.3f}".format(random.random()))
    #print()
    G = []

    for i in range(1000):
        G.append(len(bins(random.sample(A, len(A)))))


    #print(len(bins(B)))
