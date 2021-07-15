import glob
import re
import pandas as pd
import os


class GrepPY:

    def __init__(self, sourcePath: str) -> None:
        # import glob
        self.USList = [[" Andrea Rendina "], [" Antonio Falabella "], [" Federico Fornari "], [" Lucia Morganti "], [" Daniele Cesini "],[" Carmelo Pellegrino "], [" Vincenzo Rega "], [" Claudia Cavallaro "], [" Daniele Lattanzio "], [" Francesco Minarini "], [" Elena Corni "], [" Federico Versari "], [" Matteo Tenti "]]
        self.filename = os.path.join(os.getcwd(), sourcePath)

        self.uidRegex = '(?<=uid:)\s[a-z.A-Z0-9]+\s'
        self.cnRegex = '(?<=cn:)(.*)(?=mail:)'
        self.mailRegex = "[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
        # print(self.fileList)

    def load(self) -> None:
        with open(self.filename) as inputStream:
            self.db = inputStream.readlines()
            print(self.db[0])

    def grep(self) -> None:
        # import re

        self.uids = []
        self.cns = []
        self.mails = []

        for entry in range(len(self.db)):

            if re.findall(self.cnRegex, self.db[entry]) in self.USList:
                pass
            else:
                #uidRegex = '(?<=uid:)\s[a-z.A-Z0-9]+\s'
                self.uids.append(re.findall(self.uidRegex, self.db[entry]))

                #cnRegex = '(?<=cn:)(.*)(?=mail:)'
                self.cns.append(re.findall(self.cnRegex, self.db[entry]))

                #mailRegex = "[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
                self.mails.append(re.findall(self.mailRegex, self.db[entry]))

        #print(self.uids)
        # print(self.cns)
        # print(self.mails)

    def to_CSV(self, destName: str, separator: str):
        # import pandas as pd

        self.UIDS = []
        self.CNS = []
        self.MAILS = []

        for index in range(0, len(self.db)):
            try:
                self.UIDS.append(self.uids[index][0])
            except IndexError:
                self.UIDS.append("N/A")
            try:
                self.CNS.append(self.cns[index][0])
            except IndexError:
                self.CNS.append("N/A")
            try:
                self.MAILS.append(self.mails[index][0])
            except IndexError:
                self.MAILS.append("N/A")

        data = {"uid":self.UIDS, "cn":self.CNS, "mail":self.MAILS}
        database = pd.DataFrame(data)
        database.to_csv(destName, sep=separator, index=False)


class BatchGrepPY(GrepPY):

    def __init__(self):
        self.USList = [[" Andrea Rendina "], [" Antonio Falabella "], [" Federico Fornari "], [" Lucia Morganti "], [" Daniele Cesini "],[" Carmelo Pellegrino "], [" Vincenzo Rega "], [" Claudia Cavallaro "], [" Daniele Lattanzio "], [" Francesco Minarini "], [" Elena Corni "], [" Federico Versari "], [" Matteo Tenti "]]
        self.uidRegex = '(?<=uid:)\s[a-z.A-Z0-9]+\s'
        self.cnRegex = '(?<=cn:)(.*)(?=mail:)'
        self.mailRegex = "[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

        pass

    def load(self, fileName:str): # -> database:
        with open(fileName) as inputStream:
            self.db = inputStream.readlines()

    def BatchGrep(self):
        # import re

        self.uids = []
        self.cns = []
        self.mails = []

        for entry in range(len(self.db)):

            if re.findall(self.cnRegex, self.db[entry]) in self.USList:
                pass
            else:
                #uidRegex = '(?<=uid:)\s[a-z.A-Z0-9]+\s'
                self.uids.append(re.findall(self.uidRegex, self.db[entry]))

                #cnRegex = '(?<=cn:)(.*)(?=mail:)'
                self.cns.append(re.findall(self.cnRegex, self.db[entry]))

                #mailRegex = "[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
                self.mails.append(re.findall(self.mailRegex, self.db[entry]))



print("choose your option:\n")
print("1 Process a single file\n")
print("2 Process a batch\n")


choice = input("> ")

if choice == "1":
    source = input("type in the file's path:")
    Grep = GrepPY(str(source))
    Grep.load()
    Grep.grep()
    dst = input("specify destination file path:")
    Grep.to_CSV(destName=dst,separator=";")

else:
    # source = input("set source batch folder:")
    dst = input("specify destination folder:")

    fileList = os.listdir(os.getcwd()+"/prova")
    #finalFolder = os.path.join(os.getcwd(), "prova/outputbatch")

    if not os.path.exists(dst):
        os.mkdir(dst)
    else:
        print("folder already exists!")

    print("files will be saved in "+ str(dst))


    BatchGrep = BatchGrepPY()
    for file in fileList:
        try:
            BatchGrep.load(os.getcwd()+"/prova/"+str(file))
        except IsADirectoryError:
            pass
        BatchGrep.BatchGrep()
        BatchGrep.to_CSV(destName=dst+"/"+str(file)+".csv", separator=";")
