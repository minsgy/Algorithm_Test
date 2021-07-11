function solution(d, m) {
    let answer = 0;
    let box_count = 1;
   
    for (let box of d){
        if (m >= 0){
            if (box_count <= box){
                answer += 1;
                m -= box_count;
                box_count *= 2;
            }
            else {
                box_count = 1;
                answer += 1;
            }
        } 
    }
    
    if (m <= 0){
        return answer;
    }
    
    return -1;
}