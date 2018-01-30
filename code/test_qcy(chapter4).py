import nsfg
import thinkplot
import probability
import thinkstats2

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome==1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

'''
#第一种：出频数柱状图
first_hist = thinkstats2.Hist(firsts.totalwgt_lb)
other_hist = thinkstats2.Hist(firsts.totalwgt_lb)

#width = 0.02

thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', label='first_birth')
thinkplot.Hist(other_hist, align='left', label='other_birth')
thinkplot.Show(xlabel='totalwgt_lb',
               ylabel='probability',
               title='PMF of newborns_weight')
'''

#第二种：出频率柱状图
first_pmf = thinkstats2.Pmf(firsts.totalwgt_lb, label='first_birth')
other_pmf = thinkstats2.Pmf(others.totalwgt_lb, label='other_birth')

width = 0.05

thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(first_pmf, align='right', width=width)
thinkplot.Hist(other_pmf, align='left', width=width)
thinkplot.Config(xlabel='totalwgt_lb',
               ylabel='probability',
               title='Pmf of newborns_weight')

thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Pmfs([first_pmf, other_pmf])
thinkplot.Show(xlabel='totalwgt_lb',
               ylabel='probability',
               title='Pmf of newborns_weight')
