import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    dfs = pd.read_csv(os.path.join(script_dir, '..', 'skills.csv'))
    dfr = pd.read_csv(os.path.join(script_dir, '..', 'resources.csv'))
    dfr.dropna(inplace=True)
    with open(os.path.join(script_dir, '..', 'resources.json'), 'w+') as file:
        # for skill in dfs.Skill.unique():
        #     skill = skill.replace('*','')
        file.write('{\n  "skills" : [\n')
        for skill in dfr.Skill.unique():
            file.write('    {\n')
            file.write('      "name" : "' + skill + '",\n')
            file.write('      "resources" : [\n')
            dfrs = dfr[dfr.Skill == skill]
            for idx, row in dfrs.iterrows():
                file.write('        {\n')
                file.write('          "name" : "' + str(row['Resource Name']) + '",\n')
                file.write('          "link" : "' + str(row['Resource Link']) + '"\n')
                file.write('        },\n')
            file.write('      ]\n')
            file.write('    },\n')
        file.write('  ]\n')
        file.write('}')

if __name__ == '__main__':
    main()