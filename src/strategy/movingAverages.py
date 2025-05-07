import numpy as np

#Funciones para calcular las medias moviles que queremos:
##Simple: Toma el precio de los ultimos {20} sesiones, entonces solo contara esos {20} dias.
##Exponencial: Da mas peso en los dias mas cercanos, el dia de ayer es mas importante que el dia que comenzo.
##Acomulativa: 
def simple_moving_average(price, data_window = 20):
    return price.rolling(window = data_window).mean()

def exponential_moving_average(price, data_com = 0.5):
    return price.ewm(com = data_com).mean()

def comulative_moving_average(price, min_periods = 2):
    return price.expanding(min_periods).sum()

#Esta funcon calcula las MAs y despues busca si produce algun cruce
#dorado o algun cruce de la muerte:
def golden_death_crosses(price, plt, mean_type = "simple", mean = (50, 200)):

    #En funcion del tipo de medias que queremos usar, las calculamos:
    if mean_type == "simple":
        #moving average = ma
        ma_short = simple_moving_average(price, mean[0])
        ma_short = ma_short[~np.isnan(ma_short)]

        ma_long = simple_moving_average(price, mean[1])
        ma_long = ma_long[~np.isnan(ma_long)]

    if mean_type == "exponential":
        #moving average = ma
        ma_short = exponential_moving_average(price)
        ma_short = ma_short[~np.isnan(ma_short)]

        ma_long = exponential_moving_average(price)
        ma_long = ma_long[~np.isnan(ma_long)]

    if mean_type == "comulative":
        #moving average = ma
        ma_short = comulative_moving_average(price, mean[0])
        ma_short = ma_short[~np.isnan(ma_short)]

        ma_long = comulative_moving_average(price, mean[1])
        ma_long = ma_long[~np.isnan(ma_long)]

    ma_short_date = ma_short.index
    ma_long_date = ma_long.index

    mask = (ma_short_date > ma_long_date[0]) & (ma_short_date <= ma_long_date[-1])
    ma_short = ma_short.loc[mask]

    golden_cross = []
    for i_sma in range(1, len(ma_short) -1):
        if ma_short[i_sma -1] < ma_long[i_sma -1 ] and ma_short[i_sma] and ma_short[i_sma +1] > ma_long[i_sma]
