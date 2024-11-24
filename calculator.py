def calculator():
    firstnumber=int(input('Enter first number-'))
    secondnumber=int(input('Enter second number-'))
    print('Choose the method \n1.Multiplicaton \n2.Addition \n3.Substraction \n4.Division')
    a=int(input('Enter the method -'))
    if a==1:
        def mul():
            mul=firstnumber*secondnumber
            print(mul)
        mul()
    elif a==2:
        def add():
            sum=firstnumber+secondnumber
            print(sum)
        add()
    elif a==3:
        def sub():
            sub=firstnumber-secondnumber
            print(sub)
        sub()
    elif a==4:
        def div():
            div=firstnumber/secondnumber
            print(div)
        div()
calculator()