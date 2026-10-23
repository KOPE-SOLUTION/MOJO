# สภาพแวดล้อมที่ตรวจสำหรับหลักสูตร

อัปเดตและรันตรวจ Mojo วันที่ **23 ตุลาคม 2026** ตามเวลา Asia/Bangkok

## สภาพแวดล้อมที่ใช้ทดสอบ EP.1–4

| รายการ | ผลที่ตรวจเมื่อ 23 ตุลาคม 2026 |
|---|---|
| โฟลเดอร์ | C:/Users/kopes/Documents/L/MOJO |
| Ubuntu ผ่าน WSL2 | Ubuntu-24.04, 24.04.4 LTS, x86_64 |
| glibc | 2.39 |
| Python ที่ใช้รันตัวตรวจ | 3.12.3 |
| C compiler | พบ /usr/bin/cc |
| Mojo ของหลักสูตร | **1.2.0 (2016d0cd)** ใน .venv ภายใต้ MOJO |
| pip check | No broken requirements found. |
| dependency ที่ติดตั้งจริง | [requirements-mojo-lock.txt](../requirements-mojo-lock.txt) |

ทดลองติดตั้ง 1.2.0 ใน environment แยกและรัน EP.1 ก่อนอัปเดต .venv หลัก จากนั้นติดตั้งชุด dependency เดียวกันใน .venv แล้วตรวจตัวอย่าง EP.1–4 ด้วย environment หลัก ดู [ผลตรวจและข้อจำกัด](validation.md)

ใช้แพ็กเกจ mojo==1.2.0 จาก PyPI ภายใน Python venv ของ Ubuntu WSL ไฟล์ requirements-mojo.txt ระบุ dependency หลัก ส่วน requirements-mojo-lock.txt มาจาก pip freeze ของ .venv ที่ใช้ทดสอบจริง

## ข้อมูลเครื่องจากการเตรียมหลักสูตรครั้งแรก

ข้อมูลด้านล่างตรวจเมื่อ **5 ตุลาคม 2026** เก็บเป็นข้อมูลประกอบ ไม่ได้ตรวจรายการเหล่านี้ซ้ำในการอัปเดตวันที่ 23 ตุลาคม

| รายการ | ผลที่พบครั้งแรก |
|---|---|
| Windows | OSDescription รายงาน Microsoft Windows 10.0.26200, X64 |
| WSL | Version 2; มี Ubuntu-24.04 อยู่แล้ว |
| CPU ที่ WSL รายงาน | AMD Ryzen 7 5700X3D; มี avx2, fma, bmi1, bmi2 |
| RAM ที่ WSL เห็น | ประมาณ 15 GiB |
| Python ฝั่ง Windows | 3.13.7 |
| Git ฝั่ง Windows | 2.50.0.windows.1 |
| uv ฝั่ง Windows | 0.8.18 |
| Mojo ก่อนเตรียมหลักสูตร | ไม่พบใน Windows PATH และไม่พบใน Ubuntu PATH |
| Mojo ที่ติดตั้งครั้งแรก | 1.1.0 (8189361e) |
| GPU/MAX | ยังไม่ได้ตรวจหรือติดตั้งสำหรับหลักสูตรนี้ |

เก็บ [dependency รุ่นเดิม](history/mojo-1.1.0/requirements-mojo-lock.txt) และ [ผลรัน 1.1.0 เดิม](history/mojo-1.1.0/validation-results.json) ไว้เป็นประวัติ หลักสูตรปัจจุบันให้ใช้ 1.2.0 ตามคู่มือติดตั้ง

การอัปเดตนี้เปลี่ยนแพ็กเกจใน environment ของหลักสูตร ไม่ได้เปลี่ยน default WSL distribution, Windows Python, package ระบบ หรือ driver สำหรับ GPU

ดู [การเริ่มใช้](setup-windows-wsl.md) และ [ผลตรวจตัวอย่าง](validation.md)
