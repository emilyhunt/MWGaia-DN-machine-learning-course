

# 4. Convolutional neural networks

Don't be afraid - try to play a bit with CNNs yourself.

To understand CNNs, you should first understand the basics of simple ANNs (aka multi-layer pereceptrons).
But then there is a vast literature (including videos, articles, and code examples) to help you get started. 
For instance, a good start could be:

* [Convolutional Neural Networks: A Comprehensive Guide](https://medium.com/thedeephub/convolutional-neural-networks-a-comprehensive-guide-5cc0b5eae175)

## 4.1 Astronomical applications

Since it has been a full day and we want to keep it playful, just choose one of the following resources to play around and perhaps adapt it for your own research! 

### Using a CNN to determine stellar parameters from RAVE spectra (should work very similarly for Gaia RVS spectra!)

[This notebook](04_01_rave_cnn_guiglion2020.ipynb) reproduces the results of [Guiglion+2020](https://ui.adsabs.harvard.edu/abs/2020A%26A...644A.168G/abstract) (transferring high-resolution, high-quality APOGEE labels to medium-resolution RAVE spectra).

IDEA: Try to adapt it for Gaia DR3 RVS spectra! What do you have to do? What are the main obstacles?

Other examples implementing this idea are:
* [StarNet](https://github.com/Spiffical/StarNet/tree/master) (TASK: find out where in the repo you can find the architecture of the CNN model and draw it:)
* [astroNN](https://github.com/henrysky/astroNN) 
* [ThePayne](https://github.com/pacargile/ThePayne)

### CNNs for astronomical image classification

[This notebook](04_02_classifying_galaxy_mergers_with_CNNs.ipynb) gives an example using HST and JWST images of (potentially) merging galaxies.
[Hello Universe](https://archive.stsci.edu/hello-universe) has 2 more nice CNN examples - check them out!



