import csv
import numpy as np
import random
import matplotlib.pyplot as plt

def readcsv(datafile):
    data = []

    with open(datafile, 'r', encoding="utf-8-sig") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            data.append(float(row[-1]))

    return data

def permuation_test(data1, data2, n):
    data1_mean = np.mean(data1)
    data2_mean = np.mean(data2)
    t_obs = abs(data1_mean-data2_mean)
    cnt = 0
    for i in range(n):
        data1_idx = random.randint(0, len(data1)-1)
        data2_idx = random.randint(0, len(data2)-1)
        temp = data1[data1_idx]
        data1[data1_idx] = data2[data2_idx]
        data2[data2_idx] = temp

        data1_permutation_mean = np.mean(data1)
        data2_permutation_mean = np.mean(data2)
        t_i = abs(data1_permutation_mean - data2_permutation_mean)
        if t_i > t_obs:
            cnt += 1

    return cnt/n

def plot_ecdf(data1, data2):
    n = len(data1)
    Srt = sorted(data1)

    X = [min(Srt)]
    Y = [0]
    for i in range(0, n):
        X = X + [Srt[i], Srt[i]]
        Y = Y + [Y[len(Y)-1], Y[len(Y)-1]+(1/n)]
    X = X + [max(Srt)]
    Y = Y + [1]

    plt.figure('eCDF')
    plt.plot(X, Y ,label='ecdf1')
    plt.scatter(Srt, [0]*n, color='red', marker='x', s=100, label='samples1')

    n = len(data2)
    Srt = sorted(data2)

    X = [min(Srt)]
    Y = [0]
    for i in range(0, n):
        X = X + [Srt[i], Srt[i]]
        Y = Y + [Y[len(Y)-1], Y[len(Y)-1]+(1/n)]
    X = X + [max(Srt)]
    Y = Y + [1]

    plt.figure('eCDF')
    plt.plot(X, Y ,label='ecdf2')
    plt.scatter(Srt, [0]*n, color='blue', marker='.', s=100, label='samples2')

    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('eCDF')
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

def main():
    data1999 = readcsv("data/NBA_1999.csv")
    data2009 = readcsv("data/NBA_2009.csv")
    data2019 = readcsv("data/NBA_2019.csv")

    p_val_1 = permuation_test(data1999, data2009, 2000)
    p_val_2 = permuation_test(data2009, data2019, 2000)
    print("NBA1999 vs NBA2009 P-value: ", p_val_1)
    print("NBA2009 vs NBA2019 P-value: ", p_val_2)

    plot_ecdf(data1999, data2009)
    plot_ecdf(data2009, data2019)


if __name__ == '__main__':
	main()
