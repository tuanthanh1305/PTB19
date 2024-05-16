print("Bổ túc kiến thức toán")
print("---------------------")
# định nghĩa câu hỏi và câu trả lời bằng biến
question1 = "Câu 1. 2 luỹ thừa 2 là mấy"
answer1 = 4

question2 = "Câu 2. Căn bậc 3 của 8 là?"
answer2 = 2

question3 = "Câu 3. 16 có chia hết cho 2 không? Bấm Y nếu là Có hoặc N nếu là Không:"
answer3 = "Y"
# Định nghĩa biến điểm
score = 0

# Lập trình chức năng câu hỏi
# câu hỏi 1
print(question1)
user_answer = int(input("Đáp án: "))
if user_answer == answer1:
    print("Chính xác!")
    score += 1
else:
    print("Chưa chính xác!")
# câu hỏi 2
# câu hỏi 3

# in điểm ra màn hình
print("Điểm bổ túc kiến thức toán của Ngọc Hà là:", score, "/3")

    
