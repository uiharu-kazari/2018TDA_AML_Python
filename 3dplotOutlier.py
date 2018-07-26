#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:45:18 2018

@author: cx513
"""

from E3ClusterP import irohyoten


def plotly3dDrawOutlier(inputdata,clusterer,percen,samplingratio=1):
    """
    Plot the point cloud and mark the outliers with color
    """
    labels=clusterer.labels_
    labelset=set(labels)
    plottingdata=[]
    index=np.array(range(len(inputdata)))+1
    ##Create color assignment
    color_palette=[sns.color_palette("hls", 8)[0]]
    #data with label -1 will be assigned
    #color (0.5,0.5,0.5), which corresponds to grey
    threshold=np.percentile(clusterer.outlier_scores_,percen)
    colorlist = [color_palette[0] if ol >= threshold
                  else (0.9, 0.9, 0.9)
                  for ol in clusterer.outlier_scores_]
    colorlist=irohyoten(colorlist)
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
                    opacity= 0.5
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