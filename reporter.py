'''Export contact report depicting contact type, distance, angle, energy.'''

import pandas as pd
import itertools


class ReportManager:

    @staticmethod
    def export(save_path, contact_builder_list):
        """One pdb one dataframe."""
        contact_dataset = []  # dataset
        contact_dataset_summary=[]
        #if len(contact_builder_list) == 0 :
        if type(contact_builder_list) != None :
            for contact_builder in contact_builder_list:
                contacts_list = contact_builder.contacts
                contacts_breakdown = []
                contacts_summary=[]
                enery_total = 0
                for index, contact in enumerate(contacts_list):
                   contacts_breakdown.append([contact.contact_type, contact.distance, contact.angle, contact.energy])
                   enery_total += contact.energy
                # contacts_summary = list(itertools.chain.from_iterable(contacts_breakdown))
                contacts_summary.append(contact_builder.pdb_code)  # pdb_code
                contacts_summary.append(len(contacts_list))  # 接触长度
                contacts_summary.append(contact.contact_type)
                contacts_summary.append(enery_total)

                for contact in contacts_breakdown:
                    contact.insert(0, contact_builder.pdb_code)
                    # contact.insert(1, len(contacts_list))  # 接触个数
                    df_breakdown = pd.DataFrame([contact], columns=['PDB_Code',
                                                          'Contact_type',
                                                          'Contact_Distance',
                                                          'Contact_Angle',
                                                          'Contact_Energy'
                                                          ])

                    contact_dataset.append(df_breakdown)
                df_breakdown = pd.concat(contact_dataset)

                df_summary=pd.DataFrame([contacts_summary], columns=['PDB_Code', 'Contact_Number', 'Contact_type','Contact_Energy'])
                contact_dataset_summary.append(df_summary)
                df_summary=pd.concat(contact_dataset_summary)

            writer = pd.ExcelWriter(save_path)

            df_breakdown.to_excel(writer, sheet_name="breakdown", index=False)
            df_summary.to_excel(writer, sheet_name="summary", index=False)
            worksheet1 = writer.sheets["breakdown"]
            worksheet1.set_column('A:U', 18)
            worksheet2 = writer.sheets["summary"]
            worksheet2.set_column('A:U', 18)
            writer.save()