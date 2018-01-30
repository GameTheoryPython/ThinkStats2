import thinkstats2
import thinkplot
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome==1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_pmf = thinkstats2.Pmf(firsts.prglngth, label='first_birth')
other_pmf = thinkstats2.Pmf(others.prglngth, label='other_birth')

width = 0.45

thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(first_pmf, align='right', width=width)
thinkplot.Hist(other_pmf, align='left', width=width)
thinkplot.Config(xlabel='weeks',
                 ylabel='probability',
                 axis=[27, 46, 0, 0.6])

thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Pmfs([first_pmf, other_pmf]) 
thinkplot.Show(xlabel='weeks',
               axis=[27, 46, 0, 0.6])
