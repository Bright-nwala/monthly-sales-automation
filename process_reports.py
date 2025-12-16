import pandas as pd
import os

def clean_and_merge_reports(folder="downloads"):
    all_files = [f for f in os.listdir(folder) if f.endswith(".xlsx")]

    dataframes = []
    for file in all_files:
        df = pd.read_excel(os.path.join(folder, file))

        # SIMPLE CLEANING RULES
        df.columns = df.columns.str.strip().str.title()  # normalize column names
        df.dropna(how='all', inplace=True)               # remove empty rows
        df['Outlet'] = file.split('_')[0].upper()        # Add outlet name

        dataframes.append(df)

    final_df = pd.concat(dataframes, ignore_index=True)

    # Export combined cleaned report
    output_file = "Final_Monthly_Sales_Report.xlsx"
    final_df.to_excel(output_file, index=False)
    print("Compiled report saved as:", output_file)
    return output_file
