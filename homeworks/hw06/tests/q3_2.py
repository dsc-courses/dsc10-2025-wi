test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> chocolate.shape == (2693, 2) and set(chocolate.columns) == set(['Sweetness', 'Rating'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(chocolate.get('Sweetness').unique() == np.array(['Not Sweet', 'Sweet'])) # Make sure the 'Sweetness' values are either `Sweet` or `Not "
                                               'Sweet`\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> (chocolate.get('Sweetness') == 'Sweet').sum() == 339 # You may have an error in your label_sweet function.\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
