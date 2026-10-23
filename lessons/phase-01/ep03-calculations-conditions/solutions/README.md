# เฉลย EP.3

ลองทำโจทย์ใน [บทเรียน](../README.md) ก่อนเปิดหน้านี้

วิธีอื่นที่ได้ผลตรงตามโจทย์ถือว่าใช้ได้

## ข้อ 1

นำโค้ดขั้นที่ 3 มาทดลองเปลี่ยนอุณหภูมิทีละค่า:

~~~text
-1, 0, 29, 30, 31
~~~

เขียนตารางผลก่อนรัน

~~~mojo
def main():
    var temperature: Int = -1
    var threshold: Int = 30
    print("Temperature:", temperature)
    if temperature < 0:
        print("Status: INVALID")
    elif temperature >= threshold:
        print("Status: WARNING")
    else:
        print("Status: OK")
~~~

**เหตุผล:**

| อุณหภูมิ | สถานะ |
|---|---|
| -1 | `INVALID` |
| 0 | `OK` |
| 29 | `OK` |
| 30 | `WARNING` |
| 31 | `WARNING` |

ไฟล์นี้ตั้งต้นที่ -1 ให้เปลี่ยนค่าแล้วรันทีละกรณี

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Temperature: -1
Status: INVALID
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep03-calculations-conditions/solutions/exercise-1.mojo
~~~

## ข้อ 2

ตั้งค่า `threshold` และ `temperature` เป็น 35

ค่าเท่ากับเกณฑ์ยังต้องแสดงสถานะ:

~~~text
WARNING
~~~

~~~mojo
def main():
    var temperature: Int = 35
    var threshold: Int = 35
    if temperature >= threshold:
        print("Status: WARNING")
    else:
        print("Status: OK")
~~~

**เหตุผล:**

เปลี่ยนค่าเกณฑ์ แต่ยังคงเงื่อนไขว่าค่าเท่ากับเกณฑ์ต้องเตือน

จึงใช้เครื่องหมาย `>=`

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Status: WARNING
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep03-calculations-conditions/solutions/exercise-2.mojo
~~~
