from PIL import Image,ImageFilter, ImageOps

#1将RGB图转化为灰度图。
#2灰度图进行反色操作。
#3对步骤2中的图片进行高斯模糊
#4将步骤1中的灰度图像和步骤三中的模糊反色图像混合


tp = Image.open('xwmr.jpeg')   #读取图片
x,y = tp.size                  # 获得图片的长和宽
tp_gray = tp.convert('L')      #灰色化
#convert后面可以接9个不同模式，1，L，P，RGB，RGBA，CMYK，YCbCr,I，F
tp_mix = tp_gray.copy()
tp_inv = ImageOps.invert(tp_gray)    #取反色
for i in range(20):                  #模糊处理，循环次数越多越模糊
    tp_blur = tp_inv.filter(ImageFilter.BLUR)

l=1
for i in range(x):       # 遍历图片的每一个像素点
    for j in range(y):
        a = tp_gray.getpixel((i,j))    # 获取像素点的值
        b = tp_blur.getpixel((i,j))
        tp_mix.putpixel((i,j),min(int(a*255/(256-b*l)),255))
        # image.putpixel(位置，值)函数就是用来修改像素点的值的
        # a*255/(256-b) 可以达到素描效果，原理不清楚
        # min()为了防止像素点数据超过255


#控制图片大小
t = 1                    #调节比例
tp_mix = tp_mix.resize((int(x*t), int(y*t)), Image.ANTIALIAS)

#tp_mix.save('D:/wjcksm.jpg')
tp_mix.show()



