<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/luca-martinelli-09/learn-the-art">
    <img src="https://i.postimg.cc/P5m5r2sX/cat-no-bg.png" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center">Learn The Art and Put It Apart</h1>

  <p align="center">
    Transferability of Adversarial Attacks over different Datasets
    <br />
    <a href=""><strong>Paper in progress »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MarcoAlecci">Marco Alecci</a>
    ·
    <a href="https://github.com/FrancescoMarchiori">Francesco Marchiori</a>
    ·
    <a href="https://github.com/luca-martinelli-09">Luca Martinelli</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#abstract">Abstract</a>
    </li>
    <li>
      <a href="#datasets">Datasets</a>
    </li>
    <li>
      <a href="#trainer">Model Trainer</a>
    </li>
    <li>
      <a href="#attacks">Attacks</a>
      <ul>
        <li><a href="#mathattacks">Mathematical Attacks</a></li>
        <li><a href="#nonmathattacks">Non Mathematical Attacks</a></li>
      </ul>
    </li>
    <li>
      <a href="#eval">Model Evaluation</a>
    </li>
    <li>
      <a href="#plots">Plot Creation</a>
    </li>
    <li>
      <a href="#run">Run It Yourself</a>
    </li>
    <li>
      <a href="#cases">Cases</a>
    </li>
  </ol>
</details>

<div id="abstract"></div>

## 🧩 Abstract

The increasing popularity of Deep Learning employed in the Image Classification task opened a whole new branch of research on Adversarial Attacks, i.e., perturbations applicable to an image in order to have it misclassified by a model. In literature it’s possible to find different kinds of adversarial attacks which are able to fool almost any stateof- the-art neural network, highlighting the importance of this vulnerability. However, in most experimental settings datasets are too simple and fail to accurately represent realistic scenarios in which Deep Learning models could be deployed. In our work, we study the effect of these attacks on more realistic datasets than the one considered in literature. We study the transferability of some adversarial attacks, namely if perturbations computed on one model allow for the disruption of another unseen architecture. The results of our attacks show that basic filters and simple modifications of the image are more transferable and more effective than carefully crafted attacks. We highlight how the manual creation of a dataset is needed in order to have a full insight of the success rate of an attack rather than using a more simple one like MNIST or CIFAR-10. Finally we show that imbalances in the classes of the datasets used for training and attack generation don’t affect the F1-score of the model or the success rate of the attack.

<div id="datasets"></div>

## 📚 Datasets

We created our own datasets by downloading images of cats and dogs from different sources (Bing, Google and DuckDuckGo). All images are then processed in order to be 300x300 in RGB using PIL. Images for each class are then sorted in the following format:
* **Trainig Set**: 3500 images
* **Validation Set**: 500 images
* **Test Set**: 1000 images

<p align="right"><a href="#top">(back to top)</a></p>

<div id="trainer"></div>

## 💪🏽 Model Trainer

This function allows to train different models with different parameters. You can choose from the markdown tab in Colab the pre-trained model that you want, or you can choose our own model built from scratch. Most importantly, it lets you pick:
* The dataset on which the model will be trained
* The level of imbalance of the classes (e.g., percentage of cat/dog images over all the training images)
* Whether to perform fine tuning or feature extraction of pre-trained models

<p align="right"><a href="#top">(back to top)</a></p>

<div id="attacks"></div>

## ⚔️ Attacks

We divided attacks in two major categories.

<div id="mathattacks"></div>

### 🔢 Mathematical Attacks

These are the "classical" adversarial attacks, which in particular are:

|          Name          | Paper                                                        |
| :--------------------: | ------------------------------------------------------------ |
|  **FGSM**<br />(Linf)  | Explaining and harnessing adversarial examples ([Goodfellow et al., 2014](https://arxiv.org/abs/1412.6572)) |
|    **CW**<br />(L2)    | Towards Evaluating the Robustness of Neural Networks ([Carlini et al., 2016](https://arxiv.org/abs/1608.04644)) |
| **FAB**<br />(Linf, L2, L1) | Minimally distorted Adversarial Examples with a Fast Adaptive Boundary Attack ([Croce et al., 2019](https://arxiv.org/abs/1907.02044)) |
| **DeepFool**<br />(L2) | DeepFool: A Simple and Accurate Method to Fool Deep Neural Networks ([Moosavi-Dezfooli et al., 2016](https://arxiv.org/abs/1511.04599)) |
| **DIFGSM**<br />(Linf) | Improving Transferability of Adversarial Examples with Input Diversity ([Xie et al., 2019](https://arxiv.org/abs/1803.06978)) |

They are generated using [Torchattacks](https://github.com/Harry24k/adversarial-attacks-pytorch) with the pre-defined parameters used in the same dataset of the pre-training of our models.

#### :hammer: Installation

```
pip install torchattacks
```

<div id="nonmathattacks"></div>

### 🎨 Non Mathematical Attacks

These are just visual modifications of the image obtained through filters or other means using the PIL library. They appear to be more transferable and easy to generate since they are not based on any form of norm distance.

![Non Mathematical Attacks](/plots_creation/plots/png/catNonMathAttacks.jpg?raw=true "Non Mathematical Attacks")

<p align="right"><a href="#top">(back to top)</a></p>

<div id="eval"></div>

## 📋 Model Evaluation

With `modelEvaluator.ipynb` you see how much the attacks are effective on all the models. Any attack dataset (mathematical and non mathematical) is used as a test set in any of the models (with every imbalance level), so computation is quite time consuming. Results are then saved in the `results` folder.

<div id="plots"></div>

### 📊 Plot Creation

Plots are created in order to visualize different results. Since we have a huge amount of data to process and different results to show, we build different histograms with a focus on differences between models or datasets.

![RQ Example](/plots_creation/plots/png/rq1_variant.jpg?raw=true "RQ Example")

<p align="right"><a href="#top">(back to top)</a></p>

<div id="run"></div>

## 🏃🏽 Run it Yourself

Model Trainer [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luca-martinelli-09/learn-the-art/blob/main/modelTrainer.ipynb)

Adversarial Samples Generator [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luca-martinelli-09/learn-the-art/blob/main/adversarialSamplesGenerator.ipynb)

Model Evaluator [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luca-martinelli-09/learn-the-art/blob/main/modelEvaluator.ipynb)

<p align="right"><a href="#top">(back to top)</a></p>

<div id="cases"></div>

## 📌 Cases

```
x = {M, D, B}

0: x_{src} != x_{trg}
1: x_{src} = x_{trg}
```

| Case # | M | D | B |
|--------|---|---|---|
| C1     | 0 | 0 | 0 |
| C2     | 0 | 0 | 1 |
| C3     | 0 | 1 | 0 |
| C4     | 0 | 1 | 1 |
| C5     | 1 | 0 | 0 |
| C6     | 1 | 0 | 1 |
| C7     | 1 | 1 | 0 |
| C8     | 1 | 1 | 1 |

<p align="right"><a href="#top">(back to top)</a></p>