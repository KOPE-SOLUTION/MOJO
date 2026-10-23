# เฉลย EP.4

ลองทำโจทย์ใน [บทเรียน](../README.md) ก่อนเปิดหน้านี้

วิธีอื่นที่ได้ผลตรงตามโจทย์ถือว่าใช้ได้

## ข้อ 1

ใช้ `for` รวมจำนวนตั้งแต่ 1 ถึง 5

แสดงผลรวมพร้อมป้ายกำกับตามผลที่คาดหวังด้านล่าง

~~~mojo
def main():
    var total: Int = 0
    for value in range(1, 6):
        total = total + value
    print("Total:", total)
~~~

**เหตุผล:**

ใช้ขอบท้ายเป็น 6 เพื่อให้ลำดับรวมค่า 5 ด้วย

เริ่มตัวแปรสะสมที่ 0 แล้วบวกค่าเพิ่มทีละรอบ

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Total: 15
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep04-loops/solutions/exercise-1.mojo
~~~

## ข้อ 2

ใช้ `while` นับจำนวนครั้ง โดยเริ่ม `attempt` ที่ 1

แสดงครั้งที่ 1 ถึงครั้งที่ 3 แล้วออกจากลูป

~~~mojo
def main():
    var attempt: Int = 1
    while attempt <= 3:
        print("Attempt:", attempt)
        attempt = attempt + 1
~~~

**เหตุผล:**

ใช้เครื่องหมาย `<=` เพื่อรวมรอบที่ตัวนับเท่ากับ 3

เพิ่มค่าท้ายแต่ละรอบ เพื่อให้เงื่อนไขเป็นเท็จเมื่อค่าถึง 4

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Attempt: 1
Attempt: 2
Attempt: 3
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep04-loops/solutions/exercise-2.mojo
~~~
