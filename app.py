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


# def Prime(n):
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0 and n>1:
#             print('prime number')
#         else:
#             print('not a prime')
# n=int(input('NEter a nuber'))        
# Prime(n)


# def Fibbi(n):
#     n1=0
#     n2=1


from collections import defaultdict

def find_route(tickets, start):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for src, dest in tickets:
        graph[src].append(dest)
    
    # Step 2: Sort destinations to maintain lexicographical order if needed
    for city in graph:
        graph[city].sort(reverse=True)
    
    # Step 3: Use DFS to reconstruct the path
    route = []
    def dfs(city):
        while graph[city]:
            next_city = graph[city].pop()
            dfs(next_city)
        route.append(city)
    
    # Start DFS from the given starting city
    dfs(start)
    
    # Step 4: Reverse the route to get the correct order
    return route[::-1]

# Input tickets and starting city
tickets = [
    ("Paris", "Skopje"), ("Zurich", "Amsterdam"), ("Prague", "Zurich"),
    ("Barcelona", "Berlin"), ("Kiev", "Prague"), ("Skopje", "Paris"),
    ("Amsterdam", "Barcelona"), ("Berlin", "Kiev"), ("Berlin", "Amsterdam")
]
start_city = "Kiev"

# Find and print the route
route = find_route(tickets, start_city)
print(" -> ".join(route))
