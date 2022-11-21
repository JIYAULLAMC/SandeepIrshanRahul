
class Heart:
    def __init__(self, name, heart_beat):
        self.name = name
        self.heart_beat = heart_beat


    def heart_analysis(self):
        if 70<= self.heart_beat <= 90:
            print("normal man ")

        else:
            print("abnormal man")

class Patient:

    def __init__(self, name, heart_beat):
        self.name = name 
        self.heart_beat = heart_beat
        self.h1 = Heart(self.name, self.heart_beat)

    def need_meditation(self):
        if 70 <= self.h1.heart_beat <=90:
            return False
        else:
            return True

    def need_surgery(self):
        if 70 <= self.h1.heart_beat <=90:
            return False
        else:
            return True

p1 = Patient("sagar", 75)


'''

>>> p1
<__main__.Patient object at 0x0000020848DD4FD0>
>>> p1.name
'sagar'
>>> p1.heart_beat
75
>>> p1.h1.name
'sagar'
>>> p1.h1.heart_beat
75
>>> p1.h1.heart_analysis()
normal man
>>> p1.need_meditation()
False
>>>

'''