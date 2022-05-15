friend_name='Ann'
friends=['mama', 'papa', 'Ann']
roles=('admin', 'guest', 'user')

if 'mama' in friends:
    print('est takoy koresh')

if 'A' in friend_name :
    print('YES est M')

i=0
while i<len(friends):
    friend=friends[i]
    print(friend)
    i+=1

for friend in friends:
    print(friend)

for letter in friend_name:
    print(letter)
