class Solution:

    #this encodes a list of strings into a single, decodable string
    def encode(self, strs: List[str]) -> str:
        #count the length of each string

        result = ""

        for s in strs:
            result += str(len(s))
            result += "/"
            result += s
        

        #then, encode the string with the following pattern:
        #{length}string{length}string{length}string
        #like this: 4grub5piano9arbitrary

        print(f"Encoding result: {result}")
        return result


    #this takes the result from the above method and turns it back into a list of strings  
    def decode(self, s: str) -> List[str]:
       result: list[str] = []
       length: int
       i = 0
       temp: str

       #loop till the index is at the very end.
       while i < len(s):
            temp_str= ""
            #grab the value only. knows when to stop because there is a / in between.
            while(i < len(s) and s[i].isdigit()):
                temp_str += s[i]
                i +=1
            i+=1 #moves past the /
            print(f"length: {temp_str}")
            length = int(temp_str)
            print(f"Length of this string: {length}")
            
            temp = s[i:i+length]
            print(f"Temporary string: {temp}")
            result.append(temp)
            i += length #consider that string as read and appended, now advance to next
            print(f"{i}, {len(s)}")

       #print("i exited the loop here right")


       return result
          

