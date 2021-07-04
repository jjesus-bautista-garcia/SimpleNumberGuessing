#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Set initial stuff
import numpy as np

attempts, limit, random_number, winner  = None, None, None, False


# In[2]:


def Init_Settings(att=3, lim=10):
    global attempts
    global limit
    global random_number
    
    attempts = att

    limit = lim

    random_number =  np.random.randint(limit)
    
    print(f"""
    Welcome to the most exciting game in the world: Random Number Guessing

         You must type any number from 0 to {limit}
         Your attempts are: {attempts}


    ------------------------------------------------------------------

    """)


# In[3]:


def HintHelper():
    
    global user_guess_number_int
    global random_number
    
    bool_tets = int(user_guess_number_int) > random_number
    
    if bool_tets > 0:
        print("\tSlow down, mijo; it is too high...\n")
    else:
        print("\tTry a higher one, my pana!!!\n")


# In[11]:


def Prize():
    print(r"""

             _.-.
           ,'/ //\
          /// // /)
         /// // //|
        /// // ///
       /// // ///
      (`: // ///
       `;`: ///
       / /:`:/
      / /  `'
     / /
    (_/ 

    """)


# In[12]:


Init_Settings()

while attempts > 0:
    number_validation = False
    
    while False == number_validation:
        user_guess_number = input("Type a number:\n")
        
        user_guess_number_int = int(user_guess_number)
        
        number_validation = (user_guess_number_int <= limit) and (user_guess_number_int >= 0)
        
        if False == number_validation:
            
            print(f"Type another number; yours is higher than the limit: {limit}\n")
    
    if user_guess_number_int == random_number:
        
        print("You are a master!; congratulations...\n")
        
        Prize()
        
        winner = True
        
        break
        
    else:
        
        attempts-=1
        
        print(f"\nLet's try again...\n     Your attempts are: {attempts}\n\n")
        
        HintHelper()
        
if (attempts == 0) and (winner == False):
    print(f"So sorry; you didn't win this match.\n\tThe real number was {random_number}")


# In[ ]:




