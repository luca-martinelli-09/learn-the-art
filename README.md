<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/luca-martinelli-09/orco-gan">
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

## Abstract

The increasing popularity of Deep Learning employed in the Image Classification task opened a whole new branch of research on Adversarial Attacks, i.e., perturbations applicable to an image in order to have it misclassified by a model. In literature it’s possible to find different kinds of adversarial attacks which are able to fool almost any stateof- the-art neural network, highlighting the importance of this vulnerability. However, in most experimental settings datasets are too simple and fail to accurately represent realistic scenarios in which Deep Learning models could be deployed. In our work, we study the effect of these attacks on more realistic datasets than the one considered in literature. We study the transferability of some adversarial attacks, namely if perturbations computed on one model allow for the disruption of another unseen architecture. The results of our attacks show that basic filters and simple modifications of the image are more transferable and more effective than carefully crafted attacks. We highlight how the manual creation of a dataset is needed in order to have a full insight of the success rate of an attack rather than using a more simple one like MNIST or CIFAR-10. Finally we show that imbalances in the classes of the datasets used for training and attack generation don’t affect the F1-score of the model or the success rate of the attack.

## Run it Yourself

Model Trainer [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luca-martinelli-09/orco-gan/blob/main/modelTrainer.ipynb)

Adversarial Samples Generator [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luca-martinelli-09/orco-gan/blob/main/adversarialSamplesGenerator.ipynb)

Model Evaluator [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luca-martinelli-09/orco-gan/blob/main/modelEvaluator.ipynb)

## Cases
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