# Student:Coco
# Assistant:Peter
# Scores:96
# To my best-loved piggy: This class has completed structure overall...
# but in order to adapt to different requirement we often overload multiple constructors.
class Guitar:


    def __init__(self, size_0, color_0, brand_0):
        self._size = size_0
        self._color = color_0
        self._brand = brand_0
        self.strumming = "wing wing"
        self.slapping = "dong dong"

    def  get_brand(self):
        return self._brand

    def set_color(self, color_1):
        self._color = color_1

    def set_brand(self, brand_1):
        self._brand = brand_1

    def recital(self):
        print(self.strumming, self.slapping)



Coco_Guitar=Guitar(41, 'yellow' ,'YAMAHA')
Coco_Guitar.set_color('white')
Coco_Guitar.set_brand('Fender')
Coco_Guitar.get_brand()
print(Coco_Guitar.get_brand())
Coco_Guitar.recital()
