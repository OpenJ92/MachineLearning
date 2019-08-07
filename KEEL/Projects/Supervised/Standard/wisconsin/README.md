

```python
from Helper.Load.load import Base_Load
from Helper.Load.supervised import Supervised
from Helper.Load.regression import Regression
from Helper.Load.classification import Classification
from Helper.Visual.Visual import Visual
from Helper.Visual.classification import VClassification
from Helper.Transform.Transform.classification import Classificaton_Transform
from Helper.Train.Train import Train

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```


```python
loadC = Classification("Data", "wisconsin.dat", "wisconsin-names.txt")
transformC = Classificaton_Transform(loadC)
```

    > /Users/jacob/Desktop/Project/MachineLearning/KEEL/Projects/Supervised/Standard/wisconsin/Helper/Transform/Transform/classification.py(32)visual_data()
    -> return pd.DataFrame(self.featureU().transform(data), columns=data.columns)


    (Pdb)  c



```python
loadC.attributes
```




    [['@attribute', 'ClumpThickness', 'integer', '[1,10]'],
     ['@attribute', 'CellSize', 'integer', '[1,10]'],
     ['@attribute', 'CellShape', 'integer', '[1,10]'],
     ['@attribute', 'MarginalAdhesion', 'integer', '[1,10]'],
     ['@attribute', 'EpithelialSize', 'integer', '[1,10]'],
     ['@attribute', 'BareNuclei', 'integer', '[1,10]'],
     ['@attribute', 'BlandChromatin', 'integer', '[1,10]'],
     ['@attribute', 'NormalNucleoli', 'integer', '[1,10]'],
     ['@attribute', 'Mitoses', 'integer', '[1,10]'],
     ['@attribute', 'Class', '{2,4}']]



<img src="Data/Visual/andrews_curves.png">
