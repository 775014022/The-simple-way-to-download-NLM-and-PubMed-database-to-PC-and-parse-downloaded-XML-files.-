#read the XML in the folder and do xml_to_csv to parse and save XML to xlsx(not csv).
from lxml import etree
import pandas as pd

from parse import xml_to_csv
path = "E:\\DataForPaper\Pubmed\correct\pubmed24n"
target = ""
if __name__ == '__main__':
    for i in  range(120,1220):
        print(i)
        formatted_number = "{:04d}".format(i)
        path_i = "E:\\DataForPaper\Pubmed\correct\pubmed24n" +formatted_number +".xml"
        target_i = "E:\\DataForPaper\Pubmed\\xlsx\pubmed24n" + formatted_number +".xlsx"
        xml_to_csv(path_i,target_i)
