split("\n")|map(split(","))|
   map({"postdate":.[0],
        "place":"1",
        "temperature":.[1],
        "pressure":.[3],
        "humidity":.[5],
        "lux":.[7],
})
