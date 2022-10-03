import pandas as pd

path = "datasets\clean_dataset.csv"
file = pd.read_csv(path)

ICT = ["Computer Science",
"Computer Technology",
"Computer Engineering",
"Computer Information Systems",
"Computer Professional",
"Computer Programming",
"Software Development",
"Software Engineering",
"Data Analytics",
"Data Science",
"Information Technology",
"InformationTechnology",
"Information Systems",
"Information System Management",
"Management information system",
"Management Information Systems",
"Computing",
"Technology",
"System Engineering",
"Geographical Info. Science",
"CISA",
"IS",
"Information and Communication Technology",
"IT Engineering",
"Telecommunication Engineering",
"Telecom Engineering",
"Network Security",
"Networking",
"Telecoms and Networking",
]

# Remove Non-ICT data from dataset
for index,row in file.iterrows():
    found = False
    data = file.loc[index:index,"Major 1": "Major 6"]
    for item in data:
        if data[item][index] in ICT:
            found = True
            break
    
    if found == False: 
        file = file.drop(labels=index,axis=0)

# Replace Non-ICT major in ICT dataset with empty string
for index,row in file.iterrows():
    data = file.loc[index:index,"Major 1": "Major 6"]
    for item in data:
        if data[item][index] not in ICT:
            file.loc[index:index,item:item] = ""

# remove index
file = file.reset_index(drop=True)

# drop column that doesn't have anything
for item in ["Major 1","Major 2","Major 3","Major 4","Major 5","Major 6"]:
    if (file[item].values == '').sum() == len(file):
        file = file.drop(columns=item)

# write to csv file
file.to_csv("datasets/clean_ict.csv",index=False)
