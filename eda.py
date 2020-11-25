
import matplotlib.pyplot as plt

# Check the data
test = housing.head()
housing.head()

housing.info()

housing["ocean_proximity"].value_counts()

test = housing.describe()

housing.hist(bins=50)