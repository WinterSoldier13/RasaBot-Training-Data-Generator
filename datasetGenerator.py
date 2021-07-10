from random import randint

f = open('./dataset.txt', 'a')

quantity = ['profit', 'sales', 'revenue', 'quantity']
l1 = len(quantity) - 1
year = ['2018', '2019', '2020', '2021']
l2 = len(year) - 1
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Sept', 'Oct', 'Nov',
         'Dec']
l3 = len(month) - 1
state = ['Georgia', 'Illinois', 'Florida', 'Texas', 'California', 'Washington', 'Nevada', 'Massachusetts', 'Missouri',
         'Pennsylvania', 'New York', 'Michigan', 'Arizona']
l4 = len(state) - 1
product = ['Pens and Pencils', 'Cycles', 'Glasses', 'Other Items', 'Dish Washer', 'Computer Table', 'Ovens', 'Crockery',
           'Rackets', 'Safety Gears', 'Books', 'Chairs', 'Coffee Maker', 'Carrom', 'Pans', 'Balls', 'Central Table',
           'Stove', 'Cabinet', 'Bed', 'Dining Table', 'Craft Items', 'Gloves', 'Bats', 'Shoes', 'Sofa', 'Locker',
           'Magazines']
l5 = len(product) - 1

# what is the total [profit](QUANTITY) in the state of [Michigan](STATE) in [February](MONTH) [2018](YEAR) for the product [Stove](PRODUCT NAME)

for i in range(1000):
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in the state of [{state[randint(0, l4)]}](STATE) in [{month[randint(0, l3)]}](MONTH) [{year[randint(0, l2)]}](YEAR) for the product [{product[randint(0, l5)]}](PRODUCT_NAME)\n')
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in the state of [{state[randint(0, l4)]}](STATE) in [{month[randint(0, l3)]}](MONTH) [{year[randint(0, l2)]}](YEAR)\n')
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in the state of [{state[randint(0, l4)]}](STATE) in [{month[randint(0, l3)]}](MONTH)\n')
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in the state of [{state[randint(0, l4)]}](STATE) in [{year[randint(0, l2)]}](YEAR)\n')
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in [{month[randint(0, l3)]}](MONTH) of [{year[randint(0, l2)]}](YEAR)\n')
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in the state of [{state[randint(0, l4)]}](STATE)\n')
    f.write(
        f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in the state of [{state[randint(0, l4)]}](STATE)\n')
    f.write(f'- what is the total [{quantity[randint(0, l1)]}](QUANTITY) in [{year[randint(0, l2)]}](YEAR)\n')
    f.write(f'- [{quantity[randint(0, l1)]}](QUANTITY) in [{year[randint(0, l2)]}](YEAR)\n')
    f.write(f'- [{quantity[randint(0, l1)]}](QUANTITY) in [{state[randint(0, l4)]}](STATE)\n')
    f.write(f'- [{quantity[randint(0, l1)]}](QUANTITY) for the product [{product[randint(0, l5)]}](PRODUCT_NAME)\n')

f.close()
