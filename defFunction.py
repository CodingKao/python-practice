# Use def function to render Hello + Name
def greeting(name):
    print('Hello, ' + name)

greeting('Kao')

# Use def function to render 2 names
def greetings(name1, name2):
    print('Hello, ' + name1 + ' ' + name2)

greetings('Kao', 'Saelor')

# Use def function for addition
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

# use def function for to find area of triangle
def area_triangle(base, height):
    return base * height / 2

area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)

total_area = area_a + area_b
print(total_area)

# Use def function to get seconds
def get_seconds(hours, minutes, seconds):
    total_seconds = 3600*hours + 60*minutes + seconds
    return total_seconds

print(get_seconds(16,45,20))
