def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

total = sum_all(1,2,3,4,5)

print(f"Sum of all numbers: {total}")

def find_cylinder_volume(radius, height=7):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    print(volume)
    return volume
print(find_cylinder_volume(5))


def company_info(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


company_info(ticker='AAPL', ceo="Tim Cook", revenue="200 billion")
      
      
x= lambda a: a*a

print(x(5))