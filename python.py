import streamlit as st
import math

st.title("โปรแกรมคำนวณปริมาตรทรงเรขาคณิตด้วยภาษา Python")

# ตัวเลือกหน่วย
unit = st.selectbox("เลือกหน่วยความยาว", ["มิลลิเมตร", "เซนติเมตร", "เมตร", "กิโลเมตร"])

# ตัวเลือกรูปทรง
shape = st.radio("เลือกรูปทรง", ["ทรงลูกบาศก์", "ทรงสี่เหลี่ยมมุมฉาก", "ทรงกระบอก", "ทรงกลม", "ทรงกรวย", "พีระมิด"])

# ค่าที่ผู้ใช้กรอก
if shape == "ทรงลูกบาศก์":
    side = st.number_input("ความยาวด้าน", min_value=0.0, format="%.2f")
elif shape == "ทรงสี่เหลี่ยมมุมฉาก":
    width = st.number_input("ความกว้าง", min_value=0.0, format="%.2f")
    length = st.number_input("ความยาว", min_value=0.0, format="%.2f")
    height = st.number_input("ความสูง", min_value=0.0, format="%.2f")
elif shape == "ทรงกระบอก":
    radius = st.number_input("รัศมี", min_value=0.0, format="%.2f")
    height = st.number_input("ความสูง", min_value=0.0, format="%.2f")
elif shape == "ทรงกลม":
    radius = st.number_input("รัศมี", min_value=0.0, format="%.2f")
elif shape == "ทรงกรวย":
    radius = st.number_input("รัศมี", min_value=0.0, format="%.2f")
    height = st.number_input("ความสูง", min_value=0.0, format="%.2f")
elif shape == "พีระมิด":
    base_type = st.selectbox("เลือกชนิดฐาน", ["ฐานสามเหลี่ยม", "ฐานสี่เหลี่ยม", "ฐานหกเหลี่ยม"])
    if base_type == "ฐานสามเหลี่ยม":
        length = st.number_input("ความยาวฐาน", min_value=0.0, format="%.2f")
        base_height = st.number_input("ความสูงฐาน", min_value=0.0, format="%.2f")
        height = st.number_input("ความสูงพีระมิด", min_value=0.0, format="%.2f")
    elif base_type == "ฐานสี่เหลี่ยม":
        base_shape = st.radio("เลือกชนิดฐานสี่เหลี่ยม", ["จัตุรัส", "ผืนผ้า"])
        if base_shape == "จัตุรัส":
            side = st.number_input("ความยาวด้านฐาน", min_value=0.0, format="%.2f")
        else:
            length = st.number_input("ความยาวฐาน", min_value=0.0, format="%.2f")
            width = st.number_input("ความกว้างฐาน", min_value=0.0, format="%.2f")
        height = st.number_input("ความสูงพีระมิด", min_value=0.0, format="%.2f")
    elif base_type == "ฐานหกเหลี่ยม":
        side = st.number_input("ความยาวด้านฐาน", min_value=0.0, format="%.2f")
        height = st.number_input("ความสูงพีระมิด", min_value=0.0, format="%.2f")

# ปุ่มคำนวณ
if st.button("คำนวณ"):
    try:
        if shape == "ทรงลูกบาศก์":
            volume = side ** 3
        elif shape == "ทรงสี่เหลี่ยมมุมฉาก":
            volume = width * length * height
        elif shape == "ทรงกระบอก":
            volume = math.pi * radius ** 2 * height
        elif shape == "ทรงกลม":
            volume = (4/3) * math.pi * radius**3
        elif shape == "ทรงกรวย":
            volume = (1/3) * math.pi * radius ** 2 * height
        elif shape == "พีระมิด":
            if base_type == "ฐานสามเหลี่ยม":
                volume = (1/3) * (1/2) * length * base_height * height
            elif base_type == "ฐานสี่เหลี่ยม":
                if base_shape == "จัตุรัส":
                    base_area = side ** 2
                else:
                    base_area = length * width
                volume = (1/3) * base_area * height
            elif base_type == "ฐานหกเหลี่ยม":
                base_area = (3 * math.sqrt(3) / 2) * side ** 2
                volume = (1/3) * base_area * height

        st.success(f"ปริมาตร: {volume:.2f} ลูกบาศก์{unit}")
    except Exception as e:
        st.error("กรุณากรอกข้อมูลให้ครบและถูกต้อง")
