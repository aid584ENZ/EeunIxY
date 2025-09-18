# 代码生成时间: 2025-09-18 18:20:13
import scrapy


# 排序算法实现类
class SortingAlgorithm:
    """
    排序算法实现类，包括冒泡排序、插入排序和快速排序。
    """
    def bubble_sort(self, data_list):
        """冒泡排序算法实现。

        Args:
            data_list (list): 待排序的列表。

        Returns:
            list: 排序后的列表。
        """
        n = len(data_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if data_list[j] > data_list[j+1]:
                    data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
        return data_list

    def insertion_sort(self, data_list):
        """插入排序算法实现。

        Args:
            data_list (list): 待排序的列表。

        Returns:
            list: 排序后的列表。
        """
        for i in range(1, len(data_list)):
            key = data_list[i]
            j = i - 1
            while j >= 0 and key < data_list[j]:
                data_list[j + 1] = data_list[j]
                j -= 1
            data_list[j + 1] = key
        return data_list

    def quick_sort(self, data_list):
        """快速排序算法实现。

        Args:
            data_list (list): 待排序的列表。

        Returns:
            list: 排序后的列表。
        """
        if len(data_list) <= 1:
            return data_list
        pivot = data_list[0]
        less = [x for x in data_list[1:] if x <= pivot]
        greater = [x for x in data_list[1:] if x > pivot]
        return self.quick_sort(less) + [pivot] + self.quick_sort(greater)


# Scrapy Spider类
class SortingSpider(scrapy.Spider):
    """
    排序算法Spider类。
    """
    name = 'sorting_spider'
    start_urls = ['']

    def parse(self, response):
        """
        解析请求的响应内容。
        """
        try:
            # 假设我们从响应中提取了一个待排序的数字列表
            data_list = response.css('.sorting-list::text').getall()
            data_list = [int(item.strip()) for item in data_list]
            
            # 创建排序算法实现类的实例
            sorting_algorithm = SortingAlgorithm()
            
            # 调用不同的排序算法进行排序
            sorted_list = sorting_algorithm.quick_sort(data_list)
            
            # 将排序结果输出到控制台
            print('Sorted List:', sorted_list)
        except Exception as e:
            print('Error:', e)
