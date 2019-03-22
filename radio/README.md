# Satellite Radio Data Classification Task

Our time series classification task is based on a pared down version of the satellite radio dataset [RadioML](https://www.deepsig.io/datasets). The data instances in this task are composed of 128-sample snippets of complex-valued radio signals.  In the RadioML dataset, the waveforms have been modulated by 11 different waveforms and 20 different signal-to-noise ratios.  We use a simplified version of this task, described by [Reynolds, et al.](http://neuromorphic.eecs.utk.edu/publications/2018-07-24-a-comparison-of-neuromorphic-classification-tasks/), where the goal is to differentiate one of the modulation types (8PSK) from all of the other modulation types.  

The training set is composed of 300 data instances, equally divided between 8PSK and other modulation types (available in training-radio-8spk-10.txt file).  The testing set (available in the testing-radio-8spk-10.txt file) is composed of 300 different data instances, again, equally divided between 8PSK and other modulation types.

The format of the files is as follows: each line is a different data instance.  The first field in the line is the classification label.  Since we frame this as a binary classification task, the labels should be interpreted as 8PSK-10 as class 0 and all other labels as class 1.  However, we include the exact modulation type to provide complete information to the user. 

The remaining fields on each line comprise the data itself, where the real values and complex values are interleaved. In particular, if the real value at time 0 is r0, the complex value at time 0 is c0, the real value at time 1 is r1, etc., then each line is formatted:

`label r0 c0 r1 c1 r2 c2...r127 c127`
