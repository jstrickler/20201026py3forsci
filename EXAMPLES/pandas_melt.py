#!/usr/bin/env python
import pandas as pd

columns = ['year', 'US', 'UK', 'CA', 'MX ']

df = pd.DataFrame(
    [
        ['1950', 157813000, 50616000, 13737000, 27737000],
        ['2015', 321225000, 60566000, 34419000, 119175000]
    ], columns=columns)  # <1>

print("Original:")
print(df, '\n')

melted = df.melt(
    id_vars=['year'],
    value_vars=['US', 'UK', 'CA', 'MX'],
    var_name='country', value_name='population'
)  # <2>

print(melted)


# melted.sort_values(by='year', inplace=True)  # <3>
#
# print("Sorted:")
# print(melted, '\n')


