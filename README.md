# NBA-Data-Analysis

This is a follow up project of CSE357 "Statistical Methods for Data Science". 

## Part 1 - Hypthosis Test
In this statistical analysis we are testing if there is significant difference in score in the NBA by decades
(1999 vs 2009) and (2009 vs 2019)

we are doing two test, a permuation test (NBA_Permuation_Test.py) and a k-s test (NBA_KS_Test.R).

The result show that there is significant differences.

Result:
    NBA1999 vs NBA2009 P-value:  0.0005
    NBA2009 vs NBA2019 P-value:  0.0

    [1] 0.7977011
    [1] 0.8

    Graph Images require execution of file.


## Part 2 - Linear Regression

Fields Used in Training: 
    FGP - Field Goal percentage
    ORB - Offensive Rebounds/game
    DRB - Defensive Rebounds/game
    TRB - Total Rebounds/game
    PTS - points/game

    SSE refers to sum of squared error
    MAPE refers to mean absolute percentage error

    Note: In this part we ignored beta_0

Result:
    Linear Regression Test
    Test Data: 2019
    ====Part 1: 2018 as Training Data====
    [1.59603600e+02 1.84807854e-02 4.56192324e-01 3.97193567e-01]
    SSE:  621.0881913978776
    MAPE:  3.3607366754821593
    ====Part 2: 2017-18 as Training Data====
    [ 1.60780254e+02 -2.86961073e-01 -1.28371721e-02  8.15754406e-01]
    SSE:  624.5248437513496
    MAPE:  3.3778071483056804
    ====Part 2: 2010-18 as Training Data====
    [130.72004806  -0.73889371   0.46331549   0.81421273]
    SSE:  1244.6781577158763
    MAPE:  5.119033612955802
