# พื้นที่ฝึกเขียนโค้ด

เปิด Ubuntu WSL และเข้าโฟลเดอร์หลักสูตร:

~~~bash
cd /mnt/c/Users/kopes/Documents/L/MOJO
source .venv/bin/activate
mkdir -p practice
~~~

สร้าง practice/main.mojo ใน editor แล้วทำตามแต่ละบท รันจากโฟลเดอร์ MOJO เสมอ:

~~~bash
mojo practice/main.mojo
~~~

ก่อนขึ้นบทใหม่ เก็บไฟล์คำตอบเดิมด้วยชื่ออื่นถ้าต้องการ เช่น ep01-my-answer.txt แล้วค่อยใช้ main.mojo สำหรับบทใหม่ โฟลเดอร์ practice ถูกยกเว้นใน .gitignore เพื่อให้โค้ดฝึกกับต้นฉบับแยกกัน

โค้ดอ้างอิงอยู่ใน lessons/phase-01 ไม่ต้องแก้ต้นฉบับเพื่อทำโจทย์ หากต้องการเทียบให้เปิดคู่กัน

เมื่อเปิด terminal ใหม่ ต้อง activate environment อีกครั้ง หรือเรียก .venv/bin/mojo โดยตรงจากโฟลเดอร์ MOJO
