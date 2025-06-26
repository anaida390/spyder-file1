# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 20:23:02 2025

@author: Admin
"""

import os
import pandas as pd
import numpy as  np
df1=pd.read_csv("Stock_File_1.csv")
df2=pd.read_csv("Stock_File_2.txt") 
merged_df=pd.concat([df1,df2],ignore_index=True)
print(merged_df)

merged_df=merged_df.drop_duplicates()
merged_df.dropna(axis=0,inplace=True) #to remove nan











# Option E: Impute Missing Values (Fill in instead of removing)
# This is often preferred over simply dropping data, as it retains more information.

# Fill with a specific value (e.g., 0) 
df_filled_zero = merged_df.fillna(0)
print("\n--- After filling missing values with 0 ---")
print(df_filled_zero.isnull().sum())

# Fill with the mean of the column (for numerical columns)
# This is a common imputation strategy.
df_filled_mean = merged_df.fillna(merged_df.mean(numeric_only=True))
print("\n--- After filling numeric missing values with column mean ---")
print(df_filled_mean.isnull().sum())

# Fill with the median of the column (for numerical columns)
df_filled_median = merged_df.fillna(merged_df.median(numeric_only=True))
print("\n--- After filling numeric missing values with column median ---")
print(df_filled_median.isnull().sum())

# Forward fill (propagates the last valid observation forward)
df_ffill = merged_df.fillna(method='ffill')
print("\n--- After forward filling missing values ---")
print(df_ffill.isnull().sum())

# Backward fill (propagates the next valid observation backward)
df_bfill = merged_df.fillna(method='bfill')
print("\n--- After backward filling missing values ---")
print(df_bfill.isnull().sum())

# You can combine imputation methods or apply them to specific columns:
# merged_df['NumericColumn'].fillna(merged_df['NumericColumn'].mean(), inplace=True)
# merged_df['CategoricalColumn'].fillna('Unknown', inplace=True)

# --- 4. Save the cleaned DataFrame (if desired) ---
# df_cleaned = df_dropped_rows # Or whichever cleaning method you chose
# output_file_path = "C:/Users/Admin/spyder-py3/cleaned_merged_data.csv"
# df_cleaned.to_csv(output_file_path, index=False) # index=False prevents writing the DataFrame index as a column
# print(f"\nCleaned data saved to: {output_file_path}")



# --- 2. Ensure your date column is in datetime format first ---
# This step is crucial. If it's not already datetime, convert it.
# Replace 'Your_Date_Column' with the actual name of your date column.
merged_df['Date'] = pd.to_datetime(merged_df['Date'], errors='coerce')

# Handle any NaT values that might have resulted from 'errors='coerce'' if necessary.
# For example, to drop rows with invalid dates:
# merged_df.dropna(subset=['Your_Date_Column'], inplace=True)


# --- 3. Convert to 'YYYY-MM-DD' string format ---
# We use the .dt accessor and strftime() method.
# %Y: 4-digit year (e.g., 2025)
# %m: Month as zero-padded decimal (01-12)
# %d: Day of the month as zero-padded decimal (01-31)

merged_df['Formatted_Date'] = merged_df['Date'].dt.strftime('%Y-%m-%d')

# You can also overwrite the original column if you no longer need the datetime object:
# merged_df['Your_Date_Column'] = merged_df['Your_Date_Column'].dt.strftime('%Y-%m-%d')

print("\n--- DataFrame with 'YYYY-MM-DD' formatted date column ---")
print(merged_df[['Date', 'Formatted_Date']].head()) # Show original datetime and new string column
print("\nData type of 'Formatted_Date' column:", merged_df['Formatted_Date'].dtype)

# --- 4. (Optional) Save the DataFrame with the new format ---
# output_file_path = "C:/Users/Admin/spyder-py3/data_with_formatted_date.csv"
# merged_df.to_csv(output_file_path, index=False)
# print(f"\nData with formatted date saved to: {output_file_path}")
















