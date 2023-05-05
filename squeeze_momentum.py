def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 

def moving_min (array, period ):

    moving_min = np.empty_like(array)
    moving_min = np.full( moving_min.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_min[i-1] = np.min(array[i-period:i] , dtype=np.float16 )
    return moving_min

def moving_max (array, period ):

    moving_max = np.empty_like(array)
    moving_max = np.full( moving_max.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_max[i-1] = np.max(array[i-period:i] , dtype=np.float16 )
    return moving_max     

def linear_reg_slope(array = mean_deviation, period = lengthKC):
  slope = np.zeros_like(array)
  
  x = np.arange(lengthKC) 
  for i in range(period , len(array) )
    slope[i] = np.polyfit( x ,  array[i-period: i ] , 1 )[0]

  return slope  
  
basis = sma(source, length)
dev = mult * stdev(source, length)
upperBB = basis + dev
lowerBB = basis - dev

# Calculate KC
ma = sma(source, lengthKC)
# range = useTrueRange and tr(h, l, source) or (h - l) 
# rangema = sma(range, lengthKC) 
upperKC = ma + rangema * multKC
lowerKC = ma - rangema * multKC

# Calculate squeeze
sqzOn = np.logical_and(lowerBB > lowerKC, upperBB < upperKC)
sqzOff = np.logical_and(lowerBB < lowerKC, upperBB > upperKC)
noSqz = np.logical_not(np.logical_or(sqzOn, sqzOff))

mean_deviation = close -  ( mean ( mean( moving_max( h, lengthKC ) , moving_min( l, lengthKC  ) ) , sma(source , lengthKC) ) ) 

slope =  linear_reg_slope(array = mean_deviation, period = lengthKC)  # 

lagging_slope = sma(slope , 5) 
