Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["Rajiv", 35, "Infosys", "Bangalore"]
>>> D = {'name':'Rajiv', 'age':35, 'company':'Infosys', 'place':'Bangalore'}
>>> type(D)
<class 'dict'>
>>> D
{'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}
>>> D['name']
'Rajiv'
>>> D['age']
35
>>> D['salary']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    D['salary']
KeyError: 'salary'
>>> D['salary'] = '1000000 INR'
>>> D
{'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore', 'salary': '1000000 INR'}
>>> D['salary'] = '5000000 INR'
>>> D
{'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore', 'salary': '5000000 INR'}
>>> 
>>> D.pop('salary')
'5000000 INR'
>>> D
{'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}
>>> 
>>> # ---------------------------------- basic functions
>>> 
>>> D.items()
dict_items([('name', 'Rajiv'), ('age', 35), ('company', 'Infosys'), ('place', 'Bangalore')])
>>> D.values()
dict_values(['Rajiv', 35, 'Infosys', 'Bangalore'])
>>> D.keys()
dict_keys(['name', 'age', 'company', 'place'])
>>> 
>>> 
>>> # --------------------------------------- tabulated data
>>> 
>>> D1 = {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}
>>> D2 = {'name': 'Anil', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}
>>> D2 = {'name': 'Sunil','age': 37, 'company': 'Oracle', 'place': 'Bangalore'}
>>> 
>>> D3 = {'name': 'Anil','age': 36, 'company': 'Wipro', 'place': 'Bangalore'}
>>> 
>>> 
>>> emp = {'E001':D1, 'E002':D2, 'E003':D3}
>>> emp
{'E001': {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, 'E002': {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, 'E003': {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}}
>>> emp['E002']
{'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}
>>> emp['E002']['place']
'Bangalore'
>>> emp['E004'] = {'name':'raj'}
>>> emp
{'E001': {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, 'E002': {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, 'E003': {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}, 'E004': {'name': 'raj'}}
>>> emp['E005'] = ['red', 'green', 'blue']
>>> emp
{'E001': {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, 'E002': {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, 'E003': {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}, 'E004': {'name': 'raj'}, 'E005': ['red', 'green', 'blue']}
>>> emp.values()
dict_values([{'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}, {'name': 'raj'}, ['red', 'green', 'blue']])
>>> emp['E005'] = None
>>> emp
{'E001': {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, 'E002': {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, 'E003': {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}, 'E004': {'name': 'raj'}, 'E005': None}
>>> emp.setdefault('S006')
>>> emp
{'E001': {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, 'E002': {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, 'E003': {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}, 'E004': {'name': 'raj'}, 'E005': None, 'S006': None}
>>> emp['E006'] = {'name':'kumar'}
>>> emp
{'E001': {'name': 'Rajiv', 'age': 35, 'company': 'Infosys', 'place': 'Bangalore'}, 'E002': {'name': 'Sunil', 'age': 37, 'company': 'Oracle', 'place': 'Bangalore'}, 'E003': {'name': 'Anil', 'age': 36, 'company': 'Wipro', 'place': 'Bangalore'}, 'E004': {'name': 'raj'}, 'E005': None, 'S006': None, 'E006': {'name': 'kumar'}}
>>> type(emp)
<class 'dict'>
>>> 
