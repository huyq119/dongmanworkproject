class Solution(object):
    def toDay(self, dateStr):
        year = int(dateStr[:4])
        month = int(dateStr[5:7])
        day = int(dateStr[-2:])

        if month <= 2:
            year -= 1
            month += 10
        else:
            month -= 2

        return 365 * year + year // 4 - year // 100 + year // 400 + 30 * month + (3 * month - 1) // 5 + day  # - 584418

    def daysBetweenDates(self, date1, date2):
        return abs(self.toDay(date1) - self.toDay(date2))

# 作者：Dragon_fxl
# 链接：https://leetcode-cn.com/problems/number-of-days-between-two-dates/solution/cyu-yan-0ms-14xing-jian-ji-dai-ma-jie-zhu-zellergo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
