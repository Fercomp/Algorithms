def compress(chars) -> int:
    idx = 0
    compressed_idx = 0

    while idx < len(chars):
        count = 1
        while idx + 1 < len(chars) and chars[idx] == chars[idx + 1]:
            idx += 1
            count += 1 

        if count > 1:
            count_list = list(str(count))
            chars[compressed_idx] = chars[idx]
            for i in range(len(count_list)):  
                compressed_idx += 1
                chars[compressed_idx] = count_list[i]
                
            
        compressed_idx += 1
        idx += 1
    
    print(chars)
    return compressed_idx
        
    
print(compress(["a","a","a","b","b","a","a"]))