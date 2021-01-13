# PicsumPlaceholder
A simple script to get Picsum image

> python3 get_images.py [url_args] [number_of_images]
> 

## examples

下载10张 200x200 的  
`python3 get_images.py 200/200 10`  

下载 1张指定id的图  
`python3 get_images.py id/237/200/300 1`  

根据随机种子下图，seed一样，则返回图片一样  
`python3 get_images.py seed/{seed}/200/300 10`  

下载200x300 的灰度图10张
`python3 get_images.py 200/300?grayscale 10`  

类似的还有：
`python3 get_images.py 200/300?blur=2 10`    
`python3 get_images.py 200/300.webp 10`    