#functions to parse and  Articles' Attribute values

from found_function import directfind,allfind,sub_allfind

def get_pubdate(pubdate):
    Year = directfind(pubdate,"Year")
    Month = directfind(pubdate,"Month")
    Day = directfind(pubdate,"Day")
    return f'{Year}/{Month}/{Day}'

def get_authorname(Article):
    AuthorList = Article.find(".AuthorList")
    if AuthorList is None:
        return "","",""
    authors = AuthorList.findall(".Author") #Author (((LastName, ForeName?, Initials?, Suffix?) | CollectiveName), Identifier*, AffiliationInfo*) >

    name_list = []
    Initial_list = []
    Affiliations_list = [] #全部作者的机构
    for author in authors:
        LastName = directfind(author,'.//LastName')
        ForeName = directfind(author,'.//ForeName')
        Initials = directfind(author,'.//Initials')

        Affiliations  = sub_allfind(author,".//Affiliation")
        #作者名称进行拼接

        name_list.append(f'{LastName} {ForeName}')
        Initial_list.append(Initials)
        Affiliations_list.append(Affiliations)


    return "/".join(name_list),"/".join(Initial_list),"/".join(Affiliations_list)

def get_grant(Article):  #Grant (GrantID?, Acronym?, Agency, Country?)>
    GrantList = Article.find(".GrantList")
    if GrantList is None:
        return  "","",""
    grants = GrantList.findall(".Grant")
    GrantID_list = []
    Agency_list = []
    Country_list = []
    for grant in grants:
        GrantID = directfind(grant,'GrantID')
        Agency = directfind(grant,"Agency")
        Country = directfind(grant, "Country")
        GrantID_list.append(GrantID)
        Agency_list.append(Agency)
        Country_list.append(Country)
    return "/".join(GrantID_list), "/".join(Agency_list),"/".join(Country_list)

def get_PublicationType(Article):
    PublicationTypeList = Article.find(".PublicationTypeList")
    if PublicationTypeList is None:
        return ""
    return allfind(PublicationTypeList,"PublicationType")

def get_Chemical(MedlineCitation):
    ChemicalList = MedlineCitation.find(".ChemicalList")
    if ChemicalList is None:
        return "", ""

    RegistryNumber_list = []
    NameOfSubstance_list = []
    for Chemical in ChemicalList.findall(".Chemical"):
        RegistryNumber_list.append(directfind(Chemical,".RegistryNumber"))
        NameOfSubstance_list.append(directfind( Chemical,".NameOfSubstance"))

    return "/".join(RegistryNumber_list), "/".join(NameOfSubstance_list)

def get_MeshHeading(MedlineCitation):#MeshHeading (DescriptorName, QualifierName*)>
    MeshHeadingList = MedlineCitation.find(".MeshHeadingList")
    if MeshHeadingList is None:
        return "","","",""
    DescriptorName_list = []
    QualifierName_list = []
    for MeshHeading in  MeshHeadingList.findall( ".MeshHeading"): #可能仍然存在多个的情况
        DescriptorName_list.append(directfind(MeshHeading,".DescriptorName"))
        QualifierName_list.append(sub_allfind(MeshHeading,".QualifierName"))

    DescriptorNameMajorTopic = allfind(MeshHeadingList,".//DescriptorName[@MajorTopicYN='Y']")
    QualifierNameMajorTopic = allfind(MeshHeadingList,".//QualifierName[@MajorTopicYN='Y']")

    return "/".join(DescriptorName_list),"/".join(QualifierName_list), DescriptorNameMajorTopic,QualifierNameMajorTopic

def get_ArticleId(PubmedData):
    doi = directfind(PubmedData,".//ArticleId[@IdType='doi']")
    pubmedid = directfind(PubmedData,".//ArticleId[@IdType='pubmed']")
    return doi,pubmedid

def  get_Reference(PubmedData): #Reference (Citation, ArticleIdList?) >
    if PubmedData.find(".//Reference") is None:
        return "","",""
    References = PubmedData.findall(".//Reference") #找到所有reference
    Citation_list = []
    Citation_pubmedid_list = []
    Citation_doi_list = []
    for Reference in References:
        Citation_list.append(directfind(Reference,".Citation"))
        Citation_pubmedid_list.append(directfind(Reference,".//ArticleId[@IdType='pubmed']"))
        Citation_doi_list.append(directfind(Reference,".//ArticleId[@IdType='doi']"))

    return '/'.join(Citation_list),'/'.join(Citation_pubmedid_list),'/'.join(Citation_doi_list)

def get_Abstract(Article):  #Abstract？ Article
    if Article.find(".Abstract") is None:
        return ""
    Abstract =  Article.find(".Abstract")
    return  allfind(Abstract,".AbstractText")

def get_OtherAbstract(MedlineCitation):  #Abstract？ Article
    OtherAbstract = MedlineCitation.find(".//OtherAbstract")
    if OtherAbstract is None:
        return ""
    return allfind(OtherAbstract,".//AbstractText")

def get_Keyword (MedlineCitation): #KeywordList (Keyword+) >
    KeywordList = MedlineCitation.find(".KeywordList")

    if KeywordList is None:
        return "",""
    Keywords_MajorTopicY = allfind(MedlineCitation,".//Keyword[@MajorTopicYN = 'Y']")
    Keywords_MajorTopicN = allfind(MedlineCitation, ".//Keyword[@MajorTopicYN = 'N']")


    return Keywords_MajorTopicY,Keywords_MajorTopicN


