#homework3 task2 multiproc

import numpy as np
import librosa
import os
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import warnings
import time

warnings.filterwarnings('ignore')

def mfcc(input_file):
	for address, dirs, files in os.walk(input_file):
		os.mkdir("new" + address)
		if files:
			filename = "new" + address
			for file in files:
				y, sr = librosa.core.load(address+'/'+file)
				sign = np.empty(0)
				sign = librosa.feature.mfcc(y=y, sr=sr)
				np.save(filename + '/' + file[:-4], sign)

# with ProcessPoolExecutor(max_workers=5) as pool:
# 	pool.submit(mfcc, 'aac')


print("Enter dir name:")
dirname = input()

start_time = time.time()

with ProcessPoolExecutor(max_workers=5) as pool:
	pool.submit(mfcc, dirname)

print("--- %s seconds ---" % (time.time() - start_time))
