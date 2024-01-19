#__import__("os").system("pip --quiet install word2number -q")
def split_sentences(text):
    #chia văn bản thành các câu sử dụng dấu chấm, dấu chấm hỏi hoặc dấu chấm than làm dấu phân cách
    sentences = []
    sentence = ""
    for char in text:
        if char in [".", "?", "!"]:
            sentences.append(sentence.strip())
            sentence = ""
        else:
            sentence += char
    if sentence:
        sentences.append(sentence.strip())
    return sentences

def split_words(sentence):
    # chia câu thành các từ sử dụng dấu cách làm dấu phân cách
    return sentence.split()

# đọc file text
#f= open("vanban.txt", "r", encoding="utf-8")
#t=f.read()
t=input("nhập văn bản: ")
# chia văn bản thành các câu
sentences = split_sentences(t)

# chia các câu thành các từ

words = split_words(t)

# yêu cầu người dùng nhập vào từ khóa
dulieu=input("bạn muốn tách từ hay câu?t/c: ")
if dulieu== "t" : 
    print("Từ đã được tách: ",words)

if dulieu== "c": 
    print("Câu đã được tách: ",sentences)

input("Ấn Enter để thoát: ")


    