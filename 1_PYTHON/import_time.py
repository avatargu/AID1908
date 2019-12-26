import time

time_stamp = time.time()
print("时间戳, time_stamp:",time_stamp)
time_tuple = time.localtime()
print("时间元组, time_tuple:",time_tuple)

print("元组操作, time_tuple[0]:",time_tuple[0])
print("类操作, time_tuple.tm_year:",time_tuple.tm_year)

time_tuple = time.localtime(time_stamp)
print("从时间戳到时间元组:",time_tuple)
time_stamp = time.mktime(time_tuple)
print("从时间元组到时间戳:",time_stamp)

time_str = time.strftime("%y/%m/%d %H:%M:%S",time_tuple)
print("从时间元组到字符串:",time_str)
time_tuple = time.strptime(time_str,"%y/%m/%d %H:%M:%S")
print("从字符串到时间元组:",time_tuple)

# def get_wday(year,mon,mday):
#     """
#         根据年月日，获取星期几
#     :param year:年
#     :param mon:月
#     :param mday:日
#     :return:星期几
#     """
#     tuple_time = time.strptime("%d/%d/%d"%(year,mon,mday), "%Y/%m/%d")
#     dict_wday = {
#         0:"星期一",
#         1:"星期二",
#         2:"星期三",
#         3:"星期四",
#         4:"星期五",
#         5:"星期六",
#         6:"星期日"
#     }
#     return dict_wday[tuple_time.tm_wday]
#
# print(get_wday(2019,8,22))

# def get_live_days(year,mon,mday):
#     """
#         根据生日计算活了多少天
#     :param year: 年
#     :param mon: 月
#     :param mday: 日
#     :return: 活了多少天
#     """
#     tuple_time = time.strptime("%d/%d/%d"%(year,mon,mday), "%Y/%m/%d")
#     time_birthday = time.mktime(tuple_time)
#     time_now = time.time()
#     return int((time_now - time_birthday)/60/60/24)
#
# print(get_live_days(1993,7,19))


