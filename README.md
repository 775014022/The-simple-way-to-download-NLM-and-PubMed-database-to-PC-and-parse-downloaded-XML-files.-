# The-simple-way-to-download-NLM-and-PubMed-database-to-PC-and-parse-downloaded-XML-files.-
The National Library of Medicine (NLM) offers its PubMed database data files through FTP for local downloading. 
Here's a step-by-step guide on how to download these files, as well as how to parse and analyze the data.  Additionally, I will provide python codes and tips on potential issues you may encounter during the process and their solutions.

Step 1: Downloading Data Files from NLM FTP Server
Tool: FileZilla
1.1 Open FileZilla and connect to the FTP server using the provided address: ftp.ncbi.nlm.nih.gov. Navigate to the /pubmed/baseline directory.
1.2 Select the desired .xml.gz files for downloading. Remember to set the transfer type to binary to ensure file integrity.
Potential Issues and Solutions: If the downloaded file size does not match the original, or there's a checksum error. Re-download the file and select the option to "overwrite if size differs" in FileZilla

Step2: Unzipping the Downloaded .xml.gz Files
Tool: WinRAR
Potential Issues and Solutions: If the file fails to uncompress, re-download the problematic file or perform an MD5 checksum validation of the downloaded file against the original to ensure integrity.

Step3: Parsing the XML Files and  with Python


