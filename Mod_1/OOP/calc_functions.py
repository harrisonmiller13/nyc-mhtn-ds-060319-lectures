def calc_mean(data):
    mean = sum(data)/len(data)
    
    return mean


def calc_median(data):
    n = len(data)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(data)[n//2]
    else:
            return sum(sorted(data)[n//2-1:n//2+1])/2.0
        
        
def calc_mode(data)
    def calc_mode (data):
    return max(set(data), key=data.count)


def calc_var(data):
    mean = calc_mean(data)
    return sum([(x-mean)**2 for x in data])/(len(data)-1)


def calc_std (data):
    variance = calc_var(data)
    return (variance)**.5


def calc_cov (data1,data2)
    def calc_cov(data1,data2):
    a_mean = calc_mean(data1)
    b_mean = calc_mean(data2)

    sum = 0

    for i in range(0, len(data1)):
        sum += ((data1[i] - a_mean) * (data2[i] - b_mean))

    return sum/(len(data1)-1)
