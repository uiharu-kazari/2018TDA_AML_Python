#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:09:20 2018

@author: cx513
"""
##Read in the PCA data.
PCA=pd.read_csv('PCA.csv')

PCA=PCA[['Comp.1','Comp.2','Comp.3']]

print(PCA.head())

#Perform hdbscan on the extracted 3D data.
CL1=hdbscanIntegration(PCA,min_cluster_size=30,min_samples=10);

print('\n')
print('We obtained '+str(len(set(CL1.labels_))-1)+' clusters via hdbscan.')
 
#Copy and paster the url to your browser for viewing.
#Notice the setting of samplingratio. Vary it to plot more or less points.
url1=plotly3dDrawCl(PCA.values,CL1,samplingratio=0.1)

#Copy and paster the url to your browser for viewing.
#Notice the setting of samplingratio. Vary it to plot more or less points.
url2=plotly3dDrawOutlier(PCA.values,CL1,99,samplingratio=0.3)

print('Links for your plots are shown below:')
print(url1)
print(url2)