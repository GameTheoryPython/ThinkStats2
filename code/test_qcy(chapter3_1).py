import thinkplot
import probability

d = {7: 8, 12: 8, 17: 14, 22: 4, 27: 6, 32: 12, 37: 8, 42: 3, 47: 2}
pmf = thinkstats2.Pmf(d, label='actual')
print(mean, pmf.Mean())

'''
weeks = range(35, 46)
diffs = []
for week in weeks:
    p1 = first_pmf.Prob(week)
    p2 = other_pmf.Prob(week)
    diff = 100 * (p1 - p2)
    diffs.append(diff)
    
thinkplot.Bar(weeks, diffs)
'''

biased_pmf = probability.BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='class size', ylabel='PMF')

'''
max(pmf.Values())
min(pmf.Values())
'''



'''
question1:在一个文件中，执行后无法同时显示多组图形
    