thisdict = { 
    "brand":"honda",
    "model":"unicorn",
    "year":2020
}
print(thisdict)

thisdict = { 
    "brand":"honda",
    "model":"unicorn",
    "year":2020
}
print(thisdict)
thisdict ["brand" ]="bmw"
print (thisdict)

thisdict = { 
    "brand":"honda",
    "model":"unicorn",
    "year":2020
}
thisdict["color"]="pink"
print(thisdict)

thisdict . pop("model")
print(thisdict)

for x in thisdict :
    print(x)

for x in thisdict.items():
    print(x)

#nested dictionary

school = {
    "student1": {
        "name":"john",
        "age":15
    
    },
    "student2" :{
        "name": "ashuuuu",
        "age": 16
         
     },
     "student3" :{
        "name": "veduu",
        "age": 17
     }
}
print(school)
print(type(school))