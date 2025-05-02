# import pandas as pd
# data = [1,2,3,4,5]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [['Alex',10, 'M'],['Bob',12, 'M'],['Clarke',13, 'F']]
# df = pd.DataFrame(data, columns=['Name', 'Age', 'Gender'])
# print(df)

# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
# print(df)

# import pandas as pd
# data = [{'a': 1, 'b': 2, 'c': 7},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

# #With two column indices, values same as dictionary keys
# df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

# #With two column indices with one index with other name
# df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
# print(df1)
# print(df2)

# import pandas as pd
# d = {'one' :pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two' :pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print(df)

# import pandas as pd
# data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd

# #Create a Dataframe
# df = pd.DataFrame({
#     'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
#     'Age': [32, 28, 45, 38],
#     'Gender': ['Male', 'Female', 'Male', 'Female'],
#     'Rating': [3.45, 4.6, 3.9, 2.78]},
#     index=['r1', 'r2', 'r3', 'r4'])

# # Display the Input DataFrame
# print('Input DataFrame:\n',df)

# #Modify the Row labels of the DataFrame
# df.index = [100, 200, 300, 400]
# print('Outut Modified DataFrame with the updated index labels:\n', df)