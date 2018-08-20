def sidedish(number):
    def dish1(meal):
        return lambda: meal() + 30
        
    def dish2(meal):
        return lambda: meal() + 40
        
    def dish3(meal):
        return lambda: meal() + 50
        
    def dish4(meal):
        return lambda: meal() + 60
        
    def nodish(meal):
        return lambda: meal()
        
    return {
        1 : dish1,
        2 : dish2,
        3 : dish3,
        4 : dish4
    }.get(number, nodish)

@sidedish(2)
@sidedish(3)
def friedchicken():
    return 49.0
   
print(friedchicken()) # 139.0