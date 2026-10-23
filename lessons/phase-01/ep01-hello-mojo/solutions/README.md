# เฉลย EP.1

ลองทำโจทย์ใน [บทเรียน](../README.md) ก่อนเปิดหน้านี้

วิธีอื่นที่ได้ผลตรงตามโจทย์ถือว่าใช้ได้

## ข้อ 1

เปลี่ยนชื่อชุดข้อมูลและสถานะ ให้แสดงผลครบ 3 บรรทัดตามโจทย์

~~~mojo
def main():
    print("Hello, Mojo!")
    print("Dataset: demo-02")
    print("Status: waiting")
~~~

**เหตุผล:**

เปลี่ยนเฉพาะข้อความในเครื่องหมายคำพูด

จำนวนคำสั่ง `print` ยังเท่าเดิม จึงแสดงผล 3 บรรทัด

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Hello, Mojo!
Dataset: demo-02
Status: waiting
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep01-hello-mojo/solutions/exercise-1.mojo
~~~

## ข้อ 2

เพิ่มข้อความต่อท้ายโปรแกรมเดิม:

~~~text
Author: learner
~~~

คาดเดาจำนวนบรรทัดทั้งหมดก่อนรัน

~~~mojo
def main():
    print("Hello, Mojo!")
    print("Dataset: demo-01")
    print("Status: ready")
    print("Author: learner")
~~~

**เหตุผล:**

เพิ่มคำสั่ง `print` อีกหนึ่งครั้งภายใน `main`

โปรแกรมจึงแสดงผลรวม 4 บรรทัด

**ผลที่คาดหวังจากไฟล์นี้:**

~~~text
Hello, Mojo!
Dataset: demo-01
Status: ready
Author: learner
~~~

รันจากโฟลเดอร์ MOJO:

~~~bash
mojo lessons/phase-01/ep01-hello-mojo/solutions/exercise-2.mojo
~~~
