#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
os.chdir("C:\\Users\\91721\\Desktop\\Ims files\\Exploring Text Data")


# In[8]:


import pandas as pd
data=pd.read_csv("tweets.csv",encoding='ISO-8859-1')


# In[9]:


data.head()


# In[11]:


textcol=data["text"]


# In[13]:


textcol.head()


# In[38]:


def wfreq(textcol):
    wordlist=[]
    for wd in textcol.split():
        wordlist.extend(wd)
    wfreq=pd.Series(wordlist).value_counts()
    wfreq[:20]
    return wfreq


# In[29]:


fr=wfreq(textcol.str)


# In[30]:


fr


# In[31]:


print(fr)


# In[33]:


get_ipython().system('pip install WordCloud')


# In[36]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[49]:


wordfreq=wfreq(textcol.str)


# In[50]:


wc=WordCloud(height=700,width=800,background_color="white",max_words=200).generate_from_frequencies(wordfreq)
plt.figure(figsize=(12,6))
plt.axis("off")
plt.imshow(wc,interpolation="bilinear")
plt.show()


# In[53]:


wordfreq.to_csv("Wordfreq.csv")


# In[103]:


import re
def clean_text(textcol):
    textcol=textcol.lower()
    textcol=re.sub("rt","",textcol)
#     textcol=re.sub("to","",textcol)
#     textcol=re.sub("is","",textcol)
#     textcol=re.sub("in","",textcol)
    textcol=re.sub("&amp","",textcol)
    textcol=re.sub("\n","",textcol)
    textcol=re.sub(r"[?@#:.,!\_-]","",textcol)
    return textcol


# In[104]:


clean_text(str(textcol))


# In[105]:


textcol


# In[106]:


textcol1=textcol.apply(lambda x:clean_text(x))


# In[107]:


textcol1


# In[108]:


from wordcloud import STOPWORDS


# In[109]:


print(STOPWORDS)


# In[110]:


clean_words=wfreq(textcol1.str)


# In[111]:


clean_words


# In[112]:


clean_words=clean_words.drop(labels=STOPWORDS,errors="ignore")


# In[113]:


clean_words


# In[118]:


wc=WordCloud(height=200,width=200,background_color="white",max_words=100).generate_from_frequencies(clean_words)
plt.figure(figsize=(12,6))
plt.axis("off")
plt.imshow(wc,interpolation="bilinear")
plt.show()


# In[ ]:




