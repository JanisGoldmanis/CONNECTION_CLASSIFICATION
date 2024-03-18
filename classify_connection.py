import rules
import sort_connection_parts


def classify_connection(branch, connection, branch_config, list_dict):
    for connection_rule in branch_config:
        classified = connection_is_valid(connection, connection_rule, list_dict, branch)
        if classified:
            if classified not in branch:
                branch[classified] = {'connections': [], 'children': {}}
            branch[classified]['connections'].append(connection)
            if 'Subclass' in connection_rule:
                subclass = connection_rule['Subclass']
                if len(subclass) > 0:
                    classify_connection(branch[classified]['children'], connection, subclass, list_dict)
            if connection.connection_type == "":
                connection.connection_type = classified
            return True
    return False


def connection_is_valid(connection, connection_rule, list_dict, branch):
    decision = connection_rule['Decision']
    name = connection_rule['Name']

    sort_method = connection_rule['Order']

    if sort_method != 'Unspecified':
        sort_method = getattr(sort_connection_parts, sort_method)
        sort_method(connection, list_dict)

    if decision == 'Null':
        return name
    condition_gate = decision['Condition']
    criteria_list = decision['Criteria']
    valid = condition_check(condition_gate, connection, criteria_list, list_dict, branch)
    if valid:
        return name
    return False


def condition_check(condition_gate, connection, criteria_list, list_dict, branch):
    """
    Condition gates = ["OR","AND"]
    """
    for criteria in criteria_list:
        result = criteria_check(connection, criteria, list_dict, branch)
        if result and condition_gate == 'OR':
            return True
        if not result and condition_gate == 'AND':
            return False
    return result


def criteria_check(connection, criteria, list_dict, branch):
    rule = criteria['Rule']

    function = getattr(rules, rule)
    return function(connection, criteria, list_dict, branch)



