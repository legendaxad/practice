# print("==== Iterable objects & Range ====")

# Iterable objects>string,dict,tuple,list,rang,map,filter


# range_obj = range(3)
# print("range_obj:", range_obj)

# text = "MIT"

# for letter in text:
#     print(f"the letter : {letter}")
# for ele in range_obj:
#     print(f"the letter : {ele}")


print("==== Dictionary ====")

# Dictionary is Json object!
person = {
    "name": "Ali",
    "age": 35,
    "single": True
}
print(f"the person : {person}")

person_obj = dict(name="Ali", age=35, single=True)
print(f"the person_obj : {person_obj}")
# G-TASK

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin. MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# method>get()
name = person_obj.get("name")
print(name)

del person_obj["single"]

for key in person_obj:
    print(f"the key :{key} =>value {person_obj.get(key)}")
