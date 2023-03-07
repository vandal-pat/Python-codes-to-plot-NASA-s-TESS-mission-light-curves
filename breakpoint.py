from astropy.io import fits
import numpy as np 
import matplotlib.pyplot as plt
from PyAstronomy.pyTiming import pyPeriod

data = fits.open('light_curve_name.fits')[1].data

breakpoint()

# After the breakpoint, type those commands one by one:

# 1. Light curves:

#good = np.where(np.isfinite(data.PDCSAP_FLUX) & np.isfinite(data.PDCSAP_FLUX_ERR))[0]

#goodd = np.where(np.isfinite(data.SAP_FLUX) & np.isfinite(data.SAP_FLUX_ERR))
#flux = data.PDCSAP_FLUX
#flux /= np.nanmedian(data.PDCSAP_FLUX)
#fluxx /=  np.nanmedian(data.SAP_FLUX)
#plt.plot(data.TIME,flux,linestyle='dotted',marker=None, label='PDCSAP')
#plt.plot(data.TIME,fluxx+0.02,linestyle='dotted',marker=None, label='SAP')
#plt.gcf().autofmt_xdate()
#plt.xlabel('PJDS')
#plt.ylabel('Flux')
#plt.legend()
#plt.title("whatever_title_you_prefer")
#plt.show()

# 2. GLS periodograms:

#good = np.where(np.isfinite(data.PDCSAP_FLUX) & np.isfinite(data.PDCSAP_FLUX_ERR))[0]
#goodd = np.where(np.isfinite(data.SAP_FLUX) & np.isfinite(data.SAP_FLUX_ERR))[0]
#gls=pyPeriod.Gls((data.TIME[good],data.PDCSAP_FLUX[good],data.PDCSAP_FLUX_ERR[good]),Pbeg=0.1,Pend=100, label='PDCSAP')
#glss=pyPeriod.Gls((data.TIME[goodd],data.SAP_FLUX[goodd],data.SAP_FLUX_ERR[goodd]),Pbeg=0.1,Pend=100,label='SAP')
#plt.rcParams['font.size'] = '20'
#plt.semilogx(1/gls.freq,gls.power,'k.-',label='PDCSAP')
#plt.semilogx(1/glss.freq,glss.power,'b.-',label='SAP')
#plt.xlabel('Period')
#plt.ylabel('Flux')
#plt.legend()
#plt.show()
