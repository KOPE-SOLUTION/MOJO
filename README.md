# Mojo ทีละขั้นสำหรับผู้มีพื้นฐาน Python

หลักสูตรภาษาไทย ตั้งแต่พื้นฐานจนถึงหัวข้อขั้นสูง

เหมาะสำหรับผู้ที่เขียน Python ได้ และคุ้นเคยกับ NumPy, pandas และ Matplotlib

เริ่มจากโปรแกรมขนาดเล็ก แล้วต่อยอดสู่ชนิดข้อมูล การจัดการข้อมูล และการประมวลผลบน CPU/GPU

**เวอร์ชันที่ใช้:** Mojo 1.2.0

## เริ่มต้นสำหรับผู้เรียนใหม่

ทำตามลำดับนี้เพียงครั้งแรก:

1. ดาวน์โหลดและแตกไฟล์โค้ด
2. เตรียม Ubuntu บน Windows ด้วย WSL2
3. สร้าง environment และติดตั้ง Mojo 1.2.0
4. รันตัวอย่าง EP.1
5. สร้างไฟล์ฝึกและเริ่มเรียนทีละขั้น

ขั้นตอนด้านล่างใช้ **Windows และ Ubuntu 24.04 ผ่าน WSL2**

Mojo ไม่รันบน Windows โดยตรง ส่วนบทเรียน EP.1–4 ใช้ CPU ได้ ไม่จำเป็นต้องมี GPU
ดู [ข้อกำหนดระบบของ Mojo](https://mojolang.org/docs/requirements/)

หากใช้ Ubuntu อยู่แล้ว ให้ข้ามขั้นติดตั้ง WSL และใช้โฟลเดอร์ที่ดาวน์โหลดไว้ใน Linux

ผู้ใช้ macOS ดู [วิธีติดตั้งทางการ](https://mojolang.org/install/)
ชุดคำสั่งด้านล่างตรวจบน Ubuntu WSL2

## 1. ดาวน์โหลดโค้ด

เลือกเพียงวิธีเดียว

### วิธี A: ดาวน์โหลด ZIP

วิธีนี้ไม่ต้องติดตั้ง Git และไม่ต้องมีบัญชี GitHub

1. กด [ดาวน์โหลดโค้ดทั้งหมดเป็น ZIP](https://github.com/KOPE-SOLUTION/MOJO/archive/refs/heads/main.zip)
2. คลิกขวาไฟล์ ZIP ใน Windows แล้วเลือก **Extract All** เพื่อแตกไฟล์
3. เปิดโฟลเดอร์ที่แตกแล้ว หาชั้นที่มีไฟล์ README และโฟลเดอร์บทเรียน
4. เปลี่ยนชื่อโฟลเดอร์ชั้นนั้นจาก **MOJO-main** เป็น **MOJO**
5. สร้างโฟลเดอร์สำหรับเก็บหลักสูตร แล้ววางโฟลเดอร์ MOJO ไว้ตามตัวอย่างนี้

ตำแหน่งตัวอย่างบน Windows:

~~~text
C:\mojo-course\MOJO
~~~

เมื่อเปิดโฟลเดอร์นั้น ควรเห็นอย่างน้อย:

~~~text
README.md
requirements-mojo-lock.txt
lessons/
~~~

ต้องแตกไฟล์ก่อนใช้งาน ไม่เปิดรันจากข้างใน ZIP

หากเลือกเก็บที่อื่น ให้ใช้ตำแหน่งของตนเองในขั้นเข้าโฟลเดอร์ด้านล่าง

### วิธี B: ใช้ Git ที่ติดตั้งไว้แล้ว

หากเลือกดาวน์โหลด ZIP แล้ว ให้ข้ามวิธีนี้

เปิด **PowerShell บน Windows** แล้วรัน:

~~~powershell
git clone https://github.com/KOPE-SOLUTION/MOJO.git C:\mojo-course\MOJO
~~~

คำสั่งนี้ดาวน์โหลดโค้ดลงโฟลเดอร์เดียวกับวิธี A

โฟลเดอร์ปลายทางต้องยังไม่มีโค้ดที่ดาวน์โหลดไว้อยู่ก่อน
หากมีแล้ว ให้ใช้โฟลเดอร์เดิมต่อได้

## 2. เตรียม Ubuntu บน Windows

WSL ช่วยให้ใช้ Linux ภายใน Windows ได้

ขั้นนี้อิง [คู่มือติดตั้ง WSL ของ Microsoft](https://learn.microsoft.com/windows/wsl/install)
ใช้ Windows 11 หรือ Windows 10 ที่รองรับคำสั่งติดตั้ง WSL

### 2.1 ตรวจว่ามี Ubuntu แล้วหรือยัง

เปิด **PowerShell บน Windows** แล้วรัน:

~~~powershell
wsl --list --verbose
~~~

ถ้ามีชื่อ Ubuntu-24.04 และคอลัมน์ VERSION เป็น 2 แล้ว ให้ข้ามไปข้อ 2.3

### 2.2 ติดตั้งเมื่อยังไม่มี

เปิด PowerShell โดยเลือก **Run as administrator** แล้วรัน:

~~~powershell
wsl --install -d Ubuntu-24.04
~~~

รอให้ติดตั้งเสร็จ และรีสตาร์ต Windows หากระบบร้องขอ

เมื่อเปิด Ubuntu ครั้งแรก ให้สร้างชื่อผู้ใช้และรหัสผ่านของ Linux

ขณะพิมพ์รหัสผ่านจะไม่มีตัวอักษรปรากฏ เป็นพฤติกรรมปกติ
ดู [การตั้งค่าบัญชี Ubuntu](https://learn.microsoft.com/windows/wsl/setup/environment#set-up-your-linux-username-and-password)

ถ้ามี Ubuntu-24.04 อยู่แล้ว แต่ VERSION เป็น 1 ให้เปลี่ยนเป็น WSL2:

~~~powershell
wsl --set-version Ubuntu-24.04 2
~~~

### 2.3 เข้า Ubuntu

เปิด PowerShell แล้วรัน:

~~~powershell
wsl -d Ubuntu-24.04
~~~

**จากจุดนี้ คำสั่งในบล็อก bash ให้พิมพ์ใน Ubuntu**

ชื่อหน้าต่างอาจยังเป็น Windows Terminal แต่เชลล์ที่ใช้อยู่ต้องเป็น Ubuntu
อย่าพิมพ์คำสั่งติดตั้ง Linux ใน PowerShell

## 3. ติดตั้ง Mojo 1.2.0

### 3.1 เตรียม Python และเครื่องมือที่จำเป็น

รันใน **Ubuntu** ทีละคำสั่ง:

~~~bash
sudo apt update
~~~

~~~bash
sudo apt install python3 python3-venv build-essential
~~~

ถ้ามีคำถามให้ยืนยันการติดตั้ง ให้พิมพ์ Y แล้วกด Enter

หากขอรหัสผ่าน ให้ใช้รหัสผ่าน Ubuntu ที่ตั้งไว้

Python ใช้สร้าง environment สำหรับติดตั้งแพ็กเกจ
ส่วนเครื่องมือ C compiler ใช้ในกระบวนการสร้างโปรแกรม Mojo

### 3.2 เข้าโฟลเดอร์โค้ด

ตำแหน่งบน Windows ในตัวอย่างคือ:

~~~text
C:\mojo-course\MOJO
~~~

ตำแหน่งเดียวกันเมื่อเข้าจาก Ubuntu WSL คือ:

~~~text
/mnt/c/mojo-course/MOJO
~~~

เข้าโฟลเดอร์ แล้วตรวจตำแหน่งและไฟล์:

~~~bash
cd /mnt/c/mojo-course/MOJO
pwd
ls
~~~

ต้องเห็นไฟล์สำหรับติดตั้ง:

~~~text
requirements-mojo-lock.txt
~~~

ถ้าเก็บโค้ดที่อื่น ให้เปลี่ยนเฉพาะเส้นทางหลังคำสั่ง cd
หากเส้นทางมีช่องว่าง ให้ครอบด้วยเครื่องหมายคำพูด

ผู้ใช้ Ubuntu ที่ไม่ได้ผ่าน WSL ให้เข้าโฟลเดอร์โค้ดของตนเอง ไม่ใช้เส้นทางไดรฟ์ Windows

### 3.3 สร้าง environment ของหลักสูตร

โฟลเดอร์ environment ไม่ได้ติดมากับโค้ดที่ดาวน์โหลด ต้องสร้างในเครื่องของผู้เรียน

รันจากโฟลเดอร์หลักสูตร:

~~~bash
python3 -m venv .venv
~~~

เปิดใช้งาน environment:

~~~bash
source .venv/bin/activate
~~~

ให้ใช้ environment นี้เมื่อติดตั้งหรือรัน Mojo ของหลักสูตร

### 3.4 ติดตั้งแพ็กเกจตามเวอร์ชันที่กำหนด

~~~bash
python -m pip install -r requirements-mojo-lock.txt
~~~

[ไฟล์นี้](requirements-mojo-lock.txt) กำหนด Mojo 1.2.0 พร้อมเวอร์ชัน dependency ที่ใช้ตรวจตัวอย่างบน Linux x86_64

การติดตั้งใช้ Python environment แยกสำหรับหลักสูตร
แนวทางติดตั้งเป็นแพ็กเกจอ้างอิงจาก [Install Mojo](https://mojolang.org/install/)

### 3.5 ตรวจว่าติดตั้งสำเร็จ

ตรวจ dependency:

~~~bash
python -m pip check
~~~

ผลที่ควรเห็น:

~~~text
No broken requirements found.
~~~

ตรวจเวอร์ชัน Mojo:

~~~bash
mojo --version
~~~

ผลจากรุ่นที่ใช้ตรวจในหลักสูตร:

~~~text
Mojo 1.2.0 (2016d0cd)
~~~

เลขเวอร์ชันต้องเป็น **1.2.0**

## 4. รัน EP.1

ยังคงอยู่ใน **Ubuntu** ที่โฟลเดอร์หลักสูตร และเปิดใช้งาน environment แล้ว

รันตัวอย่างฉบับจบบท:

~~~bash
mojo lessons/phase-01/ep01-hello-mojo/main.mojo
~~~

ควรเห็นข้อความ 3 บรรทัด:

~~~text
Hello, Mojo!
Dataset: demo-01
Status: ready
~~~

เมื่อผลตรงกัน แสดงว่าติดตั้งและรันตัวอย่างแรกได้แล้ว

จากนั้นเปิด [EP.1 เขียน รัน และแก้โปรแกรมแรก](lessons/phase-01/ep01-hello-mojo/README.md)
เพื่อพิมพ์โค้ดเองทีละขั้น

## 5. เตรียมไฟล์สำหรับฝึกเอง

สร้างโฟลเดอร์ฝึกจากโฟลเดอร์หลักสูตร:

~~~bash
mkdir -p practice
~~~

ใช้ editor ที่ถนัดสร้างไฟล์:

~~~text
practice/main.mojo
~~~

เปิด [บทเรียน EP.1](lessons/phase-01/ep01-hello-mojo/README.md) แล้วพิมพ์โค้ดขั้นที่ 1 ลงไฟล์นี้

บันทึกไฟล์ แล้วรัน:

~~~bash
mojo practice/main.mojo
~~~

แต่ละบทจะให้คาดเดาผลก่อนรัน ทดลองเปลี่ยนค่า และทำแบบฝึกหัดก่อนเปิดเฉลย

ดูรายละเอียดการเก็บคำตอบใน [คู่มือพื้นที่ฝึก](docs/PRACTICE.md)

## เมื่อกลับมาเรียนครั้งถัดไป

ไม่ต้องดาวน์โหลดโค้ดหรือสร้าง environment ใหม่ทุกครั้ง

เปิด PowerShell แล้วเข้า Ubuntu:

~~~powershell
wsl -d Ubuntu-24.04
~~~

จากนั้นรันใน Ubuntu:

~~~bash
cd /mnt/c/mojo-course/MOJO
source .venv/bin/activate
mojo lessons/phase-01/ep01-hello-mojo/main.mojo
~~~

หากเก็บโค้ดไว้ตำแหน่งอื่น ให้ใช้เส้นทางเดิมของตนเอง

## ถ้ารันไม่สำเร็จ

| อาการ | ตรวจและแก้ |
|---|---|
| PowerShell ไม่รู้จักคำสั่งของ Linux | เข้า Ubuntu ก่อน ตามข้อ 2.3 |
| ไม่พบไฟล์สำหรับติดตั้ง | ตรวจว่าแตก ZIP แล้ว และเข้าโฟลเดอร์ชั้นที่มีไฟล์ README |
| ไม่พบไฟล์เปิดใช้งาน environment | สร้าง environment ตามข้อ 3.3 ก่อน |
| Ubuntu ไม่พบคำสั่ง Mojo | เปิดใช้งาน environment แล้วตรวจเวอร์ชันอีกครั้ง |
| ไม่พบไฟล์ตัวอย่าง EP.1 | ตรวจว่าตำแหน่งปัจจุบันเป็นโฟลเดอร์หลักสูตร ไม่ใช่โฟลเดอร์ย่อย |
| สร้าง environment ไม่ได้เพราะขาด venv | ติดตั้งเครื่องมือในข้อ 3.1 แล้วทำข้อ 3.3 ใหม่ |

ดูเพิ่มเติมใน [วิธีตรวจปัญหา](notes/troubleshooting.md)
และ [รายละเอียดการใช้ Windows กับ WSL](notes/setup-windows-wsl.md)

## บทเรียน

| ตอน | บทเรียน |
|---|---|
| EP.1 | [เขียน รัน และแก้โปรแกรมแรก](lessons/phase-01/ep01-hello-mojo/README.md) |
| EP.2 | [ตัวแปรและชนิดข้อมูล](lessons/phase-01/ep02-variables-types/README.md) |
| EP.3 | [คำนวณและตรวจเงื่อนไข](lessons/phase-01/ep03-calculations-conditions/README.md) |
| EP.4 | [ทำซ้ำด้วย for และ while](lessons/phase-01/ep04-loops/README.md) |

EP.1–4 มีเนื้อหา ตัวอย่าง แบบฝึกหัด และเฉลยพร้อมเรียน

EP.5–48 ยังเป็นแผนเนื้อหา ดูรายละเอียดใน [แผนหลักสูตร](ROADMAP.md)

## เส้นทางการเรียน

| ช่วง | EP | เนื้อหา | ผลงานปลายช่วง |
|---|---|---|---|
| 1 พื้นฐาน Mojo | 1–8 | ตัวแปร ชนิดข้อมูล เงื่อนไข ลูป ฟังก์ชัน และรายการ | รายงานข้อมูลใน terminal |
| 2 โปรแกรมที่ดูแลต่อได้ | 9–16 | การทดสอบ โมดูล struct และ ownership | ตัวประมวลผลพร้อมชุดทดสอบ |
| 3 ใช้ร่วมกับ Python | 17–24 | pandas, NumPy, Matplotlib และการส่งข้อมูล | วิเคราะห์ CSV และวาดกราฟ |
| 4 ประสิทธิภาพบน CPU | 25–32 | การวัดความเร็ว SIMD และงานขนาน | รายงานเปรียบเทียบที่ทำซ้ำได้ |
| 5 GPU | 33–40 | kernel, thread, memory และ reduction | ตัวประมวลผลที่เทียบผลกับ CPU |
| 6 ขั้นสูงและ Capstone | 41–48 | ออกแบบ API, profiling, packaging และโครงการ | ผลงานพร้อมวิธีรันและผลทดสอบ |

ช่วงที่ 1–4 เรียนด้วย CPU ได้

ช่วง GPU ต้องตรวจฮาร์ดแวร์และเวอร์ชัน MAX เพิ่มเติม
หากไม่มี GPU สามารถเลือก [โครงการสาย CPU](projects/README.md) ได้

## เอกสารประกอบ

- [แหล่งอ้างอิงทางการ](docs/REFERENCES.md)
- [ผลตรวจโค้ด EP.1–4 บน Mojo 1.2.0](notes/validation.md)
- [วิธีตรวจปัญหาระหว่างเรียน](notes/troubleshooting.md)
- [เกณฑ์ตรวจความเข้าใจ](docs/ASSESSMENT.md)
