



# 氨基酸配置表
amino_acid_table =  {
            "PHE":{'atom_num':20, 'atoms': ['N',  'CA', 'C', 'O' ,'CB' ,'CG' ,'CD1','CD2','CE1','CE2','CZ' ,'HA' ,'HB2','HB3','HD2','HE2','HZ' ,'HE1','HD1','H'],
                   'ring':['CG', 'CD1','CD2','CE1','CE2','CZ' ,'HD1' ,'HD2','HE1','HE2','HZ']},
            "TYR":{'atom_num':21, 'atoms': ['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'OH', 'HA', 'HB3', 'HB2', 'HD2', 'HE2', 'HE1', 'HD1', 'HH', 'H'],
                   'ring':['CG', 'CD1','CD2','CE1','CE2','CZ', 'OH', 'HD1', 'HD2','HE1','HE2','HH']},
            "TRP":{'atom_num':24, 'atoms': ['N',  'CA', 'C',  'O',  'CB', 'CG', 'CD1', 'CD2', 'NE1', 'CE2', 'CE3', 'CZ2', 'CZ3', 'CH2','HA', 'HB2','HB3','HE1','HD1','HZ2','HH2','HZ3','HE3','H' ],
                    'ring':['CG', 'CD1','CD2','CE2','CE3','CZ2', 'CZ3','CH2', 'NE1', 'HD1', 'HE1','HE3','HZ2','HZ3','HH2']}
}

# 氨基酸类型
amino_acid_type={'PHE': 'phe', 'TYR':'tyr', 'TRP': 'trp'}