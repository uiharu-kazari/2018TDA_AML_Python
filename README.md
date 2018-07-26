# HDBSCAN and 3D-plotting for AML's PCL data


# **See item 4 for remarks on plots and data.**

## Tutorial(if needed)

### 1.Install required packages
Make sure that you are using python3,
and install the follwing packages:
* numpy
* sklearn
* pandas
* hdbscan  ([Documentation](http://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html))
* seaborn
* matplotlib
* warnings
* random

You may install the packages above by copying and pasting the following command to terminal and run:

_pip install numpy sklearn pandas hdbscan seaborn matplotlib warnings random_

Install and/or update all other packages if there were any prompts.

### 2.Run the following.py files in order:

1. hdbSCAN.py
2. E3ClusterP.py
3. 3dplotOutlier.py
4. demo.py

Where you will get the url of plots from the result of demo.py.

## 3.Plots
You may:

Take a look files Plot1.html and Plot2.html. Just drag the file into your browser. Use google chrome if it does not work.

Visit the following links:

[Clusters' coloring](https://plot.ly/~SakuraNene/12)

[Outliers' Plot](https://plot.ly/~SakuraNene/14)

Notice that the links are subjected to change.

I recommend registering your own **plotly** account and change the _username_ and *api_key* in the top of E3clusterP.py.

See [here](https://plot.ly/python/getting-started/#initialization-for-online-plotting) for reference.

## 4.Remarks on plot files and data
1. We performed hdbscan on the PCA components 1~3, then draw the labels accordingly as shown in Plot1.html. Data of labels and outlier scores is stored in *OnPCAData.csv*.

2. We performed hdbscan on the original 10k*48 Raw data(without any normalization), then draw the labels on the PCA data in 3D space, and get Plot3.html.
Data of the labels and outlier scored is stored in *OnRawData.csv*.

## 5.Futher Remark

tSNE.py contains the code for dimension reduction via t-distributed stochastic neighbor embedding method.
