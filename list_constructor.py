simpp = list(('Hungary', 'Paris', 'Japan', 'Alaska', 60, False, 99.99, 'z'))
print(type(simpp[5]))
print(len(simpp[0]))
print(simpp[2:])



OUTPUTS :
<class 'bool'>
7
['Japan', 'Alaska', 60, False, 99.99, 'z']



## Added a Python List constructor example demostrating :
** Created a list using list()
** Checked the data type using type()
** Finding the lenght using len()
** Accessing list elements using indexing  and slicing  

MISTAKES :
Here i initially thought of doing this operation print(type(simpp[5][0]),
But 'bool' object is not subscriptable , as we cannot treat it as list or string                                                        
