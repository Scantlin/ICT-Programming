#THIS WORKPLACE IS FOR PLOTTING PRACTICE
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

def main():
    #this input will be the input for the user's customizable function
    print('--------------------------------------------------------------------------')
    print('This is function visualization')

    function = input('Enter the function: ')
    Indep = np.linspace(1, 10, 10)
    #x = symbols('x')

    poly_func = function.replace('^', '**').replace('x', '*x').replace('+ *x', '+ x').replace('- *x', '- x')

    if poly_func.startswith('*x'):
        poly_func = poly_func[1:]

    def f(x):
        return eval(poly_func)
    print(f(Indep))

    '''
    second = sympify(poly_func)
    fx = lambda x_value: second.subs(x, x_value)
    print(fx(5))

    fxx = lambdify(x, second)
    print(fxx(5))'''

    
    '''
    independent_var = np.linspace(-3, 3, 100)
    Dependendent_var = (independent_var**3) - (6 * independent_var)

    #scattering the actual points that we have
    x = np.linspace(-3, 3, 7) #or np.array([-3, -2, -1, 0, 1, 2, 3])
    fx = x**3 - 6*x

    plt.title('plotting of f(x) = x^3 - 6x')
    plt.plot(independent_var, Dependendent_var, color='red')
    plt.scatter(x, fx, color='blue', label='actual points')
    #plt.xticks(np.arange(0, 11, 1))
    #plt.yticks() <-- this is to adjust the labeling counting of any axis

    plt.xlim(min(independent_var)-1, max(independent_var) + 1)
    plt.ylim(min(Dependendent_var)-1, max(Dependendent_var)+1)

    plt.xlabel('independent variable')
    plt.ylabel('Dependent Variable')
    plt.grid()
    plt.savefig('workplace2.png')
    plt.show()
    print(independent_var)
    print(Dependendent_var)'''

    #other methods
    '''
    axvline	Vertical line	plt.axvline(x=2)
    axhline	Horizontal line	plt.axhline(y=3)
    axline	Arbitrary line	plt.axline((0,0), slope=1)

    #sample code
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(-5, 5, 100)
    y = x**2

    plt.plot(x, y, label='y = x²')
    plt.axvline(x=0, color='black', linestyle='-', label='x=0')  # Vertical axis
    plt.axhline(y=0, color='black', linestyle='-', label='y=0')  # Horizontal axis
    plt.axline((1,1), slope=2, color='red', linestyle='--', label='Tangent at x=1')  # Tangent line
    plt.legend()
    plt.grid(True)
    plt.savefig('workplace2.png')
    plt.show()'''

if __name__ == '__main__':
    main()