import math

#calculate tip
tip = 0.18


# In[9]:



def calculate_tip (bill):
    return math.ceil(tip * bill)

def calculate_bill_per_person (bill, people):
    return bill / people


# In[10]:


#calculate tip

print ("What's the total bill for today, please?")

bill = int(input ())

print ("What's the number of people, please?")

people = int(input ())

total_bill = bill+calculate_tip(bill)

print ("{}% tip is , which brings your total to {}".format(tip*100,total_bill ))

print ("which is {} per person".format(calculate_bill_per_person(total_bill,people) ))