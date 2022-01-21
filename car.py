class Car(object):
   def __init__(self,model,color,company,speed_limit):
       self.color=color
       self.model = model
       self.company=company
       self.speed_limit=speed_limit

   

Toyota=Car("innova","white","toyota","80")
print(Toyota.color)
print(Toyota.model)