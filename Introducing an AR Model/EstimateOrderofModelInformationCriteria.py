# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:38:15 2020

@author: User


Estimate Order of Model: Information Criteria

Another tool to identify the order of a model is to look at the Akaike 
Information Criterion (AIC) and the Bayesian Information Criterion (BIC). 
These measures compute the goodness of fit with the estimated parameters, but 
apply a penalty function on the number of parameters in the model. You will take 
the AR(2) simulated data from the last exercise, saved as simulated_data_2, and 
compute the BIC as you vary the order, p, in an AR(p) from 0 to 6.

"""

# Import the module for estimating an ARMA model
from statsmodels.tsa.arima_model import ARMA

import numpy as np
import matplotlib.pyplot as plt


simulated_data_2 = ([-1.0856306 ,  1.64872381, -0.38056661, -1.77257189,  0.59911287,
        1.82374039, -3.70065733,  1.24435966,  1.62951767, -2.2177589 ,
        0.16291389,  0.47287037,  1.15879324, -1.47603905,  0.0940035 ,
       -0.04794166,  2.20649403,  0.87727217, -0.18425761,  0.23355932,
        0.65251027,  1.02915807, -1.74908179,  1.9165307 , -1.87907455,
       -0.08526598,  1.52198715, -2.3162932 ,  0.79311105, -0.64273357,
       -0.10791255, -2.54102151, -0.21454644,  0.19115708,  0.87713211,
       -0.75726208,  0.19406353,  0.79896322, -1.41713333,  0.89421836,
       -0.91675753, -1.44588048,  0.75165576,  0.55657655, -0.22085361,
       -0.0462913 ,  2.48639613, -1.06503813,  0.87184004,  2.03455075,
       -2.77636779,  0.01666724,  2.56662222, -2.34303624,  0.66551831,
        1.37291586, -0.13269861,  1.42263059,  0.68187537,  0.23347827,
       -1.11735829,  1.39523416, -0.18766101, -1.6322391 ,  2.45294081,
       -0.17485622, -0.58547843,  0.17065186, -1.12504873,  0.82335775,
        0.31193909, -1.26532576,  1.82781778, -1.81429599, -1.58286809,
        2.53373674, -1.44874766, -0.01690201, -0.39275122, -1.36524143,
        2.1922076 , -1.59462111,  1.96006288,  0.10965679, -0.96857109,
       -0.53765679, -0.11929659, -0.97964814,  2.71069122, -1.16807906,
        1.03784561, -1.5396357 ,  0.79346286,  1.16367493, -1.27125458,
        1.44476473, -1.57005037, -0.85487074,  1.36333817, -0.94071811,
        0.79748411, -2.17416296,  1.77751718,  2.18404251, -1.86830664,
        0.49991336,  0.44009346, -2.2760058 ,  1.65972208, -1.91844125,
        0.22546853,  1.68312081, -1.81273   ,  1.08395075,  0.90618761,
       -0.59015693, -1.28871059,  0.61779816,  1.97534562, -3.39559259,
        1.16896585, -0.23480981, -0.08905651,  0.87209246,  1.11215244,
       -1.1991516 ,  1.19818656,  0.14057369,  0.03054712, -0.62442431,
       -0.63183102, -0.53361721, -0.24671758,  0.62980229,  0.4570833 ,
       -0.13972182, -0.602247  ,  2.20923485,  0.37399881, -1.24116986,
       -0.19092914,  0.61712339,  0.95430335, -0.42495405,  0.52523013,
       -0.39973199,  0.53854105,  1.34133942, -1.20603475,  0.46452676,
        0.33691085, -0.05777918, -1.47829462, -0.97255813,  0.00736819,
        0.45528882,  0.27847242, -0.83434466,  1.79432255, -0.96946611,
        0.0636989 ,  0.05865662,  0.07972315,  0.6390432 ,  0.25831057,
       -1.24512224,  2.19324395, -2.03743615,  0.64371552, -0.04939504,
       -1.21246931,  0.66717951, -0.77738069,  0.3391818 ,  0.43279109,
        1.11050018, -0.48875321, -0.65112347,  0.14568023,  0.24790701,
       -0.09898744,  1.44460963,  0.55828338, -1.12728885, -0.03975384,
       -2.19501565,  0.78001513, -0.78756209, -0.11629174,  0.69762791,
       -0.2064969 , -0.11535824,  0.33074613, -0.28995798,  0.27176988,
       -3.30712954,  1.63345327, -0.09878382, -0.77202741,  0.27490533,
        0.76997514, -1.14256202,  2.65524677, -0.56208252, -0.46563177,
        0.24134151, -0.09163766, -0.93272693,  0.49192492,  0.26334665,
        0.27395615,  0.33631209, -0.55885165, -1.18166489,  0.2075518 ,
        1.84216143, -0.27150408, -0.02012639, -0.66776718,  0.41034338,
       -1.30154456,  0.10588685,  0.08172792, -0.44244274,  1.1975492 ,
       -2.00452261, -0.02198346, -0.76014111, -0.77467351,  0.81690233,
       -1.85817988,  1.62370601, -0.66358542, -0.02017222,  0.53375569,
       -0.74836827,  1.32137397, -0.76265663,  0.65525204, -0.36346662,
        0.31237875,  0.20127541,  0.03549107, -1.05598511,  1.05881952,
       -0.63745317,  0.69531407, -2.37844594, -0.24664288,  1.22496507])

# Fit the data to an AR(p) for p = 0,...,6 , and save the BIC
BIC = np.zeros(7)

for p in range(7):
    mod = ARMA(simulated_data_2, order=(p,0))
    res = mod.fit()
    
# Save BIC for AR(p)    
    BIC[p] = res.bic
    
# Plot the BIC as a function of p
plt.plot(range(1,7), BIC[1:7], marker='o')
plt.xlabel('Order of AR Model')
plt.ylabel('Bayesian Information Criterion')
plt.show()