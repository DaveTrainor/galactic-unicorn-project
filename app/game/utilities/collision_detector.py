def collision_detector(element_1, element_2):
    x_min_1, x_max_1, y_min_1, y_max_1 = element_1.get_collision_properties()
    x_min_2, x_max_2, y_min_2, y_max_2 = element_2.get_collision_properties()

    if x_max_1 < x_min_2 or x_max_2 < x_min_1 or y_max_1 < y_min_2 or y_max_2 < y_min_1:
        return False
    
    return True
