# LEGB rule: Local Enclosing Global Built-in

name = 'global'

def enclosing():
    name = 'enclosing'

    def local():
        global name     # bring name from global namespace into local
        #nonlocal name  # bring name from enclosing namespace into local
        name = 'local'
    
    print(f'enclosing name: {name}')
    local()
    print(f'enclosing name: {name}')

print(f'global name: {name}')    
enclosing()
print(f'global name: {name}')
