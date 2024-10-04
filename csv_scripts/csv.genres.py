import json

with open(r'C:\Users\user\Desktop\music\data\genres.jl', encoding='utf8') as in_file:
    with open(r"C:\Users\user\Desktop\music\csv_scripts\genres.csv", 'a', encoding='utf8') as out_file:
        out_file.write('"name";"url"\n')
        for json_line in in_file:
            line = json.loads(json_line)
            name = line['name']
            url = line['url']
            out_file.write(f'"{name}";"{url}"\n')


   
   
   