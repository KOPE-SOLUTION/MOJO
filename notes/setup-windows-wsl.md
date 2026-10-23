# ใช้ Mojo บน Windows ด้วย Ubuntu WSL

หากเพิ่งเริ่ม ให้ทำตาม [README สำหรับผู้เรียนใหม่](../README.md)

README มีขั้นตอนดาวน์โหลดโค้ด ติดตั้ง WSL สร้าง environment และรัน EP.1 ครบตามลำดับ

หน้านี้อธิบายการเข้า Ubuntu การเลือกตำแหน่งโฟลเดอร์ และการอัปเดต environment ที่มีอยู่แล้ว

## เข้า Ubuntu ให้ถูกตัว

เปิด **PowerShell บน Windows** แล้วรัน:

~~~powershell
wsl --list --verbose
~~~

ดูชื่อ Ubuntu ที่ติดตั้งอยู่ และตรวจว่าใช้ WSL2

ตัวอย่างหลักสูตรเลือก Ubuntu-24.04 จึงเข้าใช้งานด้วย:

~~~powershell
wsl -d Ubuntu-24.04
~~~

หากติดตั้ง Ubuntu ด้วยชื่ออื่นที่รองรับ Mojo ให้ใช้ชื่อตามรายการในเครื่อง

ดู [ข้อกำหนดระบบ Mojo](https://mojolang.org/docs/requirements/)
และ [คู่มือ WSL ของ Microsoft](https://learn.microsoft.com/windows/wsl/install)

## เข้าโฟลเดอร์ที่ดาวน์โหลดไว้

ตัวอย่างตำแหน่งบน Windows:

~~~text
C:\mojo-course\MOJO
~~~

ตำแหน่งเดียวกันภายใน Ubuntu WSL:

~~~text
/mnt/c/mojo-course/MOJO
~~~

รันใน **Ubuntu**:

~~~bash
cd /mnt/c/mojo-course/MOJO
pwd
ls
~~~

หากเลือกโฟลเดอร์อื่น ให้เปลี่ยนเส้นทางให้ตรงกับที่เก็บไฟล์จริง

เมื่อเส้นทางมีช่องว่าง ให้ครอบด้วยเครื่องหมายคำพูด เช่น:

~~~bash
cd "/mnt/c/My Courses/MOJO"
~~~

เลือกใช้เพียงเส้นทางเดียวที่ตรงกับเครื่องของตนเอง

## เปิดใช้งาน environment

ต้องสร้างและติดตั้งแพ็กเกจตาม README ก่อน

environment ของแต่ละเครื่องไม่ได้รวมอยู่ใน ZIP หรือ Git repository

~~~bash
source .venv/bin/activate
mojo --version
~~~

ผลจากเวอร์ชันที่ใช้ในหลักสูตร:

~~~text
Mojo 1.2.0 (2016d0cd)
~~~

Python บน Windows กับ Python ใน Ubuntu ใช้ environment คนละชุดกัน

ให้ติดตั้งและเรียก Mojo ใน Ubuntu ที่เปิดใช้งาน environment ของหลักสูตรแล้ว

## อัปเดต environment เดิมเป็น Mojo 1.2.0

ใช้หัวข้อนี้เมื่อมี environment อยู่แล้ว และได้ไฟล์หลักสูตรรุ่นปัจจุบันมาเรียบร้อย

รันใน Ubuntu จากโฟลเดอร์หลักสูตร:

~~~bash
source .venv/bin/activate
python -m pip install --upgrade -r requirements-mojo-lock.txt
python -m pip check
mojo --version
~~~

เลขเวอร์ชันต้องเป็น **1.2.0**

ไฟล์ล็อกบันทึกเวอร์ชันแพ็กเกจที่ตรวจบน Linux x86_64
ดู [สถานะเครื่องที่ใช้ทดสอบ](environment.md)

## รันตัวอย่างแรก

~~~bash
mojo lessons/phase-01/ep01-hello-mojo/main.mojo
~~~

ผลที่คาดหวัง:

~~~text
Hello, Mojo!
Dataset: demo-01
Status: ready
~~~

เริ่มพิมพ์เองตาม [บทเรียน EP.1](../lessons/phase-01/ep01-hello-mojo/README.md)

## ตรวจตัวอย่างทั้งหมดเมื่อจำเป็น

รันจากโฟลเดอร์หลักสูตร หลังเปิดใช้งาน environment:

~~~bash
python scripts/check_examples.py
~~~

เมื่อพฤติกรรมตรงตามคาดครบ จะจบด้วย:

~~~text
34/34 expected behaviors confirmed
~~~

สคริปต์ครอบคลุมตัวอย่าง เฉลย และกรณีจงใจผิดของ EP.1–4

ทุกครั้งที่รันจะเขียนรายงานล่าสุดทับไฟล์:

~~~text
notes/validation-results.json
~~~

หากมีกรณีไม่ผ่าน ให้ดู [วิธีตรวจปัญหา](troubleshooting.md)

## เปิด editor

ใช้ editor ที่ถนัด

หากใช้ VS Code ให้เปิดโฟลเดอร์ผ่าน WSL และติดตั้ง extension Mojo ในฝั่ง WSL
ตาม [คู่มือติดตั้งทางการ](https://mojolang.org/install/)

[กลับ README](../README.md) · [พื้นที่ฝึก](../docs/PRACTICE.md)
