import csv
import numpy as np

def readfile(datafile: str):
    data = []
    with open(datafile, 'r', encoding="utf-8-sig") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            FGP = float(row[6])
            ORB = float(row[16])
            DRB = float(row[17])
            TRB = float(row[18]) 
            PTS = float(row[24])
            data.append([FGP, ORB, DRB, TRB, PTS])
    return data

def training(X, Y):
    X_transpose = np.transpose(X)
    A = np.matmul(X_transpose, X)
    A_inverse = np.linalg.inv(A)
    B = np.matmul(A_inverse, X_transpose)
    return np.matmul(B, Y)

def testing(X, B):
    Y_estimate = []
    for i in range(len(X)):
        s = 0
        for j in range(len(B)):
            s += B[j]*X[i][j]
        Y_estimate.append(s)
    return Y_estimate

def SSE(Y_actual, Y_estimate):
    s = 0
    for i in range(len(Y_actual)):
        s += (Y_actual[i] - Y_estimate[i]) ** 2
    return s

def MAPE(Y_actual, Y_estimate):
    s = 0
    for i in range(len(Y_actual)):
        s += abs(Y_actual[i] - Y_estimate[i]) / Y_actual[i]
    return (100*s)/len(Y_actual)


def main():
    NBA_2010 = np.array(readfile("data/NBA_2010.csv"))
    NBA_2011 = np.array(readfile("data/NBA_2011.csv"))
    NBA_2012 = np.array(readfile("data/NBA_2012.csv"))
    NBA_2013 = np.array(readfile("data/NBA_2013.csv"))
    NBA_2014 = np.array(readfile("data/NBA_2014.csv"))
    NBA_2015 = np.array(readfile("data/NBA_2015.csv"))
    NBA_2016 = np.array(readfile("data/NBA_2016.csv"))
    NBA_2017 = np.array(readfile("data/NBA_2017.csv"))
    NBA_2018 = np.array(readfile("data/NBA_2018.csv"))
    NBA_2019 = np.array(readfile("data/NBA_2019.csv"))

    Y_test = NBA_2019[:,4]
    X_test = NBA_2019[:,0:4]

    print("Linear Regression Test")
    print("Test Data: 2019")

    print('====Part 1: 2018 as Training Data====')
    Y = NBA_2018[:,4] #PTS column
    X = NBA_2018[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2018
    BETA = training(X, Y)
    print(BETA)

    Y_estimate = testing(X_test, BETA)
    sse = SSE(Y_test, Y_estimate)
    print("SSE: ", sse)
    mape = MAPE(Y_test, Y_estimate)
    print("MAPE: ", mape)

    print('====Part 2: 2017-18 as Training Data====')
    Y1 = NBA_2017[:,4] #PTS column for 2017
    Y2 = NBA_2018[:,4] #PTS column for 2018
    Y = np.concatenate((Y1, Y2), axis=None)

    X1 = NBA_2017[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2017
    X2 = NBA_2018[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2018
    X = np.concatenate((X1, X2), axis=0)

    BETA = training(X, Y)
    print(BETA)

    Y_estimate = testing(X_test, BETA)
    sse = SSE(Y_test, Y_estimate)
    print("SSE: ", sse)
    mape = MAPE(Y_test, Y_estimate)
    print("MAPE: ", mape)

    print('====Part 2: 2010-18 as Training Data====')
    Y1 = NBA_2010[:,4] #PTS column for 2010
    Y2 = NBA_2011[:,4] #PTS column for 2011
    Y3 = NBA_2012[:,4] #PTS column for 2012
    Y4 = NBA_2013[:,4] #PTS column for 2013
    Y5 = NBA_2014[:,4] #PTS column for 2014
    Y6 = NBA_2015[:,4] #PTS column for 2015
    Y7 = NBA_2016[:,4] #PTS column for 2016
    Y8 = NBA_2017[:,4] #PTS column for 2017
    Y9 = NBA_2018[:,4] #PTS column for 2018
    Y = np.concatenate((Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9), axis=None)

    X1 = NBA_2010[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2010
    X2 = NBA_2011[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2011
    X3 = NBA_2012[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2012
    X4 = NBA_2013[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2013
    X5 = NBA_2014[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2014
    X6 = NBA_2015[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2015
    X7 = NBA_2016[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2016
    X8 = NBA_2017[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2017
    X9 = NBA_2018[:,0:4] #FGP, ORB, DRB, TRB, PTS for 2018
    X = np.concatenate((X1, X2, X3, X4, X5, X6, X7, X8, X9), axis=0)

    BETA = training(X, Y)
    print(BETA)

    Y_estimate = testing(X_test, BETA)
    sse = SSE(Y_test, Y_estimate)
    print("SSE: ", sse)
    mape = MAPE(Y_test, Y_estimate)
    print("MAPE: ", mape)

if __name__ == '__main__':
	main()