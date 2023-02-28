# API for the Materials Properties Prediction (MAPP) project

![alt text](https://github.com/qjhong/mapp_api/blob/1ac350474bb49f57128f6fa27aef97b27d0206d3/MAPP.png "MAPP")

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
