import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    x = 3
    y = 6

    output = methods.som(x, y)

    assert output == 9

def test_sub():
    x = 3
    y = 6

    output = methods.sub(x, y)

    assert output == -3

def test_mult():
    x = 3
    y = 6

    output = methods.mult(x, y)

    assert output == 18

def test_div():
    x = 6
    y = 3

    output = methods.div(x, y)

    assert output == 2