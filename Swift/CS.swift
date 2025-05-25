// String mathing

func stringMatching(_ input1: String, _ input2: String) -> Bool { 
    let string1 = Array(input1)
    let string2 = Array(input2)

    var matching = false
    
    var i = 0
    var j = 0
    
    while i < string1.count {
        if string1[i] == string2[j] {
            while j < string2.count {
                if i + j > string1.count - 1 { break }
                
                
                if string1[i + j] != string2[j] {
                    break
                }
                j += 1
            }
            matching = true
            break
        }
        i += 1
    }

    return matching
}

print(stringMatching("ABC", "BCDEF"))