import pandas as pd
import numpy as np
import constants

def makeSummary():
    df = pd.read_csv(constants.filePath)
    summary = []
    dates = df.date.drop_duplicates()
    for date in dates.values:
        # Date summary
        date_df = df[df.date == date]
        #date_df = date_df.sort_values(["date","time"])

        # Check of types
        start_count = date_df[date_df.type == 'start'].count().type
        end_count = date_df[date_df.type == 'end'].count().type
        if start_count != end_count:
            msg_date = "{}".format(date_df.values[0][0])
            msg = "There are not equal amounts of start and end types. [Start:{} End:{}]".format(start_count, end_count)
            print("ERROR IN ", msg_date, " | Description: ", msg)
            continue

        # Time formatting
        date_df['time'] = pd.to_timedelta(date_df['time'],
                                            unit='s',
                                            errors='coerce')

        # Calculate time of work
        start = date_df[date_df.type == 'start']
        start = start.sort_values(["date","time"])
        start = start['time'].values
        end = date_df[date_df.type == 'end']
        end = end.sort_values(["date","time"])
        end = end['time'].values

        times = end - start
        total = 0
        for time in times:
            total += time

        # Add result to summary dataframe
        # https://stackoverflow.com/questions/10715965/add-one-row-to-pandas-dataframe
        summary.append({
            'date': date,
            'time_spent': total
        })
    df = pd.DataFrame(summary)
    # Save csv // https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
    df.to_csv(constants.summaryPath, sep=',', index=False)
    print("--- SUMMARY DONE ---")

def analyzeMonthlyData():
    month_analyze = []
    df = pd.read_csv(constants.summaryPath)
    # Date formatting
    df['date'] = pd.to_datetime(df['date'],
                                format='%Y-%m-%d',
                                errors='coerce')
    # Time formatting
    df['time_spent'] = pd.to_timedelta(df['time_spent'],
                                       unit='s',
                                       errors='coerce')
    # Analysis
    # https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column
    df['month'] = df['date'].map(lambda x: x.month)
    months = df.month.drop_duplicates()
    for month in months:
        mean_hours = df[df['month'] == month]['time_spent'].mean()
        month_analyze.append({'month': month, 'mean_hours': mean_hours})
    df = pd.DataFrame(month_analyze)
    # Save csv // https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
    df.to_csv(constants.analysisPath, sep=',', index=False)
    print("--- ANALYSIS DONE ---")

if __name__ == "__main__":
    makeSummary()
    analyzeMonthlyData()
