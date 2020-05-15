# Integral Transform Applied to Stock Markets

This repository is my attempt to implement the following idea of mine.

## Project Idea

Ever since I have learned about the probability distributions in my statistic class, I started seeing them everywhere, and even in some very peculiar places- the distribution of bird poop on the sidewalk under a tree is surprisingly Gaussian. After learning the principles of statistical mechanics I have seen how to use these distributions and the basic mathematical idea to make sense of very complicated phenomenon. Now, we all know how Fourier transforms (FT) on non-periodic data sets result in the finding of the spatial frequency, using which we can find patterns in the original data sets, e.g. FT on an air pressure vs time data plucks out the different frequencies that make up a sound. This Fourier Transform works, more generally, by transforming the data set on to the Fourier space, where the emergent geometry and symmetry provides this very valuable information- the spatial frequency. So, what I am thinking about is deriving an integral transform equation similar to Fourier’s, where the transformed space, gives some valuable information about the data set we are transforming. Such an integral transform can find patterns in stock market data for a given time interval, and using principles of statistical mechanics and machine learning we can theoretically predict the behavior of such chaotic systems by analyzing the distributions of these new data that we would create.

## Present Status 

The current repository contains the code for implementing Fourier Transform's on to the data set of Atlaba Inc. I am playing around with the paramters of sampling frequency to better understand the nature of the dynamics of such analysis.
