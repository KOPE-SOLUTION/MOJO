# แหล่งอ้างอิง Mojo

เอกสารประกอบสำหรับ Mojo 1.2.0 ตรวจเมื่อ 23 ตุลาคม 2026

## เอกสารทางการที่ใช้กับชุดเริ่มต้น

| แหล่ง | ใช้อ้างอิงอะไร |
|---|---|
| [Mojo releases](https://mojolang.org/releases/) | ตรวจเมื่อ 23 ตุลาคม 2026: รุ่น stable ที่ใช้ในหลักสูตรคือ 1.2.0 เผยแพร่ 22 ตุลาคม 2026 |
| [Release 1.2.0](https://mojolang.org/releases/v1.2.0/) | ตรวจการเปลี่ยนแปลงก่อนอัปเดตตัวอย่าง EP.1–4 |
| [Install Mojo](https://mojolang.org/install/) | การติดตั้งใน environment และ extension |
| [System requirements](https://mojolang.org/docs/requirements/) | Windows ผ่าน WSL, Ubuntu, CPU และ C compiler |
| [Language basics](https://mojolang.org/docs/manual/basics/) | main, def, print และโครงสร้างพื้นฐาน |
| [Variables](https://mojolang.org/docs/manual/variables/) | var และการกำหนด/อนุมานชนิด |
| [Operators](https://mojolang.org/docs/manual/operators/) | ลำดับคำนวณและการเปรียบเทียบ |
| [Control flow](https://mojolang.org/docs/manual/control-flow/) | if, elif, else, for, while, break และ continue |
| [Tips for Python devs](https://mojolang.org/docs/manual/python-to-mojo/) | ประเด็นที่ต้องเพิ่มจากความคุ้นเคย Python |

ระหว่างค้นพบว่าบางผลค้นหาและเส้นทางเอกสารเก่ายังแสดงตัวอย่างคนละรุ่น จึงเปิดหน้าปัจจุบันที่ redirect มายัง mojolang.org และตรวจเลขเวอร์ชันบนหน้า การเขียนโค้ดชุดนี้ใช้ def และ var ตาม baseline 1.2.0

## การอัปเดต EP.1–4 เป็น 1.2.0

รุ่นนี้เพิ่ม match/case และปรับ API บางส่วน เช่น StringSpan ตาม [release notes](https://mojolang.org/releases/v1.2.0/) หัวข้อเหล่านั้นยังไม่จำเป็นสำหรับสี่ตอนแรก จึงคงลำดับ print → ตัวแปรและชนิด → เงื่อนไข → ลูปไว้เหมือนเดิม

ตรวจโค้ดของหลักสูตรจริงด้วย compiler 1.2.0 แยกจากการอ่านเอกสาร ผลและขอบเขตอยู่ใน [บันทึกการทดสอบ](../notes/validation.md) แต่ละบทให้คาดเดาก่อนรัน ทดลองผิด แล้วแก้กลับทีละจุด

## แหล่งสำหรับพัฒนาช่วงถัดไป

| แหล่ง | ใช้กับช่วงใด |
|---|---|
| [Functions](https://mojolang.org/docs/manual/functions/) | ฟังก์ชันและการรับ/คืนค่า |
| [Get started tutorial](https://mojolang.org/docs/manual/get-started/) | ตัวอย่างลำดับการประกอบโปรแกรม |
| [Testing](https://mojolang.org/docs/tools/testing/) | assertion และ TestSuite |
| [Calling Python from Mojo](https://mojolang.org/docs/manual/python/python-from-mojo/) | Phase 3 ฝั่ง Mojo เรียก Python |
| [Calling Mojo from Python](https://mojolang.org/docs/manual/python/mojo-from-python/) | Phase 3 ฝั่ง Python เรียก Mojo |
| [GPU intro tutorial](https://max.modular.com/stable/gpu/intro-tutorial/) | Phase 5 การแบ่ง thread และย้ายข้อมูล |
| [MAX 26.5 release notes](https://max.modular.com/releases/v26.5/) | การย้าย API บางส่วนไป MAX accelerator library |
| [uv environment guide](https://docs.astral.sh/uv/pip/environments/) | ทางเลือกจัด environment หากย้ายไปใช้ uv ในอนาคต |

MAX 26.5 release notes ระบุการย้ายกลุ่ม GPU/algorithm/benchmark และ layout บางส่วนออกจาก Mojo standard library ไป MAX จึงต้องตรวจ package และคู่เวอร์ชันก่อนเขียนตัวอย่างขั้นสูง ไม่ใช้ชื่อ import จากบทความเก่าโดยไม่ตรวจ

## เวอร์ชันของตัวอย่าง

1. ตัวอย่าง EP.1–4 ใช้ Mojo 1.2.0
2. บันทึก mojo --version และ dependencies ที่รันจริงในเอกสารผลตรวจ
3. แยก environment ทดลองก่อนอัปเกรด แล้วทดสอบตัวอย่างและแบบฝึกหัดอีกครั้ง
4. เมื่อเริ่ม MAX/GPU ให้ตรวจความเข้ากันได้และกำหนดชุด dependency ของช่วงนั้น
5. ปรับผลคาดหวังเมื่อพฤติกรรมตั้งใจเปลี่ยน พร้อมบอกเหตุผล ไม่แก้ผลคาดหวังเพื่อกลบข้อผิดพลาด

ลิงก์เว็บอาจเปลี่ยนเนื้อหาในอนาคต จึงควรเทียบวันที่ตรวจ รุ่นที่ใช้ และผลรันใน repository ควบคู่กัน
