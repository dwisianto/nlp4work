
import re
import logging
LOG = logging.getLogger(__name__)

from bs4 import BeautifulSoup
from pypdf import PdfReader

# constants
number_of_retry = 2
char_pos = 80

# sent_len_char = 10
# keyword matching
# KEYWORD_SPAN_LENGTH = 100


keyword_list = ["cost", "fee", "information asymetric", "price"]
keyword_pattern = re.compile("|".join(keyword_list), re.IGNORECASE)


class ExtractFromFolder:

    def extract_text_pdf_html(self, filename):
        """
        This extract text from pdf and htm files. Files ending with ".pdf"
        are read by "PdfReader". The function "text_extract()" extract text per page.
        The function "split()" is applied to remove some unwanted characters such as "\n"
        :param filename: path of the input file
        :return: extracted text and page number
        """
        if filename and filename.endswith('.pdf'):
            success = False
            pdf = None
            i = -1
            for i in range(number_of_retry):

                try:
                    pdf = PdfReader(filename)
                    print("Successfully read pdf {} {}".format(i, filename))
                    success = True
                    break
                except Exception as e:
                    print(filename, e)
                    LOG.info(filename)
                    LOG.info(e)
            if not success:
                LOG.error("Could not read PDF {} {}".format(i, filename))
                return None, None
            clean_text = []
            pg_num = []
            for i, p in enumerate(pdf.pages):
                # print("Page number: {}".format(i))
                pg_num.append(i + 1)
                text = p.extract_text().split()  # \n
                # print("Success!")
                clean_text.append(' '.join(text))
            return clean_text, pg_num
        elif filename and filename.endswith('.htm'):
            pg_num = [1]
            with open(filename, "r") as fn:
                f = fn.read()
            htm_text = BeautifulSoup(f, "lxml").text
            print("Successfully read htm {} ".format(filename))
            clean_text = htm_text
            return clean_text, pg_num
        else:
            return None, None

    def char_pos_match(self, text):
        """
        This function extract text that contains any of the keywords in keyword_list:

        :param text: str: input text
        :return: str: text containing keyword and has 80 characters on each side of the keyword
        """
        kws = re.findall(keyword_pattern, text)
        kws = [x.lower() for x in kws]

        matched_texts = []
        matches = keyword_pattern.finditer(text)

        spans = [m.span() for m in matches]
        for sp in spans:
            if sp[0] > char_pos:
                matched_texts.append(text[sp[0] - char_pos:sp[1] + char_pos])
            else:
                matched_texts.append(text[0:sp[1] + char_pos])
        return ' '.join(matched_texts), ' '.join(list(set(kws)))
