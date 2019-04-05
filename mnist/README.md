# MNIST Image Data Classification

Contributors: James S. Plank and Catherine D. Schuman

Repository created: 2019

We use the [MNIST handwritten digit classification task](http://yann.lecun.com/exdb/mnist/) as the image classification task, as it is one of the most popular neuromorphic tasks published in the literature to date.  Though there are neuromorphic versions of the MNIST handwritten digit classification task (such as [N-MNIST](https://www.garrickorchard.com/datasets/n-mnist)), we restrict our attention to the original task, in which there are 60,000 training examples and 10,000 testing examples, and each data example is a 28 by 28 pixel grayscale image depicting a handwritten number (0-9).  We restrict our attention to the original dataset because there are many existing published results in the neuromorphic community as well as the many published results for other machine learning techniques.  We do not, however, specify how the input should be encoded into the network, which leaves the benchmark user some freedom in how they approach the task.  

We do not include the data for the MNIST task in the repository as it is available as we used it on the [MNIST website](http://yann.lecun.com/exdb/mnist/). 

## Metrics to Report

The following metrics should be reported for this task:
- Accuracy on the training set
- Accuracy on the testing set
- Average energy per image classification on the testing set

## Citation

Y. Lecun, L. Bottou, Y. Bengio and P. Haffner, "Gradient-based learning applied to document recognition," in Proceedings of the IEEE, vol. 86, no. 11, pp. 2278-2324, Nov. 1998.

```
@ARTICLE{mnist, 
author={Y. {Lecun} and L. {Bottou} and Y. {Bengio} and P. {Haffner}}, 
journal={Proceedings of the IEEE}, 
title={Gradient-based learning applied to document recognition}, 
year={1998}, 
volume={86}, 
number={11}, 
pages={2278-2324}, 
doi={10.1109/5.726791}, 
ISSN={0018-9219}, 
month={Nov}}
```
