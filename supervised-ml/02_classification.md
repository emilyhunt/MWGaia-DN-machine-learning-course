
# 2. Classification

## Have you encountered a classification problem in your own research? 

![Problem: group new students!](./images/new_students.jpg)










## How did you solve it?

![Solution: the sorting hat?](./images/sorting_hat.jpg)










## Well, how exactly? 

![Inside the hat](./images/decision_tree.png)

**Basic illustration of different classfication methods:[sklearn notebook](2_0_classifier_comparison_sklearn.ipynb)**

## 2.1 Some terminology

Most terms have been introduced by Xavi and Mario yesterday:

* labels
* features
* categories

* error rate
* classification loss (function)
* misclassification risk

* true & false positives, true & false negatives
* confusion matrix
* completeness
* contamination 
* ...

To sort these out, 
**Let's have a look at the [astroML notebook](2_1_classification_astroML.ipynb)**

If you want more details, [here is the relevant book chapter](Material/Ivezic2020_09_classification.pdf). (Note that the book introduces classification as a special case of regression: "Classification is simply the analog of regression where y is categorical, for example $y = {0, 1}$").

[Here](Material/Anders2014_classification_poster.pdf) is an example of how these codes can be adapted for a real-life astro problem (from the 1st year of my PhD, 10 years ago:)

### 2.2 Tree-based algorithms

Now that we have seen a couple of the typical classification methods, **Let's have a look at a simple class of models: [Decision trees](2_2_decision_tree_classification.ipynb)** 
The theory is explained in Sect. 9.7 of the astroML book. If you prefer a short explanatory video, try for example [this](https://www.youtube.com/watch?v=JcI5E2Ng6r4). 

## 2.3 GROUP TASK! 

(o-O all this will be EXPERIMENTAL... it might fail!)
Why ***could*** it work? Because so many of you are already experts:)

### Dive into one (class of) algorithms:

* **Get together into 4 (heterogeneous:) groups** (~6 PhDs + ~2 seniors) 
* **Each group picks 1 of the following 4 classification algorithms:**
    1. Random forests
    2. Gradient boosting / bagging
    3. Support-vector machines (incl. kernel SVMs)
    4. Multi-layer perceptron
* **Find out the 2-3 people who know the least about that technique.**
* The rest of the group will teach these 2-3 people within the next 15-20 minutes how the method works. **Use the internet:)**
* **Each group (represented by the people who initially knew the least:) presents a 3-5 slides(=minutes) summary of their method to the rest.**

Below are some ideas to get things going, but feel free to do your completely own thing!

### 2.2.1 Random-forest

[Some random notebook on kaggle](https://www.kaggle.com/code/prashant111/random-forest-classifier-tutorial)

### 2.2.2 Gradient boosting / bagging

[A complete lecture](https://www.youtube.com/watch?v=UHBmv7qCey4)

### 2.2.3 SVMs

Support-vector machines! Woohoo, algebra! 

[A complete lecture](https://www.youtube.com/watch?v=_PwhiWxHK8o)
[sklearn page](https://scikit-learn.org/stable/modules/svm.html)
[astroML summary](https://www.astroml.org/astroML-notebooks/chapter9/astroml_chapter9_Classification.html#support-vector-machines)

### 2.2.4 Neural networks

The [basics](https://github.com/zingale/computational_astrophysics/blob/main/content/machine-learning/neural-net-basics.md) of how an ANN works have been introduced by Emily in the morning. 

When we say "neural networks" or "ANNs", we usually mean [multi-layer perceptrons (MLPs)](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multi-layer-perceptron).

[Here](https://github.com/zingale/computational_astrophysics/blob/main/content/machine-learning/neural-net-mnist.ipynb) is anexample of a very simple ANN (coded from scratch) to classify hand-written digits.

[Here](https://github.com/zingale/computational_astrophysics/blob/main/content/machine-learning/keras-mnist.ipynb) is more complex neural network to do the same task - better (constructed with keras - see also the [afternoon session](04_convolutional_neural_networks.md)).


