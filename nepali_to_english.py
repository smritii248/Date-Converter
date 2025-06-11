
import nepali_datetime as np
def nepali_to_english(bs_year,bs_month,bs_day):
    #creating the nepali date obj 
    try:
     bs_date=np.date(bs_year,bs_month,bs_day)
     english_date=bs_date.to_datetime_date()
     return english_date
    
    except ValueError as e:
     return f"Invalid Nepali date: {e}"
     





