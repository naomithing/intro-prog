import random


def cars():
    cars = ['BMW','Tesla', 'Ford', 'Bugatti', 'Mercedes', 'Nissan', 'Apollo']
    print('The list of cars: ', cars)
    cars.append('Mustang')
    cars.append('Suzuki')
    print('some cars were added: ', cars)
    cars.remove('BMW')
    cars.remove('Mercedes')
    random.shuffle(cars)
    print("Updates list", cars)
cars()
