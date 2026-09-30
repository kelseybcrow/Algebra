    
'''
next problem
'''
# Find the range of the quadratic function

    f(x)   =   3x² + 6x + (-1)
    # the range of a quadratic is determined by the vertex

    a = 3
    b = 6
    c = (-1)

# TODO: EXAM_QUADRATIC_VERTEX_FORMULA

    vertex_x = (-b) / (2 * a)

    vertex_x = (-6) / (2 * 3)
    vertex_x = (-6) / 6
    vertex_x = (-1)

    vertex_y = a * vertex_x² + b * vertex_x + c









    # For f(x) = 3x² + 6x - 1, a = 3, b = 6, c = -1
    a = 3
    b = 6
    c = -1
    
    # Vertex formula: x = -b/(2a)
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    
    # Since a > 0, the parabola opens upwards, so the range is [vertex_y, ∞)
    range_of_function = (vertex_y, float('inf'))
    print("Range of the function:", range_of_function)