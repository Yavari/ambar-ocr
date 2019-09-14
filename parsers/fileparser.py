from parsers.tikaparser import TikaParser
from parsers.pdfparser import PDFParser
from parsers.contenttypeanalyzer import ContentTypeAnalyzer

class FileParser:
    def __init__(self, ParserCallTimeoutSeconds, OcrPdfSymbolsPerPageThreshold, OcrPdfMaxPageCount):
        self.parserCallTimeoutSeconds = ParserCallTimeoutSeconds
        self.pdfParser = PDFParser(OcrPdfSymbolsPerPageThreshold, OcrPdfMaxPageCount, self.parserCallTimeoutSeconds)
        self.tikaParser = TikaParser(self.parserCallTimeoutSeconds)
        
    def Parse(self, FileName, FileData):
        if ContentTypeAnalyzer.IsPdf(FileName):
            return self.pdfParser.Parse(FileName, FileData)

        return self.tikaParser.Parse(FileName, FileData)