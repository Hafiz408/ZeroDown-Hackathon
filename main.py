import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('C:/Users/hp/Downloads/weekly_market_2017_2022.tsv', sep='\t')

remove_columns=df.columns[df.isnull().mean()>0.4]
df1=df.drop(remove_columns,axis=1)

filtered_columns=['region_name', 'region_type','period_begin', 'period_end','duration',
       'average_homes_sold', 'average_homes_sold_yoy',
       'percent_homes_sold_with_price_drops','percent_homes_sold_with_price_drops_yoy', 
       'median_sale_price','median_sale_price_yoy',
       'median_sale_ppsf', 'median_sale_ppsf_yoy',
       'median_days_to_close', 'median_days_to_close_yoy',
       'price_drops',
       'pending_sales', 'pending_sales_yoy',
       'median_pending_sqft', 'median_pending_sqft_yoy',
       'average_new_listings','average_new_listings_yoy', 
       'median_new_listing_price','median_new_listing_price_yoy',
       'median_new_listing_ppsf', 'median_new_listing_ppsf_yoy',
       'inventory', 'inventory_yoy',
       'active_listings','active_listings_yoy',
       'age_of_inventory', 'age_of_inventory_yoy',
       'median_active_list_price', 'median_active_list_price_yoy',
       'median_active_list_ppsf', 'median_active_list_ppsf_yoy',
       'average_sale_to_list_ratio', 'average_sale_to_list_ratio_yoy',
       'median_days_on_market', 'median_days_on_market_yoy',
       'pending_sales_to_sales_ratio', 'pending_sales_to_sales_ratio_yoy']
df1=df1[filtered_columns]

df1["year"]=[x.split('-')[0] for x in df1["period_begin"]]
df1["month"]=[x.split('-')[1] for x in df1["period_begin"]]

df1.drop(["period_begin","period_end"],axis=1,inplace=True)

cols=df1.columns[df1.isnull().any()]
for col in cols:
  df1[col].fillna(df1[col].mean(),inplace=True)

df1["state"]=[x.split(',')[-1] for x in df1["region_name"]]
for i in range(len(df1)):
  l=df1.iloc[i]['state'].split(' ')
  if len(l)>2:
    df1.at[i,'state']=l[1]
  df1.at[i,'state']=df1.at[i,'state'].strip()

df1.to_csv('US_housing_market_processed.csv')