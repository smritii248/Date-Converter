import datetime as dt
import nepali_datetime as ndt

def english_to_nepali(ad_year, ad_month, ad_day):
    try:
        ad_date = dt.date(ad_year, ad_month, ad_day)  
        bs_date = ndt.date.from_datetime_date(ad_date)
        return bs_date
    except ValueError as e:
        return f"Invalid English date: {e}"  





