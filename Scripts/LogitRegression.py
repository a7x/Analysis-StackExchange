from sklearn import linear_model
from FeatureUtils import *
import numpy as np
(features,output) = getXy(sys.argv[1])

clf = linear_model.LogisticRegression(penalty='l1')
clf.fit(features,output)

print clf.coef_

(testFeatures, testOutput) = getXy(sys.argv[2])

print 'Error is ',np.mean((clf.predict(testFeatures) - testOutput) ** 2)


