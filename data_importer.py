import pandas


def get_dataset():
	url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
	names = ['sepal_length','sepal_width','petal_length','petal_width', 'class']
	dataset = pandas.read_csv(url, names=names)
	return dataset
