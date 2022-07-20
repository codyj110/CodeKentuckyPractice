###########################################
def extract_rows(pdf):
    rows = []
    for i, row in pdf.iloc[1:2].iterrows():
        # create a list representing the dataframe row
        rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
                           row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
                           row['TOTAL (All Selected Census Tracts)']]
    return rows

# iterate over the rows
# for i, row in pdf1950.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_1950_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf1960.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_1960_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf1970.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_1970_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf1980.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_1980_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf1990.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_1990_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf2000.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_2000_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf2010.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_2010_rows = [row['Census Tract 9, Hamilton County, Ohio'], row['Census Tract 10, Hamilton County, Ohio'],
#                        row['Census Tract 16, Hamilton County, Ohio'], row['Census Tract 17, Hamilton County, Ohio'],
#                        row['TOTAL (All Selected Census Tracts)']]
#
#
# for i, row in pdf2020.iloc[1:2].iterrows():
#     # create a list representing the dataframe row
#     White_2020_rows = [row['Census Tract 9 Total'], row['Census Tract 10 Total'],
#                        row['Census Tract 16 Total'], row['Census Tract 17 Total'],
#                        row['TOTAL (All Selected Census Tracts)']]



# append row list to ls
White_1950_list.append(extract_rows(pdf1950))
White_1960_list.append(extract_rows(pdf1960))
White_1970_list.append(extract_rows(pdf1970))
White_1980_list.append(extract_rows(pdf1980))
White_1990_list.append(extract_rows(pdf1990))
White_2000_list.append(extract_rows(pdf2000))
White_2010_list.append(extract_rows(pdf2010))
White_2020_list.append(extract_rows(pdf2020))
#############################################