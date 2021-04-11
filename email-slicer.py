# In[18]:


popular_domains = {'gmail.com':'Google','yahoo.com':'Yahoo','outlook.com':'Microsoft'}


# In[20]:


#email sclicer

email = input('Please introduce your email').strip()

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

check_domain(username,domain)


# In[19]:


def check_domain (username, domain):
    if domain in popular_domains:
        print ("Hey {}, I see your email is registered with {}, that's cool!".format(username,popular_domains[domain]))
    else: 
        print ("Hey {}, looks like you've got your own custom setup at {}. Impressive!".format(username,domain))