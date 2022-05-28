def date_convertion_ss(date_value):
    import re
    from datetime import datetime

    # pattern1='\d+.\D+.\d{2,4}' #"8 March 2017","8-March-2017","8-Mar-2017"
    if date_value==re.search("\d\-\d\-\d+|\d+.\D+.\d{2,4}|\d+\/\d+\/\d{2,4}",date_value).group():
        try:
            # "8 March 2017"
            date_value = datetime.strptime(date_value, '%d %B %Y')
            return date_value.strftime('%d.%m.%Y')
        except:
            try:
                # "8 jan 2017"
                date_value = datetime.strptime(date_value, '%d %b %Y')
                return date_value.strftime('%d.%m.%Y')
            except:
                try:
                    # "8-March-2017"
                    date_value = datetime.strptime(date_value, '%d-%B-%Y')
                    return date_value.strftime('%d.%m.%Y')
                except:
                    try:
                        # "8-Mar-2017"
                        date_value = datetime.strptime(date_value, '%d-%b-%Y')
                        return date_value.strftime('%d.%m.%Y')
                    except:
                        try:
                            # "8-March-17"
                            date_value = datetime.strptime(date_value, '%d-%B-%y')
                            return date_value.strftime('%d.%m.%Y')
                        except:
                            try:
                                # "8-Mar-17"
                                date_value = datetime.strptime(date_value, '%d-%b-%y')
                                return date_value.strftime('%d.%m.%Y')
                            except:
                                try:
                                    # "8 March 17"
                                    date_value = datetime.strptime(date_value, '%d %B %y')
                                    return date_value.strftime('%d.%m.%Y')
                                except:
                                    try:
                                        date_value = datetime.strptime(date_value, '%d/%m/%y')
                                        return date_value.strftime('%d.%m.%Y')
                                    except:
                                        try:
                                            date_value = datetime.strptime(date_value, '%d/%m/%Y')
                                            return date_value.strftime('%d.%m.%Y')
                                        except:
                                            try:
                                    # "8 jan 17"
                                           
                                                date_value = datetime.strptime(date_value, '%d %b %y')
                                                return date_value.strftime('%d.%m.%Y')
                                            except:
                                                date_value = datetime.strptime(date_value, '%d-%m-%y')
                                                return date_value.strftime('%d.%m.%Y')

    # pattern2 = '\d+.\d+.\d{2,4}'  # numeric DDMMYY
    elif date_value == re.search("\d+.\d+.\d{2,4}",date_value).group():
        try:
            date_value = datetime.strptime(date_value, '%d/%m/%Y')
            return date_value.strftime('%d.%m.%Y')
        except:
            try:
                date_value = datetime.strptime(date_value, '%d.%m.%Y')
                return date_value.strftime('%d.%m.%Y')
            except:
                try:
                    date_value = datetime.strptime(date_value, '%d-%m-%Y')
                    return date_value.strftime('%d.%m.%Y')
                except:
                    try:
                        date_value = datetime.strptime(date_value, '%d/%m/%y')
                        return date_value.strftime('%d.%m.%Y')

                    except:
                        try:
                            date_value = datetime.strptime(date_value, '%d/%m/%Y')
                            return date_value.strftime('%d.%m.%Y')
                        except:
                            try:
                                date_value = datetime.strptime(date_value, '%d.%m.%y')
                                return date_value.strftime('%d.%m.%Y')
                            except:
                                try:
                                    date_value = datetime.strptime(date_value, '%d/%m/%Y')
                                    return date_value.strftime('%d.%m.%Y')
                                except:
                                    date_value = datetime.strptime(date_value, '%d-%m-%y')
                                    return date_value.strftime('%d.%m.%Y')

# s = "8-March-17"
# s2 = "8 jan 2017"
# s3="08/02/2022"
# # s4  = "11-8-1997"
# # s5 = "09/04/22"
# d = "3/4/21"
# x = "30-Dec-2021"
# y = "3-4-22"
# r = "09/04/22"
# print(date_convertion_ss(r))
