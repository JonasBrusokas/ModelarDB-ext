from utils import *

import pandas as pd

forecasting_csv_path_string = f"{os.path.join(FileUtils.project_root_dir(), 'results', 'forecasting_results', 'combined', 'combined_10-19.csv')}"
compression_csv_path_string = f"{os.path.join(FileUtils.project_root_dir(), 'results', 'compression_details', 'output.csv')}"

#%%
# Compression CSV
compression_df = pd.read_csv(compression_csv_path_string)
compression_df = compression_df.rename({'name': 'dataset_name'}, axis=1)
compression_df.loc[ compression_df['dataset_name'] == 'raw', 'error_bound' ] = -1

#%%
# Forecasting CSV

forecasting_df = pd.read_csv(forecasting_csv_path_string)
proper_forecasting_df = forecasting_df[forecasting_df['model_type'] != 'lstm']
proper_forecasting_df = proper_forecasting_df[['dataset_name', 'model_type', 'error_bound', 'train_rmse', 'rmse', 'rmse_on_raw']]

# Renaming dataset_name to 'raw' when the error_bound is -1
proper_forecasting_df.loc[ proper_forecasting_df['error_bound'] == -1, 'dataset_name' ] = 'raw'

# Averaging over RAW cases
proper_forecasting_raw_df = proper_forecasting_df[proper_forecasting_df['dataset_name'] == 'raw']\
    .groupby('model_type').mean()
proper_forecasting_raw_df = proper_forecasting_raw_df.reset_index()
proper_forecasting_raw_df['dataset_name'] = 'raw'
proper_forecasting_raw_df

# Removing the error_bound -1 cases from proper_forecasting_df
proper_forecasting_df = proper_forecasting_df[ proper_forecasting_df['error_bound'] != -1]

# Combining these two datasets into a combined one
proper_forecasting_df = pd.concat([proper_forecasting_df, proper_forecasting_raw_df])

#%%
# Rename values (on forecasting_df)
# pmc_only -> pmc
# lg_only -> lost_gorilla_v1
# lost_gorilla_v3_d* -> lg_v3_d*

print(f"dataset_name from forecasting_df: {ListUtils.natural_sort(list(proper_forecasting_df['dataset_name'].unique()))}")
print(f"dataset_name from compression_df: {ListUtils.natural_sort(list(compression_df['dataset_name'].unique()))}")
print()


renamed_proper_forecasting_df = proper_forecasting_df.copy()

# TODO: make this rename
renamed_proper_forecasting_df.loc[renamed_proper_forecasting_df['dataset_name'] == 'pmc_only', 'dataset_name'] = 'pmc'
renamed_proper_forecasting_df.loc[renamed_proper_forecasting_df['dataset_name'] == 'lg_only', 'dataset_name'] = 'lost_gorilla_v1'
renamed_proper_forecasting_df.loc[renamed_proper_forecasting_df['dataset_name'] == 'lg_v3_d5', 'dataset_name'] = 'lost_gorilla_v3_d5'
renamed_proper_forecasting_df.loc[renamed_proper_forecasting_df['dataset_name'] == 'lg_v3_d10', 'dataset_name'] = 'lost_gorilla_v3_d10'
renamed_proper_forecasting_df.loc[renamed_proper_forecasting_df['dataset_name'] == 'lg_v3_d25', 'dataset_name'] = 'lost_gorilla_v3_d25'


print(f"Columns from renamed forecasting_df: {ListUtils.natural_sort(list(renamed_proper_forecasting_df.columns))}")
print(f"Columns from compression_df: {ListUtils.natural_sort(list(compression_df.columns))}")

renamed_proper_forecasting_df_dataset_names = ListUtils.natural_sort(list(renamed_proper_forecasting_df['dataset_name'].unique()))
print(f"dataset_name from renamed forecasting_df: {renamed_proper_forecasting_df_dataset_names}")
compression_df_dataset_names = ListUtils.natural_sort(list(compression_df['dataset_name'].unique()))
print(f"dataset_name from compression_df: {compression_df_dataset_names}")

print(f"Dataset names are equal: {set(renamed_proper_forecasting_df_dataset_names) == set(compression_df_dataset_names)}")

#%%
# Combining tables

joined_df = renamed_proper_forecasting_df.merge(compression_df,
                                   on=['dataset_name', 'error_bound'],
                                   how='outer')
print(f"Number of NaN values in joined_df: {joined_df.isnull().values.sum()}")

#%%
# Saving tables in separate files
final_results_folder = os.path.join(FileUtils.project_root_dir(), 'results', 'final_results')
FileUtils.create_dir(final_results_folder)

renamed_proper_forecasting_df.to_csv(os.path.join(final_results_folder, 'forecasting_results.csv'), header=True, index=False)
compression_df.to_csv(os.path.join(final_results_folder, 'compression_results.csv'), header=True, index=False)
joined_df.to_csv(os.path.join(final_results_folder, 'joined_results.csv'), header=True, index=False)


#%%
# TODOs
"""
- Make renaming work (unify the names) --- V
- Join those tables --- V
- Save all three (separate_1, _2, combined) dataframes in a folder

- Make a list of charts worth plotting
- Create a .ipynb notebook
- Plot the charts 
"""
