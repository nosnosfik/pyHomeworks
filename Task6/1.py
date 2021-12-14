def combine_dicts(*dicts):
    final_dict = {}

    for dictionary in dicts:
        for key, value in dictionary.items():
            if not key.isalpha() or len(key) > 1:
                raise KeyError()
            if type(value) is not int:
                raise ValueError()
            if key not in final_dict:
                final_dict[key] = 0

            final_dict[key] += value

    return final_dict