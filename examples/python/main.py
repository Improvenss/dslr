# LINK: https://saturncloud.io/blog/python-spyder-display-all-columns-of-a-pandas-dataframe-in-describe/#:~:text=describe()%20method%20in%20Pandas,and%20maximum%20of%20the%20columns.
# import pandas as pd

# # Load the CSV file
# file_path = '/Users/yuandre/Desktop/dslr/datasets/dataset_test.csv'
# data = pd.read_csv(file_path)

# # Save DataFrame to a text file
# data.to_csv('data_output.txt', index=False, sep='\t')

# print("Data has been written to 'data_output.txt'")

# -----------------------------------------------------------------------------

import pandas as pd

pd.set_option('display.max_columns', None) # For show all cloumns. If delete this line showing like your screen resolution.

# Create a simple dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 4, 5, 6],
        'C': [3, 4, 5, 6, 7],
        'D': [1, 2, 3, 4, 5],
        'E': [2, 3, 4, 5, 6],
        'F': [3, 4, 5, 6, 7],
        'G': [1, 2, 3, 4, 5],
        'H': [2, 3, 4, 5, 6],
        'I': [3, 4, 5, 6, 7],
        'J': [1, 2, 3, 4, 5],
        'K': [2, 3, 4, 5, 6],
        'L': [3, 4, 5, 6, 7],
        'M': [1, 2, 3, 4, 5],
        'N': [2, 3, 4, 5, 6],
        'O': [3, 4, 5, 6, 7],
        'P': [1, 2, 3, 4, 5],
        'Q': [2, 3, 4, 5, 6],
        'R': [3, 4, 5, 6, 7]
})

print(df.describe())
# Inspecting to .describe() function.
