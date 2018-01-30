import thinkstats2
import thinkplot
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome==1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

firsts1 = firsts[firsts.prglngth > 26]
others1 = others[others.prglngth > 26]
firsts2 = firsts1[firsts1.prglngth < 47]
others2 = others1[others1.prglngth < 47]

first_hist = thinkstats2.Hist(firsts2.prglngth)
other_hist = thinkstats2.Hist(others2.prglngth)
# plot

width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width, label='birthord_first')
thinkplot.Hist(other_hist, align='left', width=width, label='birthord_other')
thinkplot.Show(xlabel='weeks', ylabel='frequency')