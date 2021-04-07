import pandas as pd


class ExcelUtil:

    @staticmethod
    def write_excel(save_path, content, columns=None):
        df = pd.DataFrame(content, columns=columns)
        df.to_excel(save_path, index=False)
        return df