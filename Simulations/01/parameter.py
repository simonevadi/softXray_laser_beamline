import numpy as np
import pandas as pd

nrays    = 1e5
rounds   = 1
ncpu     = 10

param_dict = {
    '20240628-681.64eV-TVLSG-Spec-105eV-620eV-2.0m-1mROCG-1deg-1200l,mm-1000mm-1030.8mm-2400RP-IW.rml':'202406-Spectrometer-CVLSG-2-ResolutionScanParameters.csv',
    '20240709-1-103.3eV-TVLSG-Spec-58eV-310eV-2.0m-1mROCG-1deg-600l,mm-1000mm-1036mm-2400RP-IW.rml':'202406-Spectrometer-CVLSG-Stolow-1-ResolutionScanParameters.csv', 
    '20240627-2-206.7eV-TVLSG-Spec-105eV-620eV-2.0m-1mROCG-1deg-1200l,mm-1000mm-1036mm-2400RP-IW.rml': '202406-Spectrometer-CVLSG-Stolow-2-ResolutionScanParameters.csv',
    '20240709-3-413.3eV-TVLSG-Spec-210eV-1240eV-2.0m-1mROCG-1deg-2400l,mm-1000mm-1036mm-2400RP-IW.rml':'202406-Spectrometer-CVLSG-Stolow-3-ResolutionScanParameters.csv', 
    }
