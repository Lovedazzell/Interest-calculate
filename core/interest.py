from datetime import date


def find_interest(amount,release_date):
            # calculating total days of loan ammmount
            final = release_date - date.today()
            
            # converting seconds to year
            year = ( (final.total_seconds())/(365.242*24*3600))
            intyear = int(year)
            
            # extracting month form year
            months =(year-intyear)*12
            intmonths = int(months)
            
            # extracting days from months
            days= int((months-intmonths)*(365.242/12))
            
            # select interest rate according to ammmount
            if amount >= 5001:
                interest_rate = 2
            else:    
                interest_rate = 3
            if intyear > 0:
                # statement for find compound interest
                interest_p_month = (amount/100)*interest_rate
                interest_all_year =( intyear *12)*interest_p_month
                one_year_total = interest_all_year+amount
                interest_p_month = (one_year_total/100)*interest_rate
                interest_all_months = interest_p_month * intmonths
                interest_all_days = (interest_p_month/30)*days
                compound_grand_total = (one_year_total+interest_all_months+interest_all_days)
                return compound_grand_total

            else:    
                # statement to Find simple interest
                interest_p_month = (amount/100)*interest_rate
                interest_all_months = interest_p_month * intmonths
                interest_all_days = (interest_p_month/30)*days
                simple_grand_toatal = interest_all_days+interest_all_months +amount
                return simple_grand_toatal