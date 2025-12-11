def q(x,y):
    print(f"? {x} {y}")
def a(x,y):
    print("!",x, y)
def i():
    return int(input())
q(2,2)
if i() == 1:
    q(1,1)
    if i() == 1:
        a(1,1)
    else:
        q(2,1)
        if i() == 1:
            a(2,1)
        else:
            q(1,2)
            if i() == 1:
                a(1,2)
            else:
                a(2,2)
else: #Bottom right
    q(4, 4)
    if i() == 1:
        q(4, 3)
        if i() == 1:
            q(3,3)
            if i() == 1:
                a(3,3)
            else:
                a(4,3)
        else:
            q(3, 4)
            if i() == 1:
                a(3, 4)
            else:
                a(4,4)
    else: # Top Right
        q(2, 4)
        if i() == 1:
            q(2, 3)
            if i() == 1:
                q(1,3)
                if i() == 1:
                    a(1,3)
                else:
                    a(2,3)
            else:
                q(1,4)
                if i() == 1:
                    a(1,4)
                else:
                    a(2,4)
        else: # Bottom left
            q(4,1)
            if i() == 1:
                q(3,2)
                if i() == 1:
                    a(3,1)
                else:
                    a(4,1)
            else:
                q(3,2)
                if i() == 1:
                    a(3,2)
                else:
                    a(4,2)

