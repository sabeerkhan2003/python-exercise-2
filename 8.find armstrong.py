def armstrong(num):
  sum=0
  str_num=str(num)
  n=len(str_num)
  for digit in str_num:
    sum+=int(digit)**n
  if sum==num:
    print("armstrong")
  else:
    print("not armstrong")
    
print(armstrong(1634))
    
                   
