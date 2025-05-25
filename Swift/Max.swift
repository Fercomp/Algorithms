// Find the maximum element in an array

func maximum(_ input: [Int]) -> Int {
    var max = input[0]

    for i in 1..<input.count {
        if input[i] > max {
            max = input[i]
        }
    }
    return max
}

print(maximum([4,5,1,8,9,10]))
print(maximum([9]))