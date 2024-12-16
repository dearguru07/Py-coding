# class Bird:
#     def speak(self):
#         print("Chirp")

# class Parrot(Bird):
#     def speak(self):
#         print("Squawk")

# def make_bird_speak(bird):
#     bird.speak()

# parrot = Parrot()
# make_bird_speak(parrot)



# n=int(input('Enter a number..'))
# x=int(input('enter a number'))
# y=int(input('enter a number'))
# res=x*y
# if(res==n):
#     print(1)
# else:
#     print(-1)    


def Prime(n):
    er=n//2
    for i in range(2,er+1):
        if n%i==0 and n>1:
            print('prime number')
        else:
            print('not a prime')
n=int(input('NEter a nuber'))        
Prime(n)


def Fibbi(n):
    n1=0
    n2=1