import re

#line = "xxx出生于2001年6月1日"
#line = "xxx出生于2001/6/1"
#line = "xxx出生于2001-6-1"
#line = "xxx出生于2001-06-01"
line = "xxx出生于2001-06"
regex = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]|\d{1,2}|$))"
math_obj = re.match(regex, line)
if math_obj:
    print(math_obj.group(1))
#贪婪的匹配模式