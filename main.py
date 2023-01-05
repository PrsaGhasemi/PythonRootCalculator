#I used a simple x^2 - x - 1 math function because its easier to find its real Root and compare with my python functions' answer.
# but you can change it to any other math function!

f = lambda x: x**2 - x - 1
# a and b are intervals! and N shows how many times you want to repeat this method. and obv. you know more bisections you have, more accurate answer you get!
a = float(input("enter a: "))
b = float(input("enter b: "))
N = int(input("enter N: "))

def bisection(f,df,a,b,eps,N):
    if f(a)*f(b) < 0 and (df != 0):
        a_n = a
        b_n = b
        for n in range(1,N+1):
            mid = (a_n + b_n)/2 
            f_mid = f(mid)
            if f(a_n)*f_mid < 0:
                a_n = a_n
                b_n = mid
            elif f(b_n)*f_mid < 0:
                a_n = mid
                b_n = b_n
            elif f_mid == 0:
                if abs(f_mid) < eps:
                    print("Found exact solution.")
                    return mid
            else:
                print("Bisection method fails.")
                
        return (a_n + b_n)/2
df = lambda x: 2*x - 1
eps = 2**(-26)
approx_phi = bisection(f,df,a,b,eps,N)
print(approx_phi)
    
y_0 = approx_phi
def newtonsWay(f,y_0,df,eps) :
    y= (y_0 - (f(y_0)/df(y_0)))
    if f(y)<eps:
        return y
    else:
        newtonsWay(f,y_0,df,eps)
newtonsGuess = newtonsWay(f,y_0,df,eps)
print(newtonsGuess)