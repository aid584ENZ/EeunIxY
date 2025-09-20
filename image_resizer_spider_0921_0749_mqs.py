# 代码生成时间: 2025-09-21 07:49:00
import os
from PIL import Image
import scrapy
from scrapy.crawler import CrawlerProcess


class ImageResizerSpider(scrapy.Spider):
    name = 'image_resizer'
    allowed_domains = []
    start_urls = []

    def __init__(self, image_paths=[], target_size=(800, 600), output_dir='./resized_images', *args, **kwargs):
        super(ImageResizerSpider, self).__init__(*args, **kwargs)
        self.image_paths = image_paths  # 需要调整尺寸的图片路径列表
        self.target_size = target_size  # 目标尺寸
        self.output_dir = output_dir  # 输出目录

    def parse(self, response):
        # 遍历所有图片路径
        for image_path in self.image_paths:
            try:
                # 打开图片文件
                with Image.open(image_path) as img:
                    # 调整图片尺寸
                    img = img.resize(self.target_size)
                    # 构建输出路径
                    base_name = os.path.basename(image_path)
                    output_path = os.path.join(self.output_dir, base_name)
                    # 保存调整后的图片
                    img.save(output_path)
                    self.log(f'Image resized and saved to {output_path}')
            except IOError as e:
                self.log(f'Error resizing image {image_path}: {e}')


# 使用CrawlerProcess运行爬虫
def run_spider(image_paths, target_size, output_dir):
    process = CrawlerProcess({
        'USER_AGENT': 'ImageResizerSpider (+http://www.yourwebsite.com)',
    })
    process.crawl(ImageResizerSpider, image_paths=image_paths, target_size=target_size, output_dir=output_dir)
    process.start()


if __name__ == '__main__':
    # 图片路径列表
    image_paths = [
        'path/to/image1.jpg',
        'path/to/image2.png',
        # 更多图片路径...
    ]
    # 目标尺寸
    target_size = (800, 600)
    # 输出目录
    output_dir = './resized_images'
    run_spider(image_paths, target_size, output_dir)