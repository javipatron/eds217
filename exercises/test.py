print("Hello World!")

import pandas as pd


df3 = pd.DataFrame({"Rivers": ["Amazon", "Congo", "Yangtze", "Mississippi"],
                    "Length(km)": [6400,4371,6410,3730],
                     "Drainage Area (km2)": [7050000,4014500,1808500,3202230]})
                     

df_4 = pd.DataFrame({"Rivers":["Zambezi", "Mekong", "Murray", "Rhône", "Cubango"], 
                     "Length(km)":[2574,4023,2508,813,1056],
                     "Drainage area (km2)": [1331000,811000,1061469,98000,530000]})


print(df_3)
print(df_4)


df_5 = pd.concat([df_3,df_4])

df_5.reset_index(inplace=True, drop=True)


print(df_5)

df_6 = df_5.assign(Mouth = ["Atlantic Ocean", "Atlantic Ocean", "East China Sea", "Gulf of Mexico", "Indian Ocean", 
                            "South China Sea", "Southern Ocean", "Mediterranean Sea", "Okavango Delta"],
                   Source = ["Rio Mantaro", "Lualaba River", "Jianggendiru Glacier", "Lake Itasca", "Miombo Woodlands",
                             "Lasagongma Spring", "Australian Alps", "Rhône Glacier", "Bié Plateau"],
                   Continent = ["South America", "Africa", "Asia", "North America", "Africa", 
                                "Asia", "Oceania", "Europe", "Central America"])


df_6