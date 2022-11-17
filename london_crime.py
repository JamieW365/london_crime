import pandas as pd

def crime_per_pop(tots :pd.DataFrame,
                  pops: pd.DataFrame,
                  per: int = 1000) -> pd.DataFrame:

    '''
    Adjust yearly crime totals to be representative of changing borough populations
    '''

    for i, pop in pops.iterrows():

        ind = tots[tots['Borough'] == pop['Name']].index

        cols = [col for col in tots.columns if col.startswith(str(pops['Year']))]

        tots.loc[ind, cols] /= (pop['Population'] / per)

    return tots
