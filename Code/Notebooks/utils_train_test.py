from collections import namedtuple

ProcessingStatus = namedtuple("ProcessingStatus", 
                "excluded df_path times_path tr_path ex_path ts_path naive_md_p aarima_md_p aets_md_p theta_md_p spc_stt_md_p lin_reg_md_p rnd_frst_md_p")    

ForecastingBW = namedtuple("ForecastingBW", 
                "y_tr y_ex y_ts naive aarima aets theta spc_stt lin_reg rnd_frst")   

ProcessingStatusCV = namedtuple("ProcessingStatusCV", 
                "excluded df_path times_path y_path cv_path naive_md_p aarima_md_p aets_md_p theta_md_p spc_stt_md_p lin_reg_md_p rnd_frst_md_p")    

ForecastingCV = namedtuple("ForecastingCV", 
                "y cv naive aarima aets theta spc_stt lin_reg rnd_frst")   

ProcessingStatusTest = namedtuple("ProcessingStatusTest", 
                "excluded tr_path ex_path ts_path model_path")    

