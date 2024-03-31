import speech_recognition as SR
a=SR.Recognizer()
import webbrowser
import PyPDF2
with SR.Microphone() as source:
    print("Speak Anything:")
    audio = a.listen(source)
    try:
        text = a.recognize_google(audio)
        print("You Said:", text)
    except:
        print("Sorry! could not recognize your voice")
    list=[" a) You want web search?"," b) You want offline Data?"," c) You want Image Sketch Converter?"," d) You Want to Open any folder?"]
    for i in list:
        print(i,'\n')
    t=input("Enter Your Choice:")
    if t.lower() == "a" :
        text = a.recognize_google(audio)
        webbrowser.open("https://google.co.in/search?q="+text)
    elif t.lower()=="b":
        if text.upper() == "MADHYA PRADESH" or text.upper() == "MP":
            pdfFileObj = open('C:\\Users\\asus\\Downloads\\MADHYA PRADESH.pdf', 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            # printing number of pages in pdf file
            print(len(pdfReader.pages))
            # creating a page object
            pageObj = pdfReader.pages[0]
            # extracting text from page
            print(pageObj.extract_text())
            # closing the pdf file object
            pdfFileObj.close()
            # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if text.upper() == "BIHAR":
            pdfFileObj = open('C:\\Users\\asus\\Downloads\\bihar.pdf', 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            # printing number of pages in pdf file
            print(len(pdfReader.pages))
            # creating a page object
            pageObj = pdfReader.pages[0]
            # extracting text from page
            print(pageObj.extract_text())
            # closing the pdf file object
            pdfFileObj.close()
            # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if text.upper() == "DELHI":
            pdfFileObj = open('C:\\Users\\asus\\Downloads\\delhi.pdf', 'rb')
            pdfReader = PdfReader(pdfFileObj)
            # printing number of pages in pdf file
            print(len(pdfReader.pages))
            # creating a page object
            pageObj = pdfReader.pages[0]
            # extracting text from page
            print(pageObj.extract_text())
            # closing the pdf file object
            pdfFileObj.close()
            # pdfReader = PdfReader(pdfFileObj)
        if text.upper() == "ANDHRA PRADESH":
            pdfFileObj = open('C:\\Users\\asus\\Downloads\\ANDHRA PRADESH.pdf', 'rb')
            pdfReader = PdfReader(pdfFileObj)
            # printing number of pages in pdf file
            print(len(pdfReader.pages))
            # creating a page object
            pageObj = pdfReader.pages[0]
            # extracting text from page
            print(pageObj.extract_text())
            # pdfReader = PdfReader(pdfFileObj)
        if text.upper() == "ARUNANCHAL PRADESH":
            pdfFileObj = open('C:\\Users\\asus\\Downloads\\ARUNANCHAL PRADESH.pdf', 'rb')
            pdfReader = PdfReader(pdfFileObj)
            # printing number of pages in pdf file
            print(len(pdfReader.pages))
            # creating a page object
            pageObj = pdfReader.pages[0]
            # extracting text from page
            print(pageObj.extract_text())
            # closing the pdf file object
            pdfFileObj.close()
            # pdfReader = PdfReader(pdfFileObj)
    elif t.lower()=="c":
        import cv2
        y="C:/Users/asus/Pictures/INPUT IMG/" + text.capitalize()+".jpg"
        image = cv2.imread(y)
        grey_filter = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(grey_filter)
        blur = cv2.GaussianBlur(invert,(21,21),0)
        invertedblur = cv2.bitwise_not(blur)

        sketch_filter = cv2.divide(grey_filter,invertedblur,scale = 256.0)
        cv2.imwrite("C:/Users/asus/Pictures/OUTPUT IMG/output.png",sketch_filter)
        print("succesful")
    elif t.lower()=="d":
        import os
        d = "C:\\Users\\asus\\" + text.capitalize()
        os.startfile(d)
    else:
        print("please enter your choice correctly")



