
import datetime
import pandas as pd

# split the dataset by 'chunkID', return a dict of id to rows
def to_chunks(values, chunk_ix=1):
	chunks = dict()
	# get the unique chunk ids
	chunk_ids = unique(values[:, chunk_ix])
	# group rows by chunk id
	for chunk_id in chunk_ids:
		selection = values[:, chunk_ix] == chunk_id
		chunks[chunk_id] = values[selection, :]
	return chunks

def fill_day_gaps_in_place(df, develop_mode):
    day_in_df = 0
    sdt = df.at[0,'WeldingTime']
    if "." in sdt:
        sdt = datetime.datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S.%f")
    else:
        sdt = datetime.datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S")
    start_date = sdt.date()
    #print(sdt)
    curr_date = start_date
    #print(curr_date)
    for i, row in df.iterrows():
        rwdt = str(row['WeldingTime'])
        if "." in rwdt:
            rwdt = datetime.datetime.strptime(rwdt, "%Y-%m-%d %H:%M:%S.%f")
        else:
            rwdt = datetime.datetime.strptime(rwdt, "%Y-%m-%d %H:%M:%S")
        rwd = rwdt.date()
        if(curr_date != rwd):
            day_in_df += 1
            curr_date = rwd
        day_diff = (rwdt.date() - sdt.date()).days
        nd = rwdt - datetime.timedelta(days=day_diff) + datetime.timedelta(days=day_in_df)
        df.at[i,'WeldingTime'] = nd
        if develop_mode:
            if (i % 10000 == 0):
                print((i, rwdt, day_diff, day_in_df))
        else: 
            if (i % 50000 == 0):
                print((i, rwdt, day_diff, day_in_df))

def fill_milisec_gaps_in_place(df, develop_mode):
    # NOT COMPLETED!!!
    ms_in_df = 0
    sdt = df.at[0,'WeldingTime']
    if "." in sdt:
        sdt = datetime.datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S.%f")
    else:
        sdt = datetime.datetime.strptime(sdt, "%Y-%m-%d %H:%M:%S")
    start_dt = sdt
    #print(start_dt)
    curr_dt = start_dt
    #print(curr_dt)
    for i, row in df.iterrows():
        rts = str(row['TimeStamp'])
        if "." in rts:
            rts = datetime.datetime.strptime(rts, "%Y-%m-%d %H:%M:%S.%f")
        else:
            rts = datetime.datetime.strptime(rts, "%Y-%m-%d %H:%M:%S")
        rwdt = str(row['WeldingTime'])
        if "." in rwdt:
            rwdt = datetime.datetime.strptime(rwdt, "%Y-%m-%d %H:%M:%S.%f")
        else:
            rwdt = datetime.datetime.strptime(rwdt, "%Y-%m-%d %H:%M:%S")
        if(rwdt != rts):
            ms_in_df += 1
            curr_dt = rwdt
        else:
            #ubaciti elemenat sa nultim naponom i nultom strujom
            pass
        ms_diff = rwdt - sdt
        nd = rwdt - ms_diff + datetime.timedelta(milliseconds=ms_in_df)
        df.at[i,'WeldingTime'] = nd
        if develop_mode:
            if (i % 10000 == 0):
                print((i, rwdt, ms_diff, ms_in_df))
        else: 
            if (i % 50000 == 0):
                print((i, rwdt, ms_diff, ms_in_df))