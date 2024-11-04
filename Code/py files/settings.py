import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter
import seaborn as sns

# Used for setting the seed
import random

# Test-train split
from sklearn.model_selection import train_test_split

# Grid Search
from sklearn.model_selection import GridSearchCV

# Decision tree 
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree
from sklearn.tree import plot_tree

# KNN
from sklearn.neighbors import KNeighborsClassifier
import threadpoolctl # NEEDED FOR KNN TO WORK

# Logistic Regression 
import scikitplot as skplt
from sklearn.linear_model import LogisticRegressionCV

# Support Vector Classifier
from sklearn.svm import SVC

# Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Evaluation metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.inspection import permutation_importance

# pandas display options
# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options
pd.options.display.max_columns = 30 # default 20
pd.options.display.max_rows = 60 # default 60
pd.options.display.float_format = '{:.2f}'.format
# pd.options.display.precision = 2
pd.options.display.max_colwidth = 200 # default 50; -1 = all
# otherwise text between $ signs will be interpreted as formula and printed in italic
pd.set_option('display.html.use_mathjax', False)

# np.set_printoptions(edgeitems=3) # default 3

plot_params = {'figure.figsize': (12, 8), 
               'axes.labelsize': 'large',
               'axes.titlesize': 'large',
               'xtick.labelsize': 'large',
               'ytick.labelsize':'large',
               'figure.dpi': 100}
# adjust matplotlib defaults
import matplotlib
matplotlib.rcParams.update(plot_params)

sns.set_style("darkgrid")