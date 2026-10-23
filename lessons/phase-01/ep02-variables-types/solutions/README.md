# เฉลย EP.2

ลองทำโจทย์ใน [บทเรียน](../README.md) ก่อนเปิดหน้านี้

วิธีอื่นที่ได้ผลตรงตามโจทย์ถือว่าใช้ได้

## ข้อ 1

กำหนดค่าเริ่มต้นของ `sample_count` เป็น 10

แสดงค่าก่อนเปลี่ยน จากนั้นเพิ่มอีก 2 แล้วแสดงค่าใหม่

~~~mojo
def main():
    var sample_count: Int = 10
    print("Before:", sample_count)
    sample_count = sample_count + 2
    print("After:", sample_count)
~~~

**เหตุผล:**

ด้านขวาอ่านค่าเดิมแล้วบวก 2

จากนั้นจึงนำผลเก็บกลับในตัวแปรชนิดเดิม

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Before: 10
After: 12
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep02-variables-types/solutions/exercise-1.mojo
~~~

## ข้อ 2

ใช้ `String` เก็บชื่อชุดข้อมูล และ `Float64` เก็บอุณหภูมิ

แสดงข้อมูลแต่ละรายการคนละบรรทัด ตามผลที่คาดหวังด้านล่าง

~~~mojo
def main():
    var dataset: String = "demo-02"
    var temperature: Float64 = 30.5
    print("Dataset:", dataset)
    print("Temperature:", temperature)
~~~

**เหตุผล:**

ชนิดของตัวแปรตรงกับข้อมูลที่ต้องการเก็บ

คำสั่ง `print` ในตัวอย่างรับป้ายข้อความและค่าของตัวแปร แล้วแสดงโดยคั่นด้วยช่องว่าง

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Dataset: demo-02
Temperature: 30.5
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep02-variables-types/solutions/exercise-2.mojo
~~~
