# 代码生成时间: 2025-08-02 19:06:05
import scrapy


# 排序算法实现爬虫
class SortingAlgorithmSpider(scrapy.Spider):
    '''
    该爬虫用于实现排序算法，包括冒泡排序、插入排序、选择排序等。
    '''
    name = 'sorting_algorithm_spider'
    allowed_domains = []
    start_urls = []

    def parse(self, response):
        # 这里可以解析网页内容，获取需要排序的数据
        pass

    def bubble_sort(self, arr):
        """冒泡排序算法实现"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def insertion_sort(self, arr):
        """插入排序算法实现"""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def selection_sort(self, arr):
        """选择排序算法实现"""
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def run_sorting_algorithms(self, arr):
        """运行排序算法并打印结果"""
        try:
            # 冒泡排序
            sorted_arr = self.bubble_sort(arr.copy())
            print('Bubble Sort: ', sorted_arr)

            # 插入排序
            sorted_arr = self.insertion_sort(arr.copy())
            print('Insertion Sort: ', sorted_arr)

            # 选择排序
            sorted_arr = self.selection_sort(arr.copy())
            print('Selection Sort: ', sorted_arr)

        except Exception as e:
            print('Error occurred while sorting:', str(e))

    def start_requests(self):
        # 示例数据
        arr = [64, 34, 25, 12, 22, 11, 90]

        # 运行排序算法
        self.run_sorting_algorithms(arr)
