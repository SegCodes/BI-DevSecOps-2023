def action1(num):
    print('action1')
    if num>10:
        raise ValueError

def action2(num):
    print('action2')
    if num>10:
        raise ValueError
    
def action3(num):
    print('action3')
    if num>10:
        raise ValueError
    
try:
    action1(8)
    action2(4)
    action3(2)
    print('OK AT LAST')
except:
    print('BAD NUMBER')