# เตรียม Mojo บน Windows ด้วย Ubuntu WSL

คู่มือนี้ใช้โฟลเดอร์ C:/Users/kopes/Documents/L/MOJO ที่คุณเตรียมไว้ และ Ubuntu-24.04 ที่พบในเครื่องแล้ว การตรวจครั้งนี้ติดตั้ง Mojo 1.2.0 ใน .venv ของหลักสูตรเรียบร้อย ดู [สถานะเครื่อง](environment.md)

Mojo รุ่นที่ใช้ไม่รันบน Windows โดยตรง ให้ใช้ Ubuntu WSL สำหรับคำสั่ง Mojo ส่วน editor จะเปิดจาก Windows ผ่าน WSL ได้ ตาม [ข้อกำหนดระบบทางการ](https://mojolang.org/docs/requirements/)

## 1 เข้า Ubuntu ให้ถูกตัว

เปิด PowerShell และรัน:

~~~powershell
wsl -d Ubuntu-24.04
~~~

เครื่องนี้มี WSL หลาย distribution และค่าเริ่มต้นเป็น kali-linux จึงระบุ Ubuntu-24.04 ในคำสั่ง เพื่อให้ตัวอย่างและ environment ตรงกัน

จากนี้คำสั่ง bash ทั้งหมดให้พิมพ์ใน terminal Ubuntu

## 2 เข้าโฟลเดอร์หลักสูตร

~~~bash
cd /mnt/c/Users/kopes/Documents/L/MOJO
pwd
~~~

ผลของ pwd ควรเป็นเส้นทางดังกล่าว /mnt/c คือไดรฟ์ C ของ Windows ที่เข้าถึงจาก WSL ไฟล์ต้นฉบับจึงยังอยู่ในโฟลเดอร์ที่คุณเตรียมไว้

## 3 ใช้ environment ที่จัดไว้

~~~bash
source .venv/bin/activate
mojo --version
~~~

เวอร์ชันที่ตรวจได้ในการจัดทำชุดนี้:

~~~text
Mojo 1.2.0 (2016d0cd)
~~~

ถ้าเพิ่งดาวน์โหลดหลักสูตรในเครื่องอื่น .venv จะไม่ได้ติดมาด้วย ให้ทำขั้นสร้างด้านล่างก่อน

<details>
<summary>สร้าง environment ใหม่เมื่อยังไม่มี .venv</summary>

ตรวจ Python และ C compiler:

~~~bash
python3 --version
cc --version
~~~

สร้าง environment ในโฟลเดอร์ MOJO แล้วติดตั้งชุดที่ล็อกเวอร์ชัน:

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-mojo-lock.txt
mojo --version
~~~

requirements-mojo.txt ระบุ dependency หลัก ส่วน requirements-mojo-lock.txt บันทึกชุดเวอร์ชันที่ติดตั้งจริงบน Linux x86_64 ไม่ใช่ lock แบบรวมทุกแพลตฟอร์ม

หาก Ubuntu แจ้งไม่มี venv หรือ C compiler จึงค่อยติดตั้ง package ระบบที่ขาดด้วยคำสั่งต่อไปนี้ คำสั่งนี้เปลี่ยน package ระบบและอาจขอรหัสผ่าน:

~~~bash
sudo apt update
sudo apt install python3-venv build-essential
~~~

จากนั้นกลับมาสร้าง environment ไม่จำเป็นต้องทำขั้น apt หากเครื่องมือมีแล้ว เครื่องที่ตรวจครั้งนี้มีเครื่องมือเหล่านี้อยู่ก่อน

การติดตั้ง Mojo เป็น Python package อิง [Install Mojo](https://mojolang.org/install/) เลือก environment แยกสำหรับหลักสูตรเพื่อเก็บเวอร์ชันที่ใช้สอนได้

</details>

## ถ้ามี environment รุ่น 1.1.0 อยู่แล้ว

ในโฟลเดอร์เครื่องนี้ .venv อัปเดตเป็น 1.2.0 ให้แล้ว ใช้ขั้นที่ 3 แล้วเรียนต่อได้ ส่วนผู้ที่มีสำเนาหลักสูตรเดิม ให้เปิด Ubuntu terminal เข้าโฟลเดอร์ MOJO แล้วทำทีละคำสั่ง:

~~~bash
source .venv/bin/activate
python -m pip install --upgrade -r requirements-mojo-lock.txt
python -m pip check
mojo --version
python scripts/check_examples.py
~~~

คำสั่ง install ใช้ชุดเวอร์ชันที่บันทึกไว้สำหรับหลักสูตร; pip check ตรวจ dependency; mojo --version ต้องขึ้น 1.2.0; สคริปต์สุดท้ายรันตัวอย่างและกรณีจงใจผิด โดยควรจบด้วย 34/34 expected behaviors confirmed

ถ้าสคริปต์แจ้ง FAIL ให้เปิด [วิธีตรวจปัญหา](troubleshooting.md) และรายงาน notes/validation-results.json ก่อนเริ่มอัดคลิป รายงานล่าสุดจะถูกเขียนทับทุกครั้งที่รัน สคริปต์นี้เป็นเครื่องมือของผู้สอน ยังไม่ต้องเรียนโค้ด Python ข้างในเพื่อเรียน EP.1

## 4 รันบทแรก

~~~bash
mojo lessons/phase-01/ep01-hello-mojo/main.mojo
~~~

ควรเห็น:

~~~text
Hello, Mojo!
Dataset: demo-01
Status: ready
~~~

เปิด [EP.1](../lessons/phase-01/ep01-hello-mojo/README.md) แล้วพิมพ์เองทีละขั้น ก่อนอ่านเฉลย

## 5 เปิด editor

ใช้ editor ที่ถนัด หากใช้ VS Code ให้เปิดโฟลเดอร์ผ่าน WSL และติดตั้ง extension Mojo ของ Modular ในฝั่ง WSL ตาม [คู่มือทางการ](https://mojolang.org/install/) ไม่จำเป็นต้องเพิ่ม Jupyter ในบทเริ่มต้น

## เมื่อต้องเปิดใหม่

เข้า Ubuntu → cd โฟลเดอร์ → source .venv/bin/activate → รันไฟล์ ส่วน Python บน Windows มี environment แยกจาก Python ภายใน WSL การติดตั้ง library ฝั่งหนึ่งไม่ได้ทำให้ใช้อีกฝั่งได้อัตโนมัติ

ขั้น CPU ใช้ .venv ชุดนี้ ส่วน GPU/MAX จะจัด environment ที่ตรงรุ่นเมื่อถึง Phase 5 ยังไม่ต้องเปลี่ยน driver เพื่อเรียน EP.1–4
