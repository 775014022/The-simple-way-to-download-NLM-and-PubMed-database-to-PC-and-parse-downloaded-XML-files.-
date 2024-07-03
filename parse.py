#Parse singal XML file and save data to xlsx

from lxml import etree
import pandas as pd
from found_function import directfind,allfind,sub_allfind
import openpyxl
from get_function import get_pubdate,get_authorname,get_grant,get_PublicationType,get_Chemical,get_MeshHeading,get_Abstract,get_OtherAbstract,get_Keyword,get_ArticleId,get_Reference
def xml_to_csv(file, target):
    data = etree.parse(file)
    root = data.getroot()
    pubmedarticles = root.findall(".PubmedArticle")

    PMID_list = []
    pub_date_list = []
    Journal_Title_list = []
    ArticleTitle_list = []
    Authorname_list = []
    Initials_list = []
    Affiliation_list = []
    Language_list = []
    GrantID_list = []
    GrantAgency_list = []
    GrantCountry_list = []
    PublicationType_list = []
    Country_list = []
    MedlineTA_list = []
    NlmUniqueID_list = []
    ISSNLinking_list = []
    RegistryNumber_list = []
    NameOfSubstance_list = []
    DescriptorName_list = []
    QualifierName_list = []
    DescriptorNameMajorTopic_list = []
    QualifierNameMajorTopic_list = []
    Abstract_list = []
    OtherAbstract_list = []
    Keywords_MajorTopicY_list = []
    Keywords_MajorTopicN_list = []
    PublicationStatus_list = []
    pubmedid_list = []
    doi_list = []
    Citation_list = []
    Citatio_pumedid_list = []
    Citatio_doi_list = []


    for pubmedarticle in pubmedarticles:  # PubmedArticle (MedlineCitation, PubmedData?)>
        MedlineCitation = pubmedarticle.find(".MedlineCitation")
        '''
               MedlineCitation (PMID, DateCompleted?, DateRevised?, Article, 
                                        MedlineJournalInfo, ChemicalList?, SupplMeshList?,CitationSubset*, 
                                        CommentsCorrectionsList?, GeneSymbolList?, MeshHeadingList?, 
                                        NumberOfReferences?, PersonalNameSubjectList?, OtherID*, OtherAbstract*, 
                                        KeywordList*, CoiStatement?, SpaceFlightMission*, InvestigatorList*, GeneralNote*)>

        '''
        PMID = directfind(MedlineCitation,".PMID")

        Article = MedlineCitation.find(".Article")  # Article PubModel
        '''
               Article (Journal,ArticleTitle,((Pagination, ELocationID*) | ELocationID+),
                                Abstract?,AuthorList?, Language+, DataBankList?, GrantList?,
                                PublicationTypeList, VernacularTitle?, ArticleDate*) >
        '''

        Journal = Article.find(".Journal")  # Journal (ISSN?, JournalIssue, Title?, ISOAbbreviation?)>
        JournalIssue = Journal.find(".JournalIssue")
        pub_date = get_pubdate(JournalIssue.find(".PubDate"))

        Journal_Title =  directfind(Journal,".Title")
        ArticleTitle =directfind(Article,".ArticleTitle")

        Authorname, Initials, Affiliation = get_authorname(Article)
        Language =directfind(Article,".Language")
        GrantID, GrantAgency, GrantCountry = get_grant(Article)  # 不一定全部存在

        PublicationType = get_PublicationType(Article)

        MedlineJournalInfo = MedlineCitation.find(".MedlineJournalInfo")
        Country = directfind(MedlineJournalInfo,"Country")
        MedlineTA =directfind(MedlineJournalInfo,"MedlineTA")
        NlmUniqueID = directfind(MedlineJournalInfo,"NlmUniqueID")
        ISSNLinking = directfind(MedlineJournalInfo,"ISSNLinking")

        # ChemicalList
        RegistryNumber, NameOfSubstance = get_Chemical(MedlineCitation)

        # CitationSubset

        # MeshHeadingList
        DescriptorName, QualifierName, DescriptorNameMajorTopic, QualifierNameMajorTopic = get_MeshHeading(
            MedlineCitation)

        # Abstract？ Article
        Abstract = get_Abstract(Article)

        # OtherAbstract* MedlineCitation
        OtherAbstract = get_OtherAbstract(MedlineCitation)

        Keywords_MajorTopicY, Keywords_MajorTopicN = get_Keyword(MedlineCitation)

        PubmedData = pubmedarticle.find(".PubmedData")  # PubmedData (History?, PublicationStatus, ArticleIdList, ObjectList?, ReferenceList*) >
        if PubmedData is None:
            PublicationStatus = ""
            pubmedid = ""
            doi = ""
        else:
            PublicationStatus = PubmedData.find(".PublicationStatus").text
            doi, pubmedid = get_ArticleId(PubmedData)

        Citation, Citatio_pumedid, Citatio_doi = get_Reference(PubmedData)
        PMID_list.append(PMID)
        pub_date_list.append(pub_date)
        Journal_Title_list.append(Journal_Title)
        ArticleTitle_list.append(ArticleTitle)
        Authorname_list.append(Authorname)
        Initials_list.append(Initials)
        Affiliation_list.append(Affiliation)
        Language_list.append(Language)
        GrantID_list.append(GrantID)
        GrantAgency_list.append(GrantAgency)
        GrantCountry_list.append(GrantCountry)
        PublicationType_list.append(PublicationType)
        Country_list.append(Country)
        MedlineTA_list.append(MedlineTA)
        NlmUniqueID_list.append(NlmUniqueID)
        ISSNLinking_list.append(ISSNLinking)
        RegistryNumber_list.append(RegistryNumber)
        NameOfSubstance_list.append(NameOfSubstance)
        DescriptorName_list.append(DescriptorName)
        QualifierName_list.append(QualifierName)
        DescriptorNameMajorTopic_list.append(DescriptorNameMajorTopic)
        QualifierNameMajorTopic_list.append(QualifierNameMajorTopic)
        Abstract_list.append(Abstract)
        OtherAbstract_list.append(OtherAbstract)
        Keywords_MajorTopicY_list.append(Keywords_MajorTopicY)
        Keywords_MajorTopicN_list.append(Keywords_MajorTopicN)
        PublicationStatus_list.append(PublicationStatus)
        pubmedid_list.append(pubmedid)
        doi_list.append(doi)
        Citation_list.append(Citation)
        Citatio_pumedid_list.append(Citatio_pumedid)
        Citatio_doi_list.append(Citatio_doi)

    update_dict = {
        "PMID": PMID_list,
        "pub_date": pub_date_list,
        "Journal_Title": Journal_Title_list,
        "ArticleTitle": ArticleTitle_list,
        "Authorname": Authorname_list,
        "Initials": Initials_list,
        "Affiliation": Affiliation_list,
        "Language": Language_list,
        "GrantID": GrantID_list,
        "GrantAgency": GrantAgency_list,
        "GrantCountry": GrantCountry_list,
        "PublicationType": PublicationType_list,
        "Country": Country_list,
        "MedlineTA": MedlineTA_list,
        "NlmUniqueID": NlmUniqueID_list,
        "ISSNLinking": ISSNLinking_list,
        "RegistryNumber": RegistryNumber_list,
        "NameOfSubstance": NameOfSubstance_list,
        "DescriptorName": DescriptorName_list,
        "QualifierName": QualifierName_list,
        "DescriptorNameMajorTopic": DescriptorNameMajorTopic_list,
        "QualifierNameMajorTopic": QualifierNameMajorTopic_list,
        "Abstract": Abstract_list,
        "OtherAbstract": OtherAbstract_list,
        "Keywords_MajorTopicY": Keywords_MajorTopicY_list,
        "Keywords_MajorTopicN": Keywords_MajorTopicN_list,
        "PublicationStatus": PublicationStatus_list,
        "pubmedid": pubmedid_list,
        "doi": doi_list,
        "Citation": Citation_list,
        "Citatio_pumedid": Citatio_pumedid_list,
        "Citatio_doi": Citatio_doi_list,
    }

    data = pd.DataFrame(update_dict)
    data.to_excel(target, sheet_name= "Sheet1")


if __name__ == '__main__':
    xml_to_csv("C:\\Users\lhthn\Desktop\pubmed24n1213.xml","test.xlsx")
