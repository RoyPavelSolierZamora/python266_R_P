import numpy as np
import seaborn as sb
import pandas as pd
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf



import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from pmdarima.arima import auto_arima


pib_data = read_csv('C:/Users/PC/OneDrive - Universidad Antonio Ruiz de Montoya/UARM/ECONOMIA Y GESTION AMBIENTAL/CURSOS 2024-I Ciclo 7 (Intercambio)/Econometria III/Semana 10/pib.csv', header=0, index_col=0)
pib_data.plot()
pyplot.show()

pib_data.head()

#Make sure there are no null values
pib_data.isnull().value_counts()
#Check the datatypes
print(pib_data.dtypes)
#Convert the month column to datetime
pd.to_datetime(pib_data['t'])

pib_data.dtypes
pib_data.head()
plt.figure(figsize=(12,8))
sns.lineplot(data=pib_data, x='t', y= 'Yt')
#Set the index of the Month 
pib_data.set_index('t',inplace=True)
#Testing for stationarity
from pmdarima.arima import ADFTest
adf_test = ADFTest(alpha = 0.05)
adf_test.should_diff(pib_data)


#Spliting the dataset into train and test
train = pib_data[:158]
test = pib_data[-8:]

train.tail()
test.head()
plt.figure(figsize=(12,8))
plt.plot(train)
plt.plot(test)
plt.xlabel('Year')
plt.ylabel('yt')


arima_model =  auto_arima(train,start_p=0, d=1, start_q=0, 
                          max_p=5, max_d=5, max_q=5, start_P=0, 
                          D=0, start_Q=0, max_P=5, max_D=5,
                          max_Q=5, m=4, seasonal=True, 
                          error_action='ignore',trace = True,
                          supress_warnings=True,stepwise = True,
                          random_state=20,n_fits = 50 )

auto_arima
arima_model.summary()
prediction = pd.DataFrame(arima_model.predict(n_periods = 8),index=test.index)
prediction.columns = ['predicted_yt']
prediction

plt.figure(figsize=(12,8))
plt.plot(train,label="Training")
plt.plot(test,label="Test")
plt.plot(prediction,label="Predicted")
plt.legend(loc = 'best')
plt.show()

arima_model.plot_diagnostics(figsize=(14,10))
plt.show()