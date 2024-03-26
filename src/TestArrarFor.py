import json  
  
# 假设jsonObj是一个字符串，表示JSON对象  
jsonObj = '''  
{  
    "a": [32, 32],  
    "b": [3, 2],  
    "c": [11, 53]  
}  
'''  
  
# 解析JSON对象  
data = json.loads(jsonObj)  
  
# 提取a, b, c三个数组  
a_list = data.get('a', [])  
b_list = data.get('b', [])  
c_list = data.get('c', [])  
  
# 确定遍历的次数（以最长的数组为准或使用min函数以最短的数组为准）  
length = max(len(a_list), len(b_list), len(c_list))  
  
# 使用for循环遍历索引并手动组合元素  
new_arrays = []  
for i in range(length):  
    # 根据索引从每个数组中取出元素，这里假设如果数组长度不够则用None填充  
    a_value = a_list[i] if i < len(a_list) else None  
    b_value = b_list[i] if i < len(b_list) else None  
    c_value = c_list[i] if i < len(c_list) else None  
      
    # 根据需要进行组合，这里只是简单地将它们放入一个列表中  
    # 你可以根据需要自定义组合方式，比如拼接字符串、创建字典等  
    combined = [a_value, b_value, c_value]  
      
    # 将组合后的结果添加到新数组中  
    new_arrays.append(combined)  
  
# 输出结果  
print(new_arrays)