# In[3]:


def distribution1(ii):
    x=0;
    if(ii==0):
        x=np.random.uniform(0, 400);
    else:
        x=np.random.uniform(0, 15);
    return x;

def value_distribution():
    list_temp=[np.random.rand(agent_number_n) for i in range(agent_number_n)];
    for ii in range(len(list_temp)):
        list_temp[ii]=distribution1(ii)
        
    list_temp=np.array(list_temp)
    return list_temp;
print(value_distribution())


# In[4]:


value_list=[];
for i in range(200000):
    temp=value_distribution()
    value_list.append(temp);


# In[5]:


value_list1=np.array(value_list)
print(value_list1)
print(value_list1[:,0])


# In[6]:


pa1=value_list1[:,0]


# In[7]:

plt.hist(pa1,bins=200)
plt.show()

pa2=value_list1[:,1]
plt.hist(pa2,bins=200)
plt.show()



