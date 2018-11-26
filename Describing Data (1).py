#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
                 
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]
                 
df


# In[11]:


import numpy as np
import pandas as pd
                 
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]

np.mean(df['age'])


# In[13]:


import numpy as np
import pandas as pd
                 
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]

np.median(df['age'])


# In[14]:


import numpy as np
import pandas as pd
import statistics
             
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]

statistics.mode(df['age'])


# In[15]:


import numpy as np
import pandas as pd
             
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]

np.var(df.age)


# In[17]:


import numpy as np
import pandas as pd
             
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]

np.std(df['age'], ddof=1)


# In[18]:


import numpy as np
import pandas as pd
             
df = pd.DataFrame()
df['name'] = ['Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Oliver']
df['age'] = [14,12,11,10,8,6,8]

np.std(df['age'] ,ddof=1) / np.sqrt(len(df['age']))


# In[ ]:




