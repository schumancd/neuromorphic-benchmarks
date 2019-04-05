# Wisconsin Breast Cancer

Contributors: James S. Plank and Catherine D. Schuman

Though image classification or processing is the most popular use case of neuromorphic systems, there are many other types of data that could be processed by SNNs.  Even for relatively simple images, such as those in MNIST, the images themselves require a large number of inputs, which result in networks that have a minimum of hundreds of neurons.  Particularly for experimental hardware, it may be very difficult to build networks of this size to perform initial testing.  For our initial non-image data classification task, we select the [Wisconsin Breast Cancer dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+\%28Original\%29). This dataset includes a total of 699 data points, where each data point includes nine features and a label.  The nine features regard diagnosing breast cancer and are reported in integer values between 1 and 10.  Those features correspond to the following measured values: clump thickness, uniformity of cell size, uniformity of cell shape, marginal adhesion, single epithelial cell size, bare nuclei, bland chromatin, normal nucleoli, and mitoses.  The label corresponds to either benign or malignant.  We have split this data into a training set of size 444 and a testing set of size 255.

The training set is available [here](https://github.com/schumancd/neuromorphic-benchmarks/blob/master/wbc/training_wbc.txt) and the testing set is available [here](https://github.com/schumancd/neuromorphic-benchmarks/blob/master/wbc/testing_wbc.txt). The lines in each of these files takes the following format:

`f0 f1 f2 f3 f4 f5 f6 f7 f8 Type`

Where the `fn` is one of the nine features (clump thickness, uniformity of cell size, uniformity of cell shape, marginal adhesion, single epithelial cell size, bare nuclei, bland chromatin, normal nucleoli, and mitoses), and `Type` is one of `Benign` and `Malignant`.

## Scikit-Learn Results

There are many published results on this dataset.  A summary of some of the traditional neural network, spiking neural network, and neuromorphic results as of 2016 on this dataset are available in [this work](http://neuromorphic.eecs.utk.edu/publications/2016-07-01-an-evolutionary-optimization-framework-for-neural-networks-and-neuromorphic-architectures/).  For completion, we have also provided a short list of results for scikit-learn on this dataset:


| Classifier | Training | Testing |
| --- | :---: | :---: |
| KNN (neighbors = 3) | 0.995 | 0.925 |
| Naive Bayes | 0.975 | 0.929 |
| Random Forest (max_depth = 5, n_estimators=10, max_features=1) | 0.995 | 0.937 | 
| Linear SVM (kernel="linear", C=0.025) | 0.991 | 0.933 |
| MLP (one hidden layer of 100 neurons) | 0.989 | 0.933 | 
| Decision Tree (max depth=5) | 0.998 | 0.898 |
| AdaBoost | 1.0 | 0.937 | 
| RBF SVM (gamma=2, C=1) | 1.0 | 0.808 |

## Metrics to Report

The following metrics should be reported for this task:
- Accuracy on the training set
- Accuracy on the testing set
- Average energy per classification on the testing set


## Citation

Wolberg, W.H., & Mangasarian, O.L. (1990). Multisurface method of pattern separation for medical diagnosis applied to breast cytology. In Proceedings of the National Academy of Sciences, 87, 9193--9196. 

```
@inproceedings { wolberg1990multisurface,
  author = "W Wolberg and O Mangasarian",
  title = "Multisurface method of pattern separation for medical diagnosis applied to breast cytology,",
  pages = "9193--9196",
  month = "Dec",
  year = "1990",
  booktitle = "Proceedings of the National Academy of Sciences",
}
```
