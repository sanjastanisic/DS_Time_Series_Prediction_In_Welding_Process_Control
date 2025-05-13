import pandas as pd

def insert_milisec_data(df):
    spot_name = df.SpotName.min()
    df.drop('SpotName', axis=1, inplace=True)
    df.drop('TimeStamp', axis=1, inplace=True)
    df.drop('Year', axis=1, inplace=True)
    df.drop('Month', axis=1, inplace=True)
    df.drop('Day', axis=1, inplace=True)
    df.drop('Date', axis=1, inplace=True)
    inserted_data = {'WeldingTime': [],
            'Voltage' : [],
            'Current' : []
            }
    ts_days_mins = df.WeldingTime.min()
    ts_days_max = df.WeldingTime.max()
    ts_delta = pd.to_timedelta(1, unit="ms")
    ts = ts_min + ts_delta
    while ts < ts_max:
        if ts in df.WeldingTime.values:
            ts += ts_delta
            continue
        inserted_data['WeldingTime'].append(ts)
        inserted_data['Voltage'].append(0)
        inserted_data['Current'].append(0)
        ts += ts_delta
    inserted_df = pd.DataFrame(inserted_data)
    if inserted_df.shape[0] > 0:
        df = pd.concat([df, inserted_df])
        df.sort_values(by=['WeldingTime'], inplace=True)
        df.set_index(df.WeldingTime, inplace=True)
