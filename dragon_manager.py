# start with 3 heads
# 0...200 - + 3 heads
# 201...300 - + 2 heads
# > 300 - +1 head

class DragonManager:
    @staticmethod
    def calculate_total_heads(age):
        head = 3

        if isinstance(age, int) and age > 0:
            if age <= 200:
                head += age * 3
            elif age <= 300:
                head += 600 + (age - 200) * 2
            else:
                head += 800 + age - 300
            return head
        else:
            return 0
