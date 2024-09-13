# A two-day machine learning course for the MWGaia-DN

This repository contains course materials for a two-day machine learning course at the [MWGaia-DN doctoral school](https://indico.cern.ch/event/1413524/overview) in Coimbra, Portugal (9th - 13th September 2024), created by [Friedrich Anders](https://github.com/fjaellet) and [Emily Hunt](https://github.com/emilyhunt).


## Topics

**Supervised learning techniques**: Classification and regression, with a focus on neural networks and tree-based algorithms. Work examples include source classification, determining stellar parameters from spectra, and estimating photometric redshifts.

**Unsupervised learning techniques**: Clustering algorithms, dimensionality reduction methods (e.g. PCA, t-SNE, UMAP, self-organizing maps)

**Interpretable ML & the future**: Interpreting machine learning models using SHAP (SHapley Additive exPlanations). Including uncertainties in ML models. The future of ML/AI, including the potential of transformers.


## Installation instructions

The dependencies for each supervised ML notebook can be quite complicated, and depend on the notebook itself.

The dependencies needed for the unsupervised ML notebooks are in `requirements.txt`. It is **strongly recommended** that you use a fresh virtual environment (or open each one on a cloud service like [Google Colab](https://colab.research.google.com/).)

After creating a virtual environment with the tool of your choice (e.g. with [venv](https://stackoverflow.com/questions/43069780/how-to-create-virtual-env-with-python3)), you can install them locally with pip via:

```pip install -r requirements.txt```

**Python 3.12 was used to develop this course. We recommend using the latest version of Python if possible - though (slightly) older versions should also be ok.**


## Other parts of the MWGaia-DN Coimbra doctoral school

You may also be interested in some of the other course materials from this summer school, which can also be found here on GitHub:

- [Astrostatistics (introduction, theory)](https://github.com/xluri/MWGaia-Astrostatistics-I)
- [Astrostatistics (Bayesian statistics, sampling)](https://github.com/mjuric/mwgaia-school-2024)
- [Introduction to working with large datasets and LSDB (Large Survey DataBase)](https://github.com/lincc-frameworks/MWGaia-DN_Introductory_School)
- [Visualisation](https://github.com/amoitinho/MWGaia-DN-Visualisation)
