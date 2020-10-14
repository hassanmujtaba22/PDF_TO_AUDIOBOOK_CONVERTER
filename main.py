import pyttsx3
import PyPDF2
book = open("book.pdf", "rb")
speacker = pyttsx3.init()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
# for num in range(1, 1):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     speacker.say(text)
#     speacker.runAndWait()
page = pdfReader.getPage(1)
text = page.extractText()
speacker.say(text)
speacker.runAndWait()


# speacker = pyttsx3.init()
# speacker.say("Hello World!")
# speacker.runAndWait()