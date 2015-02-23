# image_width_checker
This script check images width under current directory recursively.
You need Python Imaging Library (PIL)

for example, <br>
$ python image_width_checker.py 700<br>
first argument 700 is min width of image.

output
```
----------------
----OK LIST-----
----------------
count:2
./hoge/hogehoge.jpg
./hoge/hogehoge/ok.png
----------------
----NG LIST-----
----------------
count:1
./hoge/ng1.jpg
```
