# API for the Materials Properties Prediction (MAPP) project

![alt text](https://github.com/qjhong/mapp_api/blob/c4ce2cd77af756e3e75c363d89594347a9181d1a/MAPP.png "MAPP")

## Melting temperature prediction in seconds!

Follow these simple steps:
1. Edit the file "chemical_formula.csv" to include all chemical formula. The upper limit of entries is 10,000. Read the file for examples.
2. Run python code.
```python
python mapp_mp.py
```
3. Find the melting temperature predictions in "output.csv". Read the file for examples.

## Speed test

Number of entries                          |Time [seconds]                         |
-------------------------------|-----------------------------|
10                            |7         |
1,000                           |34         |
10,000|303|

## Cite this project:

<p>Si-Da Xue and Qi-Jun Hong, Materials Properties Prediction (MAPP): Empowering the Prediction of Material Properties Solely Based on Chemical Formulas, Materials, 2024. <a href="https://doi.org/10.3390/ma17174176"> Download</a>. </p>
<p>Qi-Jun Hong, A melting temperature database and a neural network model for melting temperature prediction, arXiv, 2021. <a href="https://arxiv.org/abs/2110.10748"> Download</a>. </p>
<p>Qi-Jun Hong, Sergey V Ushakov, Axel van de Walle, and Alexandra Navrotsky, Melting temperature prediction using a graph neural network model: From ancient minerals to new materials, PNAS, 2022. <a href="https://doi.org/10.1073/pnas.2209630119"> Download</a>. </p>
