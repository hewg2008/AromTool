import os


class Path:

    @staticmethod
    def get_ligand_path(src_path, f):
        return os.path.join(src_path, f, f + '_ligand.mol2')

    @staticmethod
    def get_protein_path(src_path, f):
        return os.path.join(src_path, f, f + '_protein.pdb')

    @staticmethod
    def getBasename(filename):
        return os.path.basename(filename)

    @staticmethod
    def getfilename(filename, only_name=False):
        name = os.path.splitext(filename)[0]
        if only_name:
            return name.split('\\')[-1]
        return name

    @staticmethod
    def get_extension(filename):
        return os.path.splitext(filename)[1]
