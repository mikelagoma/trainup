#!/usr/bin/python
import pandas as pd
import numpy as np
import os
import argparse

script_dir = os.path.dirname(os.path.realpath(__file__))

def parse_args():
    parser = argparse.ArgumentParser(description='create json formatted object from csv files')

    parser.add_argument('-o', '--output', dest='output', metavar='<output directory>', type=str,
        default=os.path.join(script_dir, '..', 'public', 'data'),
        help='directory to dump output files')
    return parser.parse_args()

def create_skill_json(df, output_dir):
    df.dropna(inplace=True)
    with open(os.path.join(output_dir, 'skills.json'), 'w+') as file:
        # for skill in dfs.Skill.unique():
        #     skill = skill.replace('*','')
        file.write('{\n  "fields" : [')
        for idx, field in enumerate(df.Field.unique()):
            if idx == 0:
                file.write('\n    {')
            else:
                file.write(',\n    {')
            file.write('\n      "name" : "' + field + '",')
            file.write('\n      "positions" : [')
            # Filter df to this field
            df_field = df[df.Field == field]
            for idx, position in enumerate(df_field.Position.unique()):
                if idx == 0:
                    file.write('\n        {')
                else:
                    file.write(',\n        {')
                file.write('\n          "name" : "' + position + '",')
                file.write('\n          "skills" : [')
                # Filter df to this position
                df_position = df[df.Position == position].copy().reset_index()
                for idx, row in df_position.iterrows():
                    if idx == 0:
                        file.write('\n            {')
                    else:
                        file.write(',\n            {')
                    file.write('\n              "name" : "' + str(row['Skill']) + '"')
                    file.write('\n            }')
                file.write('\n          ]')
                file.write('\n        }')
            file.write('\n      ]')
            file.write('\n    }')
        file.write('\n  ]')
        file.write('\n}')
    file.close()
    return

def create_resource_json(df, output_dir):
    df.dropna(inplace=True)
    with open(os.path.join(output_dir, 'resources.json'), 'w+') as file:
        # for skill in dfs.Skill.unique():
        #     skill = skill.replace('*','')
        file.write('{\n  "skills" : [')
        for idx, skill in enumerate(df.Skill.unique()):
            if idx == 0:
                file.write('\n    {')
            else:
                file.write(',\n    {')
            file.write('\n      "name" : "' + skill + '",')
            file.write('\n      "resources" : [')
            df_skill = df[df.Skill == skill].copy().reset_index()
            for idx, row in df_skill.iterrows():
                if idx == 0:
                    file.write('\n        {')
                else:
                    file.write(',\n        {')
                file.write('\n          "name" : "' + str(row['Resource Name']) + '",')
                file.write('\n          "link" : "' + str(row['Resource Link']) + '"')
                file.write('\n        }')
            file.write('\n      ]')
            file.write('\n    }')
        file.write('\n  ]')
        file.write('\n}')
    file.close()
    return

def main():
    args = parse_args()
    skills_df = pd.read_csv(os.path.join(script_dir, '..', 'skills.csv'))
    resources_df = pd.read_csv(os.path.join(script_dir, '..', 'resources.csv'))
    create_skill_json(skills_df, args.output)
    create_resource_json(resources_df, args.output)

if __name__ == '__main__':
    main()