#-*- coding: utf-8 -*-
from datetime import datetime

now = datetime.now()

print 'Date is %s/%s/%s' % (now.day, now.month, now.year)
print 'Time is %s:%s:%s' % (now.hour, now.minute, now.second)
