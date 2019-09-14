# import jnius_config
# jnius_config.add_options('-Xmx256m')
from apiproxy import ApiProxy
from logger import AmbarLogger
from parsers.fileparser import FileParser
from parsers.contenttypeanalyzer import ContentTypeAnalyzer
from parsers.pdfparser import PDFParser
from contentprocessors.autotagger import AutoTagger
from model import AmbarFileContent, AmbarFileMeta
from containerprocessors.archiveprocessor import ArchiveProcessor
from containerprocessors.pstprocessor import PstProcessor
import sys

PARSE_TIMEOUT_SECONDS = 1200
pipelineId ='0'
ocrPdfSymbolsPerPageThreshold = 1000
ocrPdfMaxPageCount = 5

fileParser = FileParser(PARSE_TIMEOUT_SECONDS, ocrPdfSymbolsPerPageThreshold, ocrPdfMaxPageCount)
fileName = sys.argv[1]
writeFile = sys.argv[2]


with open(fileName, mode='rb') as file:
    fileData = file.read()

fileParserResp = fileParser.Parse(fileName, fileData)

if not fileParserResp.success:
    print('error', 'error parsing {0} {1}'.format(fileName, fileParserResp.message))
else:
    print('verbose', 'successfully parsed {0}'.format(fileName))
    with open(writeFile, "w") as text_file:
        print(fileParserResp.text, file=text_file)
    print(fileParserResp.text)