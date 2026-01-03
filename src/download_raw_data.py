"""
TAKE CLEAN DATA -> LOAD INTO POSGRESQL
"""



import yfinance as yf
import numpy as np
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
import os
from datetime import datetime

import preprocess_raw_data
    
def prep_df_for_sql(df):
    
    df.index_name = "timestamp"
    df_sql = df.reset_index()

    
    return True
    
def download_data_as_postgressql(df):
    
    engine = create_engine(
        f"postgresql+psycopg2://{os.environ['PG_USER']}:"
        f"{os.environ['PG_PASSWORD']}@"
        f"{os.environ['PG_HOST']}:"
        f"{os.environ['PG_PORT']}/"
        f"{os.environ['PG_DB']}",
        pool_pre_ping=True
    )    

    # df.to_sql(f'{ticker}_table', engine)
   
    return True

def verify_download():
    
    return True


def download_raw_data(ticker):
    
    df = preprocess_raw_data.preprocess_data(ticker)
    
    
    print(df)
    
    return

"""
==========================================
Testing Section
"""
if __name__ == "__main__":
    
    
    download_raw_data("^SPX")
    
    print("TESTING COMPLETE")
    
    


    
    

    