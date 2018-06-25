Ques-1

import re
emails = "zuck26@facebook.com" " page33@google.com" " jeff42@amazon.com"
pattern = (r'[\w]+')
print(re.findall(pattern, emails))

Ques-2

import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
pattern = (r'[bB]+\S*')
print(re.findall(pattern,text))
