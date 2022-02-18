users = {
    'sahinmaral':{
        'age':22,
        'telephoneNumber' : 2221113322,
        'id' : 1,
        'username' : 'sahinmaral',
        'isActive' : True,
        'roles' : ['user','admin']
    },
    'aliyetmez':{
        'age':22,
        'telephoneNumber' : 2225551100,
        'id' : 2,
        'username' : 'aliyetmez',
        'isActive' : True,
        'roles' : ['user']
    }
}

print(users['aliyetmez']['id'])
print(users['sahinmaral']['roles'][1])