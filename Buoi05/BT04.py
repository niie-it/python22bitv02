'''GPA1
Nhập điểm: assignment, mid_term, final_exam
'''

def nhap_diem():
    '''Hàm nhập điểm thành phần, trả về dict'''
    assignment, mid_term, final_exam = 0, 0, 0
    assignment = float(input("Điểm bài tập (20%):"))
    mid_term = float(input("Điểm giữa kỳ (20%):"))
    final_exam = float(input("Điểm cuối kỳ (60%):"))
    
    diem_trung_binh = round(assignment * 0.2 + mid_term * 0.2 + final_exam * 0.6)
    grade = "F"
    if diem_trung_binh >= 8.5:
        grade = "A"
    elif diem_trung_binh >= 7.0:
        grade = "B"
    elif diem_trung_binh >= 5.5:
        grade = "C"
    elif diem_trung_binh >= 4:
        grade = "D"
    
    return {
        "assignment": assignment,
        "mid_term": mid_term,
        "final_exam": final_exam,
        "score": diem_trung_binh,
        "grade": grade
    }

    
#Demo gọi hàm
diem_ap = nhap_diem()
#Lưu xuống file JSON (có cấu trúc - y chang dict)
import json
with open("student_ap.json", "w", encoding="utf8") as my_file:
    json.dump(diem_ap, my_file) # Lưu dict xuống file json