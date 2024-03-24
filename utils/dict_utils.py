from typing import Dict, Any, List


def restricted(items: List[Any], original_dict: Dict[Any, Dict[Any, Any]]) -> Dict[Any, Dict[Any, Any]]:
    '''
    Return the subdictionary of dict whose keys and values are restricted to those in items.

    Arguments:
        - items: the values to restrict to
        - dict: the original dictionary
        
    Outputs:
        - a "subdictionary" whose keys are the values in items, and each corresponding value 
        is also from items.
    '''
    if not items:
        return {}
    
    missing_items = [item for item in items if item not in original_dict]
    if missing_items:
        raise KeyError(f'These items are invalid or missing from the original dictionary: {missing_items}')
    
    restricted_dict = {}
    for item_1 in items:
        restricted_dict[item_1] = {}
        for item_2 in items:
            if item_2 in original_dict[item_1]:
                restricted_dict[item_1][item_2] = original_dict[item_1][item_2]
            else:
                raise KeyError(f'{item_2} is not a key in {original_dict[item_1]}')
    return restricted_dict
