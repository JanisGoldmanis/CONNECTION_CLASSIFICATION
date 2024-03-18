import operator


def PropertyInList(connection, rule, list_dict, branch):
    part = rule['Part']
    property = rule['Property']
    list_of_properties = rule['List']
    list_of_properties = list_dict[list_of_properties]
    part = getattr(connection, part)
    property = getattr(part, property)
    if property in list_of_properties:
        return True
    return False


def PropertyNotInList(connection, rule, list_dict, branch):
    part = rule['Part']
    property = rule['Property']
    list_of_properties = rule['List']
    list_of_properties = list_dict[list_of_properties]
    part = getattr(connection, part)
    property = getattr(part, property)
    if property not in list_of_properties:
        return True
    return False


def ValueNumericCheck(connection, rule, list_dict, branch):
    part = rule['Part']
    property = rule['Property']
    condition = rule['Condition']
    value = rule['Value']

    if part == 'connection':
        part = connection
    else:
        part = getattr(connection, part)

    property = getattr(part, property)
    expression = str(property) + condition + str(value)

    result = eval(expression)
    return result


def TwoPropertyCheck(connection, rule, list_dict, branch):
    part1 = rule['Part']
    part2 = rule['Part2']
    property1 = rule['Property']
    property2 = rule['Property2']
    condition = rule['Condition']

    if part1 == 'connection':
        part1 = connection
    else:
        part1 = getattr(connection, part1)

    if part2 == 'connection':
        part2 = connection
    else:
        part2 = getattr(connection, part2)

    property1 = getattr(part1, property1)
    property2 = getattr(part2, property2)

    expression = str(property1) + condition + str(property2)

    result = eval(expression)

    return result


def PropertySet(connection, rule, list_dict, branch):
    parts = rule['Part']
    properties = rule['Property']

    name = ""

    result = ""
    result_description = ""

    for i in range(len(parts)):

        part_str = parts[i]
        property = properties[i]

        if part_str == 'connection':
            part = connection
        else:
            part = getattr(connection, part_str)

        attribute = str(getattr(part, property))
        result += attribute + " "
        result_description += part_str + '.' + property + " "

    property = result + "|" + result_description

    if property not in branch:
        branch[property] = {'connections': [], 'children': {}}

    branch[property]['connections'].append(connection)

    return False


def PartIsHorizontal(connection, rule, list_dict, branch):
    part = rule['Part']
    part = getattr(connection, part)

    if abs(part.start_z - part.end_z) < 10:
        return True
    return False


def PartIsVertical(connection, rule, list_dict, branch):
    part = rule['Part']
    part = getattr(connection, part)

    if abs(part.start_x - part.end_x) < 10 and abs(part.start_y - part.end_y) < 10:
        return True
    return False
