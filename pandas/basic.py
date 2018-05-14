# 
# author gino
# created on 2018/5/14
import logging
from logging.config import fileConfig

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(pd.__version__)

fileConfig('logging_config.ini')
logger = logging.getLogger(__name__)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])


def log_info(message):
    logger.info("\n%s", message)


def create_dataframe():
    data_frame = pd.DataFrame({'City name': city_names, 'Population': population})
    log_info('data frame: \n%s' % data_frame)

    log_info(type(data_frame['City name']))
    log_info(data_frame['City name'])

    log_info(type(data_frame['City name'][1]))
    log_info(data_frame['City name'][1])

    log_info(type(data_frame[0:2]))
    log_info(data_frame[0:2])


def read_csv():
    california_housing_dataframe = pd.read_csv('./california_housing_train.csv', sep=",")
    log_info(california_housing_dataframe)
    describe = california_housing_dataframe.describe()
    log_info(describe)
    log_info(california_housing_dataframe.head())
    california_housing_dataframe.hist('housing_median_age')
    plt.show()


def controller_data():
    log_info(population / 1000)
    log_info(np.log(population))
    log_info(population.apply(lambda val: val > 1000000))

    data_frame = pd.DataFrame({'City name': city_names, 'Population': population})
    data_frame['Area square miles']=pd.Series([46.87, 176.53, 97.92])
    data_frame['Population density'] = data_frame['Population'] / data_frame['Area square miles']
    log_info(data_frame)

    data_frame['Is wide and has saint name'] = (data_frame['Area square miles'] > 50) & data_frame['City name'].apply(lambda name: name.startswith('San'))
    log_info(data_frame)
    log_info(data_frame.reindex(np.random.permutation(data_frame.index)))
    log_info(data_frame.reindex([0, 4, 5, 2]))


if __name__ == '__main__':
    create_dataframe()
    read_csv()
    controller_data()
