#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:11:23 2018

@author: cx513
"""


import plotly

####IMPORTANT
####IMPORTANT
#Remember to change the following code line to your own plotly account's
#API key, if you want to save it in your plotly acccount.
#See the link below:
#https://plot.ly/python/getting-started/#initialization-for-online-plotting
plotly.tools.set_credentials_file(username='SakuraNene',\
                                  api_key='WEKEAwn7bugQ7HGjVhXL')
import plotly.plotly as py
import plotly.graph_objs as go
import warnings
import random
import numpy as np

#class DimensionIncompatibleWarning(UserWarning):
#    pass

#Create a new exception
class DimensionError(Exception):
    pass

#Auxilary function for creating color values
def NarrtoStr(array):
        return str(round(array[0]))+\
                ','+str(round(array[1]))+\
                ','+str(round(array[2]))

#Another auxilary function for creating color values
def irohyoten(ColorList):
    npa=np.array(ColorList)
    npa=npa*255
    result=[]
    for i in range(len(npa)):
        temp='rgb('+NarrtoStr(npa[i])+')'
        result.append(temp)
    return np.array(result)


def plotly3dDrawCl(inputdata,clusterer,samplingratio=1):
    """
    Three dimensional plotting with cluster information.
    samplingratio performs random stratified sampling in order
    to lessen the number of points being drawn.
    """
    labels=clusterer.labels_
    labelset=set(labels)
    plottingdata=[]
    index=np.array(range(len(inputdata)))+1
    ##Create color assignment
    color_palette=sns.color_palette('Paired', len(labelset))
    #data with label -1 will be assigned
    #color (0.5,0.5,0.5), which corresponds to grey 
    cluster_colors = [color_palette[x] if x >= 0
                  else (0.5, 0.5, 0.5)
                  for x in labels]
    cluster_member_colors = [sns.desaturate(x, p) for x, p in
                         zip(cluster_colors, clusterer.probabilities_)]
    #Change color parameters from 0~1 to 0~255
    colorlist=irohyoten(cluster_member_colors)
    #Start to creat stratified plotting data
    for i in labelset:
        sliced=inputdata[labels==i]
        length=len(sliced)
        colorsliced=colorlist[labels==i]
        indexsliced=index[labels==i]
        draw=random.sample(range(length),int(length*samplingratio))
        trace0= go.Scatter3d(
                x= sliced[draw,0],
                y= sliced[draw,1],
                z= sliced[draw,2],
                mode= 'markers',
                ##You may change the size of drawing sphere
                ##and its opacity here.
                marker= dict(size= 3,
                    line= dict(width=1),
                    color= colorsliced[draw],
                    opacity= 0.6
                   ),
                #name is the same for all points in this loop
                name= 'cluster'+str(i),
                #text is an array of size sliced
                text= index[labels==i][draw]
                ) # The hover text goes here... 
        plottingdata.append(trace0);
    #Configure the layout
    layout = go.Layout(margin=dict(l=0,r=0,b=0,t=0))
     
    fig= go.Figure(data=plottingdata, layout=layout)
    output=py.plot(fig, auto_open=False)
    return output    