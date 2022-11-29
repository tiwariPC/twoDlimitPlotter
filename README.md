# twoDlimitPlotter

To get the text file containing limits scaled to tanbeta values run

```python rescale.py```

However, you need csv file with the value of cross-sections (using scans in madgraph), an example of such file is int cross_section.

A limit file containing ```"expm2, expm1, exp, expp1, expp2, obs``` for all the mass points should be kept inside limitFiles.

After getting ```limits_tanb_vs_ma_scan.txt``` file, to get 2d plot, run

```python LimitContour.py```
