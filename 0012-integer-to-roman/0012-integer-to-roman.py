class Solution:
    def intToRoman(self, num: int) -> str:
      
      digits = [(1000, "M"), 
                (900, "CM"), 
                (500, "D"), 
                (400, "CD"), 
                (100, "C"), 
                (90, "XC"), 
                (50, "L"), 
                (40, "XL"), 
                (10, "X"), 
                (9, "IX"), 
                (5, "V"), 
                (4, "IV"), 
                (1, "I")]
        
      roman = ""
        
      for value, symbol in digits:
          if num == 0: 
            return roman

          count, num = divmod(num, value)
          roman += (symbol * count)
            
      return roman
      
#         romans = {
#           1000: "M",
#           900: "CM",
#           500: "D",
#           400: "CD",
#           100: "C",
#           90: "XC",
#           50: "L",
#           40: "XL",
#           10: "X",
#           9: "IX",
#           5: "V",
#           4: "IV",
#           1: "I"
#         }
#         romNum = ""
#         i = 0
#         prev = num
#         for key in romans:
#           print("start for", key, num, prev)
#           if num == 0:
#             return romNum
          
#           num = prev % key
          
          
#           num = prev
#           while num > 0:
#             num -= key
#             romNum += romans[key]
          
# #           else:
# #             print("prev%key", num)
# #             while num > 0 and num != prev:
# #               print("num != prev")
# #               romNum += romans[key]

# #               prev = num
# #               num = prev % key
                

#             print(prev, num)
          
#           print("curr rom", romNum)
#         return romNum
        
#         # sumNum = 0
#         # i = 0
#         # while i < len(num):
#         #   if num[i] + num[i+1] in romans:
#         #     sumNum += romans[num[i] + num[i+1]]
#         #     i += 2
#         #   else:
#         #     sumNum += romans[num[i]]
#         #     i += 1
        
        
        