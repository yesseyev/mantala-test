def roman_to_int(s):
    roman_to_dec = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_reducers_map = {
        'I': ['V', 'X'],
        'X': ['L', 'C'],
        'C': ['D', 'M']
    }

    reducers = roman_reducers_map.keys()
    result = 0
    size = len(s)
    i = 0
    while i != len(s):
        val = roman_to_dec[s[i]]
        if i != (size - 1) and s[i] in reducers and s[i + 1] in roman_reducers_map[s[i]]:
            val = roman_to_dec[s[i + 1]] - val
            i += 1
        result = result + val
        i += 1

    return result
