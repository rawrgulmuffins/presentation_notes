# Practical Optimization for Stats Nerds (Ryan J. O'Niel)

## Minimizing Least Squares
* NOTE: This is easily the most dense talk I've ever seen but it was absolutely
fascinating.
* https://github.com/ryanjoneil/talks/blob/master/2017/03/data-science-dc/practical-optimization-for-stats-nerds.ipynb
* Solving least squares with scikitlearn
* cvxopt provides a qp method


```py
from bokeh.charts import Scatter, output_notebook, show
output_notebook()

    scatter = Scatter({'x': x, 'y': y}, width=750, height=400)
    show(scatter)
```

Well this is cool. The first example is an out of the box example that just
works for this form of regressions.

This next example is more general that will work for all quadratic models
instead of just our specific example.
```py
from bokeh.charts import show
y_hat = [beta[0]*xi**2 + beta[1]*xi + beta[2] for xi in x]
show(Line({'x': x, 'y': y_hat}, x='x', y='y', width=750, height=400))
```

* I'm not sure why you want to use SVM's instead of just a regular regression.

# Pandas, Pipelines, and Custom Transformations (Julie Michelman)
## Data Set
* Special events permits  from the city of seattle
* data.seattle.gov/Permitting/Special-Events-Permits/dm95-f8w5
* The goal of the talk is to make a Binary model about an event being complete
or not. Features are all columns in the dataset.
```py
from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df)
```

```py
from sklearn.linear_model import LogisticRegression
model = LogisticRegression() # No meta variables

model.fit(x_train, y_test)
p_baseline = [y_train.mean()] * len(y_test)
p_pred_test = model.predict_proba(x_test)[:, 1]
```

```py
from sklearn.metrics import roc_auc_score # Not sure what this means
```

## Transformations
* scikitlearn transformers vs estimators. Both of them have a fit method.
* A common transformation is `StandardScaler`. `fit` finds the mean, stadard
deviation of each. `transform` subtracts mean, then divide standard deviation.

```py
from sklearn.preprocessing import imputer, PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
        ("imputer", Imputer()),
        ("polynomial", PolynomialFeatures()),
        ("StandardScalar", StandardScalar()),])
```

* zack Stuart blog post about scikitlearn pipelines

## Example Pipeline
```py
df_train.event_location_park.value_counts(dropna=False).head())
df_train.attendance.isnull().sum()
x = df_train.attendance
```

* Making a histogram of the attendance showed a large deviation.
* Choosing a log scale helped deal with those outliers.

* **NOTE: One of my goals for next week is to recreate this talk on my own
without looking at her talk to learn from this.**

```py
from sklearn.base import TransformerMixin
class Log1pTransformer(TransformerMixin):

    def fit(self, x, y=None):
        return self


from sklearn.feature_extraction import DictVectorizer
class DummyTransformer(TransformerMixin):

    def fit(self, x, y=None):
        XDict = x.to_dict("records")
        self.dv = DictVectorizer(
        # TODO: fill this in

    def transform(self, x):
        Xdict= x.to_dict("records")
        # TODO: fill this in
```

## Pandas vs scikit-learn
* Pandas supports many data types, allows missing, and Labels rows and columns
* scikit-learn has very limited types, doesn't allow nulls, and strips labels.

* Pipelines are already pandas friendly. We can write scikitlearn transformers
to return pandas DataFrames

```py
class DFStandardScalar(
# TODO: Fill this in to remember what this does
```

* **NOTE: Look up AUC**
* zacsteward.com/2014/08/05/pipelines-of-flatureunions-of-pipelines.html
* github.com/jem1031/pandas-pipelines-custom-transformers
* This was an excellent talk.

# Thursday Keynote (Jake Vanderplas)
* 'The making of Python' - Guido Van Rossum
* 'Scientific Computing with Python' - David Beazley ACM vol. 216, 2000
* 'I had a hodge-podge of work processes. I would have Perl scripts that called
c++ numerica routines that would dump data files, and I would load them into
Matlab to plot them ... ' - John Hunter
* Fernando Perez creator of IPython
* jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions
* for loops over large data arrays, think about vectorizations in Numpy
* Bokeh, Plotly
* Look up ggplot
* Numba? This is a python to llvm transpiler
* emcc (mc package) Monte carlo simulations
* 

# Batch and Streaming Processing in the World of Data Engineering and Data Science (Keira Zhou)
## Online vs batch processing
* Online algrithms are computationally much faster
* Useful when dataset is too big
* adapt to new trend faster
vs
* Majority of algorithms only work in batch processing
* Some feature extraction is slow

## Streaming Pipeline
Kafka -> spark streaming -> redis -> flask
* Event time vs processing time. The closer event time and processing time are
the more "real time" your system is.
* You need to balance time-agnostic vs event times matters
* 
